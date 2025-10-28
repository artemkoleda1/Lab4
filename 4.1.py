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