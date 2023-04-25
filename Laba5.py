#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно
#и итерационно. Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить
#в табличной и графической форме.

#F(x<2) = 100; F(n) = -F(n-1) + F(n//5)

import time
import matplotlib.pyplot as plt

def recursive_f(n):
    if n < 2:
        return 100
    else:
        return (-1) * recursive_f(n - 1) + recursive_f(n // 5)

def iterative_f(n):
    if n < 2:
        return 100
    else:
        a = 100
        for i in range(2, n + 1):
            if i < 5:
                b = (-1) * a + 100
            else:
                b = (-1) * a + iterative_f(i // 5)
            a = b
        return b

try:
    print("Введите натуральное число n, являющееся входным для функции  F(x<2) = 100; F(n) = -F(n-1) + F(n//5): ")
    n = int(input())
    while n < 1:
        n = int(input("\nВы ввели не натуральное число, функция определенна лишь в области натуральных чисел. Введите натуральное число:\n"))

    print("Введите шаг изменения числа s: ")
    s = int(input())
    while s < 1:
        s = int(input("\nВы ввели не натуральное число, шаг должен быть натуральным числом. Введите натуральное число:\n"))

    if n > 100000:
        print("\nРабота программы может занять существенное время...")

    start = time.time()         # счетчик времени и результат работы итерационного подхода
    result = iterative_f(n)
    end = time.time()
    print("\nРезультат работы итерационного подхода:", result, "\nВремя работы:", end - start)

    k = 1
    if n > 40:
        k = int(input(
            "\nЧисло n > 40, вы хотите получить результат работы рекурсивного подхода? Это может занять существенное время. (Да: 1 / Нет: 0):\n"))
    while k != 0 and k != 1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу:\n"))

    if k == 1:
        if 40 < n < 100000:
            print("\nРабота рекурсивного подхода может занять существенное время, ожидайте...")

        start = time.time()         # счетчик времени и результат работы рекурсивного подхода
        result = recursive_f(n)
        end = time.time()
        print("\nРезультат работы рекурсивного подхода:", result, "\nВремя работы:", end - start)

    if n > 40 and k != 0:
        k = int(input("\nЧисло n > 40, вы хотите сделать сравнительную таблицу? Это может занять существенное время. (Да: 1 / Нет: 0):\n"))
    while k != 0 and k != 1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу:\n"))

    if k == 1:
        print("\nПрограмма формирует сравнительную таблицу и графики времени вычисления рекурсивным и итерационным подходом для n чисел, ожидайте...\n")

        recursive_times = []                # создание списков для дальнейшего построения таблицы
        recursive_values = []
        iterative_times = []
        iterative_values = []
        n_values = list(range(1, n + 1, s))

        for n in n_values:                  # заполнение списков данными
            start = time.time()
            recursive_values.append(recursive_f(n))
            end = time.time()
            recursive_times.append(end - start)

            start = time.time()
            iterative_values.append(iterative_f(n))
            end = time.time()
            iterative_times.append(end - start)

        table_data = []             # создание и заполнение последующей таблицы
        for i, n in enumerate(n_values):
            table_data.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])

        print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации'))
        print('-' * 110)
        for data in table_data:
            print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(data[0], data[1], data[2], data[3], data[4]))

        plt.plot(n_values, recursive_times, label='Рекурсия')
        plt.plot(n_values, iterative_times, label='Итерация')
        plt.xlabel('n')
        plt.ylabel('Время (с)')
        plt.title('Сравнение рекурсивного и итерационного подхода')
        plt.legend()
        plt.show()

    print("\nРабота программы завершена.\n")

except ValueError:
    print("\nВы ввели число, не следуя условиям. Перезапустите программу и введите число, следуя инструкциям.")

except RecursionError:
    print("\nВы превысили относительную максимальную глубину рекурсии. Перезапустите программу и введите меньшее число, если хотите получать результат работы рекурсивного подхода и сравнительную таблицу.")