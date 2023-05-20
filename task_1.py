#!pip install qiskit Не забыть установить модуль, если его нет
from qiskit import QuantumCircuit, execute, Aer


def task1():
    qc = QuantumCircuit(2, 1)
    qc.h(0)
    qc.cx(0, 1)
    qc.unitary([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], [0, 1], label='U')
    qc.cx(0, 1)
    qc.h(0)
    qc.measure(0, 0)
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    print(counts)
    # Визуализация схемы сохраняется в виде картинки
    qc.draw(output='mpl', filename='task1.png')
