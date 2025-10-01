import qiskit.circuit.library as gates
from qiskit.circuit import Parameter
from qiskit.transpiler import InstructionProperties, Target

from .gates import DDCRotXGate, NCRXGate


def create_xq1_target() -> Target:
    """
    Create a Qiskit transpiler target for the XQ1 device based on a single nitrogen-vacancy center.
    """

    target = Target(
        description="XQ1 target based on a single nitrogen-vacancy center",
        num_qubits=4,
    )

    # Arbitrary angle rotations around the x-axis by direct driving
    # on the electron and nitrogen nuclear spins.
    theta = Parameter('theta')
    target.add_instruction(
        gates.RXGate(theta),
        {
            (0,): InstructionProperties(),
            (1,): InstructionProperties(),
        },
    )
    # Arbitrary angle rotations around the y-axis by phase shifted direct driving
    # on the electron and nitrogen nuclear spins.
    target.add_instruction(
        gates.RYGate(theta),
        {
            (0,): InstructionProperties(),
            (1,): InstructionProperties(),
        },
    )
    # Arbitrary angle rotations around the z-axis by virtual frame rotations
    # on all qubits.
    target.add_instruction(
        gates.RZGate(theta),
        {
            (0,): InstructionProperties(),
            (1,): InstructionProperties(),
            (2,): InstructionProperties(),
            (3,): InstructionProperties(),
        },
    )
    # Fixed-angle (sqrt(X)) rotations around the x-axis of the carbon-13 nuclear spins.
    # Implemented using a dynamical decoupling sequence which creates an unconditional rotation
    # as described in https://arxiv.org/pdf/1205.4128.pdf.
    target.add_instruction(
        gates.SXGate(),
        {
            (2,): InstructionProperties(),
            (3,): InstructionProperties(),
        },
    )
    # Fixed-angle rotations around the x-axis of the carbon-13 nuclear spins
    # controlled by the electron spin and implemented using a dynamical decoupling sequence
    # as described in https://arxiv.org/pdf/1205.4128.pdf.
    target.add_instruction(
        DDCRotXGate(),
        {
            (0, 2): InstructionProperties(),
            (0, 3): InstructionProperties(),
        },
    )
    # Controlled arbitrary angle x rotation gate with a negated control qubit.
    # Implemented by selective driving of the relevant hyperfine transition.
    # Available between the electron spin and the nitrogen nuclear spin.
    target.add_instruction(
        NCRXGate(theta),
        {
            (0, 1): InstructionProperties(),
            (1, 0): InstructionProperties(),
        },
    )
    # Controlled arbitrary angle x rotation gate.
    # Implemented by selective driving of the relevant hyperfine transition.
    # Available between the electron spin and the nitrogen nuclear spin.
    target.add_instruction(
        gates.CRXGate(theta),
        {
            (0, 1): InstructionProperties(),
        },
    )

    return target
