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