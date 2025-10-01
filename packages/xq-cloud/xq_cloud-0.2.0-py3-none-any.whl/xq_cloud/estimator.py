from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any

import numpy as np
import qiskit.qasm2
from qiskit.circuit import QuantumCircuit
from qiskit.primitives import BaseEstimatorV2 as BaseEstimator
from qiskit.primitives import DataBin, PrimitiveJob, PrimitiveResult, PubResult
from qiskit.primitives.backend_estimator_v2 import BindingsArray
from qiskit.primitives.containers.estimator_pub import EstimatorPub, EstimatorPubLike
from qiskit.primitives.containers.observables_array import ObservablesArray
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import Target

# from xq_cloud.job import XQCloudJob
from .client import XQCloudClient
from .target import create_xq1_target
from .transpiler import transpile as xq_transpile


def rotate_for_pauli_label(circ: QuantumCircuit, label: str) -> QuantumCircuit:
    """
    Append basis-change rotations so that measuring Z gives expectation of label.
    label uses Qiskit's convention: leftmost char corresponds to highest qubit index.
    """
    circ = circ.copy()
    n = circ.num_qubits
    for char_index, p in enumerate(label):
        # map label position to circuit qubit index
        qubit_index = n - 1 - char_index
        match p:
            case "X":
                circ.h(qubit_index)
            case "Y":
                circ.sdg(qubit_index)
                circ.h(qubit_index)
            case _:
                # I or Z -> no rotation needed
                pass
    return circ


def _expectation_from_probs(label: str, probs: dict[str, float]) -> float:
    """Compute ⟨P⟩ for Pauli string ``label`` from bitstring probabilities.

    ``label`` uses Qiskit's convention (leftmost char is highest qubit index).
    Bitstrings in ``probs`` follow Qiskit's density-matrix ``probabilities_dict`` convention
    where leftmost bit corresponds to highest qubit index.
    """
    if len(probs) == 0:
        return 0.0
    n = len(next(iter(probs.keys())))
    assert len(label) == n, "Observable qubit count must match circuit qubit count"

    exp_val = 0.0
    for bitstr, p in probs.items():
        # Compute eigenvalue of Z^{mask} on bitstring: (-1)^{sum bits on masked positions}
        parity = 0
        for char_index, pauli in enumerate(label):
            if pauli == "I":
                continue
            if bitstr[char_index] == "1":
                parity ^= 1
        eigenvalue = 1.0 if parity == 0 else -1.0
        exp_val += eigenvalue * float(p)
    return float(exp_val)


def _observable_to_terms(observable: SparsePauliOp, num_qubits: int) -> list[tuple[str, complex]]:
    """Normalize a ``SparsePauliOp`` into explicit (label, coeff) terms.

    Pads labels to circuit width if necessary.
    """
    terms: list[tuple[str, complex]] = []
    for lbl, coeff in observable.to_list():
        # ``lbl`` is ordered left->right as highest->lowest qubit index.
        if len(lbl) < num_qubits:
            lbl = "I" * (num_qubits - len(lbl)) + lbl
        terms.append((lbl, complex(coeff)))
    return terms


class XQCloudEstimator:
    """Estimator-like primitive that submits circuits to XQ Cloud.

    This primitive evaluates expectation values of Pauli-sum observables by applying
    local basis-change rotations and using the remote service to obtain exact
    probabilities of Z-basis outcomes for the rotated circuits.
    """

    def __init__(
        self,
        client: XQCloudClient,
        *,
        target: Target | None = None,
        backend_name: str = "xq1-sim-aer",
    ) -> None:
        self.client = client
        self.target = target or create_xq1_target()
        self.backend_name = backend_name

    def run(
        self,
        circuits: QuantumCircuit | Sequence[QuantumCircuit],
        observables: SparsePauliOp | Sequence[SparsePauliOp],
        *,
        parameter_values: Sequence[Sequence[float]] | Sequence[float] | None = None,
    ) -> _CompletedJob:
        circ_list = (
            circuits if isinstance(circuits, Sequence) and not isinstance(circuits, QuantumCircuit) else [circuits]
        )  # type: ignore[list-item]
        obs_list = (
            observables
            if isinstance(observables, Sequence) and not isinstance(observables, SparsePauliOp)
            else [observables]
        )  # type: ignore[list-item]

        if len(circ_list) != len(obs_list):
            # Basic zip behavior only (no full broadcasting)
            raise ValueError("circuits and observables must have the same length")

        # Normalize parameter values: either one entry per circuit or None
        if parameter_values is None:
            params_list: list[Any | None] = [None] * len(circ_list)
        elif isinstance(parameter_values, Sequence) and len(circ_list) == 1:
            # Accept 1 circuit with 1D param list
            params_list = [parameter_values]  # type: ignore[assignment]
        elif isinstance(parameter_values, Sequence) and len(parameter_values) == len(circ_list):
            params_list = list(parameter_values)  # type: ignore[list-item]
        else:
            raise ValueError("parameter_values shape does not match circuits")

        expectation_values: list[float] = []
        metadatas: list[dict[str, Any]] = []

        for circuit, observable, params in zip(circ_list, obs_list, params_list):
            if not isinstance(observable, SparsePauliOp):
                raise TypeError("Only SparsePauliOp observables are supported")

            # Bind circuit parameters
            if params is None or len(circuit.parameters) == 0:
                bound = circuit
            else:
                bound = circuit.assign_parameters(params, inplace=False)

            num_qubits = bound.num_qubits

            # Evaluate each Pauli term separately and sum with coefficients
            value = 0.0
            for label, coeff in _observable_to_terms(observable, num_qubits):
                # Build rotated circuit for this term
                rotated = rotate_for_pauli_label(bound, label)

                # Transpile to device ISA and dump QASM2
                isa = xq_transpile(rotated, target=self.target)
                qasm = qiskit.qasm2.dumps(isa)

                # Submit and get exact probabilities
                circuit_id = self.client.queue_circuit(qasm, backend=self.backend_name)
                probs = self.client.wait_for_result(circuit_id)

                # Compute expectation of the (rotated) Z-product
                term_expectation = _expectation_from_probs(label, probs)
                value += coeff.real * term_expectation

            expectation_values.append(float(value))
            metadatas.append({"num_qubits": num_qubits})

        result = EstimatorResult(values=np.asarray(expectation_values, dtype=float), metadata=metadatas)
        return _CompletedJob(result)


class XQCloudEstimatorV2(BaseEstimator):
    """Estimator V2 implementation that evaluates exact expectation values via XQ Cloud.

    This computes expectation values by rotating into the appropriate
    measurement bases and using the remote service to return Z-basis
    probabilities for the rotated circuits.
    """

    def __init__(
        self,
        client: XQCloudClient,
        *,
        target: Target | None = None,
        backend_name: str = "xq1-sim-aer",
    ) -> None:
        self.client = client
        self.target = target or create_xq1_target()
        self._default_precision = 0.01  # unused (no shots), but required by API
        self.backend_name = backend_name

    def run(
        self,
        pubs: Iterable[EstimatorPubLike],
        *,
        precision: float | None = None,
    ) -> PrimitiveJob[PrimitiveResult[PubResult]]:
        default_precision = self._default_precision if precision is None else precision
        coerced_pubs = [EstimatorPub.coerce(pub, default_precision) for pub in pubs]
        job = PrimitiveJob(self._run, coerced_pubs)
        job._submit()
        return job

    def _run(self, pubs: list[EstimatorPub]) -> PrimitiveResult[PubResult]:
        pub_results: list[PubResult] = []
        for pub in pubs:
            circuit = pub.circuit
            obs_array: ObservablesArray = pub.observables
            param_values: BindingsArray | None = pub.parameter_values

            # Broadcast parameter shape with observables shape
            param_shape = getattr(param_values, "shape", ())
            obs_np = obs_array.sparse_observables_array()

            # Build broadcasted indices and observables per position
            param_indices = np.fromiter(np.ndindex(param_shape), dtype=object).reshape(param_shape)
            bc_param_ind, bc_obs = np.broadcast_arrays(param_indices, obs_np)

            evs = np.zeros(bc_param_ind.shape, dtype=float)
            stds = np.zeros_like(evs)

            for index in np.ndindex(bc_param_ind.shape):
                # Bind parameters for this index
                if param_values is None or param_values.shape == ():
                    # For scalar/None bindings, bind all if a mapping exists, otherwise no-op
                    bound = circuit if param_values is None else param_values.bind_all(circuit)[()]
                else:
                    bound = param_values.bind(circuit, bc_param_ind[index])

                # Evaluate expectation for this observable element
                sparse_obs = bc_obs[index]
                value = 0.0
                for term_label, qubit_indices, coeff in sparse_obs.to_sparse_list():
                    full_label = _build_full_label(term_label, qubit_indices, bound.num_qubits)
                    rotated = rotate_for_pauli_label(bound, full_label)
                    isa = xq_transpile(rotated, target=self.target)
                    qasm = qiskit.qasm2.dumps(isa)
                    circuit_id = self.client.queue_circuit(qasm, backend=self.backend_name)
                    probs = self.client.wait_for_result(circuit_id)
                    term_expectation = _expectation_from_probs(full_label, probs)
                    value += term_expectation * (coeff.real)
                evs[index] = value

            data_bin = DataBin(evs=evs, stds=stds, shape=evs.shape)
            pub_results.append(
                PubResult(
                    data_bin,
                    metadata={
                        "target_precision": pub.precision,
                        "shots": None,
                        "circuit_metadata": pub.circuit.metadata,
                    },
                )
            )

        return PrimitiveResult(pub_results, metadata={"version": 2})


def _build_full_label(term_label: str, qubit_indices: list[int], num_qubits: int) -> str:
    # Build label string of length num_qubits, leftmost char for highest qubit index
    chars = ["I"] * num_qubits
    for pos, q in enumerate(qubit_indices):
        char = term_label[pos]
        chars[num_qubits - 1 - q] = char
    return "".join(chars)
