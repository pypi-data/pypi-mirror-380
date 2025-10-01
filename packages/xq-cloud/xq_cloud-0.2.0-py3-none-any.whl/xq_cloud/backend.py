from __future__ import annotations

import qiskit.qasm2
from qiskit.circuit import QuantumCircuit
from qiskit.providers import BackendV2 as Backend
from qiskit.providers import JobV1 as Job
from qiskit.providers import Options
from qiskit.providers.jobstatus import JobStatus
from qiskit.result import Result
from qiskit.result.models import ExperimentResultData
from qiskit.result.result import ExperimentResult
from qiskit.transpiler import Target
from typing_extensions import override

from xq_cloud.client import XQCloudClient
from xq_cloud.target import create_xq1_target


class XQCloudJob(Job):
    _backend: XQCloudBackend
    _job_id: str
    shots: int

    def __init__(self, backend: XQCloudBackend, job_id: str, shots: int = -1):
        super().__init__(backend, job_id)
        self.shots = shots

    @override
    def result(self):
        success = False
        expectation_values: dict[str, float] | None = None
        try:
            success = True
            expectation_values = self._backend._client.wait_for_result(
                int(self._job_id),
                poll_interval_seconds=0.5,
                timeout_seconds=30,  # TODO: This might be too short
            )
        except TimeoutError:
            success = False

        return Result(
            backend_name=self._backend.name,
            backend_version=self._backend.backend_version,
            job_id=self._job_id,
            success=success,
            results=[
                ExperimentResult(
                    shots=self.shots,
                    success=success,
                    data=ExperimentResultData(expectation_values=expectation_values),
                )
            ],
        )

    @override
    def submit(self):
        """This is a no-op as the job is submitted on creation."""
        return

    def cancel(self):
        """Attempt to cancel the job."""
        # TODO: Implement job cancellation in the API
        raise NotImplementedError

    @override
    def status(self) -> JobStatus:
        result = self._backend._client.get_result(int(self._job_id))
        if result.status == 'running':
            status = JobStatus.RUNNING
        elif result.status == 'completed':
            status = JobStatus.DONE
        else:
            status = JobStatus.ERROR
        return status


class XQCloudBackend(Backend):
    """Qiskit Backend describing the XQ Cloud target."""

    def __init__(
        self,
        client: XQCloudClient,
        *,
        target: Target,
        name: str = "xq-cloud-xq1",
        description: str = "XQ Cloud backend for XQ1 target",
        backend_version: str = "0.0.0",
    ) -> None:
        super().__init__(
            provider=None,
            name=name,
            description=description,
            backend_version=backend_version,
        )
        self._client = client
        self._target = target or create_xq1_target()
        self._options = self._default_options()

    @property
    def target(self) -> Target:  # type: ignore[override]
        return self._target

    @property
    def options(self) -> Options:  # type: ignore[override]
        return self._options

    @property
    def max_circuits(self) -> int | None:  # type: ignore[override]
        return 1

    @override
    def run(self, run_input: QuantumCircuit | list[QuantumCircuit], **options) -> XQCloudJob:  # type: ignore[override]
        if isinstance(run_input, list):
            # Unwrap single circuit if needed
            assert len(run_input) == 1, f"Only single-circuit jobs are supported by the {self.name} backend"
            circuit = run_input[0]
        else:
            circuit = run_input

        # Validate the circuit is compatible with this backend's target before submission
        self.assert_compatible(circuit, self.target)

        serialized_circuit = qiskit.qasm2.dumps(circuit)
        job_id = self._client.queue_circuit(serialized_circuit, backend=self.name)

        return XQCloudJob(
            backend=self,
            job_id=str(job_id),
        )

    @classmethod
    def _default_options(cls) -> Options:  # type: ignore[override]
        """Default backend options."""
        return Options()

    def __repr__(self) -> str:
        return f"XQCloudBackend(name={self.name}, description={self.description})"

    @staticmethod
    def assert_compatible(circuit: QuantumCircuit, target: Target) -> None:
        """Raise ValueError if ``circuit`` is not compatible with ``target``.

        Checks:
        - Circuit qubit count does not exceed target qubits.
        - All instructions are in the target's operation set (barrier is ignored).
        - Each instruction is applied to a qubit tuple allowed by the target.
        """
        # Basic qubit count check
        if circuit.num_qubits > int(target.num_qubits):
            raise ValueError(f"Circuit uses {circuit.num_qubits} qubits, but target supports only {target.num_qubits}.")

        allowed_ops = set(target.operation_names)
        errors: list[str] = []

        for inst in circuit.data:
            op = inst.operation

            # Skip barriers
            if op.name == "barrier":
                continue

            # Disallow measurements for this backend
            if op.name == "measure":
                errors.append("Unsupported operation 'measure' — remove measurements before submission")
                continue

            name = op.name
            if name not in allowed_ops:
                errors.append(f"Unsupported operation '{name}'. Supported: {sorted(allowed_ops)}")
                continue

            # Validate the specific qubit tuple is allowed by the target
            qargs = tuple(circuit.find_bit(qb).index for qb in inst.qubits)
            try:
                qarg_map = target[name]
            except Exception:
                errors.append(f"Target mapping for operation '{name}' is unavailable")
                continue

            if qargs not in qarg_map:
                allowed_qargs = sorted(map(tuple, qarg_map.keys()))
                errors.append(
                    f"Operation '{name}' on qubits {qargs} is not allowed for target; "
                    f"allowed qubit tuples: {allowed_qargs}"
                )

        if errors:
            hint = "Transpile the circuit for this target first."
            raise ValueError("; ".join(errors) + ". " + hint)
