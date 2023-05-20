from qiskit import *
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt


def task3():
    # Cоздание квантовой схемы из 3х кубитов и 3х битов и вывод схемы
    telCirc = QuantumCircuit(3, 3)
    telCirc.draw(output='mpl', filename='task3_init_scheme.png')
    # Шаг 1: Применение к q_0 (его необходимо телепортировать) гейта X
    telCirc.x(0)
    telCirc.barrier()
    telCirc.draw(output='mpl', filename='task3_step1.png')
    # Шаг 2: Создание запутанности между q_1 и q_2, с использованием гейта Адамара к q_1 и гейта CX к q_1 и q_2
    telCirc.h(1)
    telCirc.cx(1, 2)
    telCirc.draw(output='mpl', filename='task3_step2.png')
    # Шаг 3: Создание запутанности между q_0 и q_1
    telCirc.cx(0, 1)
    telCirc.h(0)
    telCirc.barrier()
    telCirc.measure([0, 1], [0, 1])
    telCirc.draw(output='mpl', filename='task3_step3.png')
    # Шаг 4: Применение гейта CX к q_1 и q_2 и гейта CZ к q_0 и q_2
    telCirc.barrier()
    telCirc.cx(1, 2)
    telCirc.cz(0, 2)
    telCirc.draw(output='mpl', filename='task3_step4.png')
    # Вычисление результата и сохранение гистограммы
    sim = Aer.get_backend('qasm_simulator')
    telCirc.measure(2, 2)
    result = execute(telCirc, backend=sim, shots=1000).result()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.savefig('histogram_task3.png')
