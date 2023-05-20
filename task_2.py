import matplotlib.pyplot as plt
from qiskit import Aer
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram


# Cоздание пары Белла в виде схемы
def bellPairInit():
    qc = QuantumCircuit(2)
    qc.h(1)
    qc.cx(1, 0)
    return qc


# Энкодинг
def encodeMessage(qc, qubit, msg):
    if len(msg) != 2 or not set(msg).issubset({"0", "1"}):
        raise ValueError(f"message '{msg}' is invalid")
    if msg[1] == "1":
        qc.x(qubit)
    if msg[0] == "1":
        qc.z(qubit)
    return qc


# Декодинг
def decodeMessage(qc):
    qc.cx(1, 0)
    qc.h(1)
    return qc


def task2():
    calcResult('00')
    calcResult('01')
    calcResult('10')
    calcResult('11')


def calcResult(message):
    # Получение пары Белла
    qc = bellPairInit()
    qc.barrier()
    # Кубит 0 переходит к A, а кубит 1 переходит к B
    # A кодирует сообщение в кубит 1.
    qc = encodeMessage(qc, 1, message)
    qc.barrier()
    # A отправляет кубит адресату B
    # B применяет функцию декодирования
    qc = decodeMessage(qc)
    # B измеряет кубит
    qc.measure_all()
    # Вычисление результата, сохранение схемы и гистограммы
    qc.draw(output='mpl', filename=f'task2_{message}.png')
    aer_sim = Aer.get_backend('aer_simulator')
    result = aer_sim.run(qc).result()
    counts = result.get_counts(qc)
    print("Task 2 result:", counts)
    plot_histogram(counts)
    plt.savefig('histogram_task2.png')
