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

    # Анализ данных
    total_packets = len(packets)
    lost_packets = packets.count('0')

    # Находим самую длинную последовательность нулей
    max_loss_streak = 0
    current_streak = 0

    for packet in packets:
        if packet == '0':
            current_streak += 1
            max_loss_streak = max(max_loss_streak, current_streak)
        else:
            current_streak = 0

    # Вычисляем процент потерь
    loss_percentage = (lost_packets / total_packets) * 100

    # Определяем качество связи
    if loss_percentage <= 1:
        quality = "Отличное качество"
    elif loss_percentage <= 5:
        quality = "Хорошее качество"
    elif loss_percentage <= 10:
        quality = "Удовлетворительное качество"
    elif loss_percentage <= 20:
        quality = "Плохое качество"
    else:
        quality = "Критическое состояние сети"

    # Вывод результатов
    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_loss_streak}")
    print(f"Процент потерь: {loss_percentage:.1f}%")
    print(f"Качество связи: {quality}")



analyze_packets()