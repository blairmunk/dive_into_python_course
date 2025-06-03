from datetime import datetime

def get_current_datetime_info():
    # Получаем текущее время и дату
    now = datetime.now()
    
    # Форматируем дату и время
    formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
    
    # Получаем день недели
    day_of_week = now.strftime('%A')
    
    # Получаем номер недели в году
    week_number = now.isocalendar()[1]
    
    # Дополнительная информация
    day_of_year = now.strftime('%j')  # День года (001-366)
    
    return {
        'datetime': formatted_datetime,
        'day_of_week': day_of_week,
        'week_number': week_number,
        'day_of_year': day_of_year
    }

def main():
    # Получаем информацию о дате и времени
    datetime_info = get_current_datetime_info()
    
    # Выводим информацию
    print(f"Текущие дата и время: {datetime_info['datetime']}")
    print(f"День недели: {datetime_info['day_of_week']}")
    print(f"Номер недели в году: {datetime_info['week_number']}")
    print(f"День года: {datetime_info['day_of_year']}")

if __name__ == "__main__":
    main()