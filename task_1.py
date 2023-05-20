from qiskit import QuantumCircuit, execute, Aer


def task1():
    # Инициализация схемы (2 кубита, 1 бит)
    qc = QuantumCircuit(2, 1)
    # Применение оператора Адамара к первому кубиту (индекс 0)
    qc.h(0)
    # Применение NOT к двум кубитам
    qc.cx(0, 1)
    # Применение U-оператора
    qc.unitary([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], [0, 1], label='U')
    # Применение NOT к двум кубитам
    qc.cx(0, 1)
    # Применение оператора Адамара к первому кубиту (индекс 0)
    qc.h(0)
    # Измерение первого кубита и запись результата в бит
    qc.measure(0, 0)
    # Запуск схемы
    simulator = Aer.get_backend('qasm_simulator')
    # Получение результата, запись в переменную и вывод в консоль
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    print("Task 1 result:", counts)
    # Визуализация схемы
    qc.draw(output='mpl', filename='task1.png')
