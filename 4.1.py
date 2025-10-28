import random
import time


def multiplication_trainer():
    n = int(input("Введите количество примеров: "))
    correct_answers = 0
    total_time = 0

    for i in range(1, n + 1):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        correct_result = a * b

        while True:
            start_time = time.time()
            try:
                user_answer = int(input(f"Вопрос {i}/{n}\n{a} x {b} = "))
                end_time = time.time()
                time_spent = end_time - start_time
                total_time += time_spent

                if user_answer == correct_result:
                    print(f"Верно! (Время: {time_spent:.1f} сек)")
                    correct_answers += 1
                else:
                    print(f"Неверно! Правильно: {correct_result} (Время: {time_spent:.1f} сек)")
                break

            except ValueError:
                end_time = time.time()
                time_spent = end_time - start_time
                total_time += time_spent
                print("Пожалуйста, введите целое число!")

    # Вывод статистики
    print("\n" + "=" * 30)
    print("СТАТИСТИКА:")
    print("=" * 30)
    print(f"Общее время: {total_time:.1f} секунд")
    print(f"Среднее время на вопрос: {total_time / n:.1f} сек")
    print(f"Правильных ответов: {correct_answers}/{n}")
    print(f"Процент правильных: {correct_answers / n * 100:.1f}%")


# Запуск программы
multiplication_trainer()