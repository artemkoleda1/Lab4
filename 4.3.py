def analyze_packets():
    while True:
        packets = input("Введите последовательность пакетов (0 и 1): ")

        # Проверка корректности ввода
        if len(packets) < 5:
            print("Длина строки должна быть не меньше 5 символов!")
            continue

        if not all(char in '01' for char in packets):
            print("Неверный ввод. Используйте только символы '0' и '1'!")
            continue

        break