from datetime import datetime, timedelta

def get_future_date(days):
    """
    Функция возвращает дату, которая наступит через указанное количество дней.
    
    :param days: int, количество дней от текущей даты
    :return: str, дата в формате YYYY-MM-DD
    """
    # Получаем текущую дату
    current_date = datetime.now()
    
    # Вычисляем дату через указанное количество дней
    future_date = current_date + timedelta(days=days)
    
    # Форматируем дату в строку
    formatted_date = future_date.strftime('%Y-%m-%d')
    
    return formatted_date


# Пример использования
days_to_add = 10
future_date = get_future_date(days_to_add)
print(f"Дата через {days_to_add} дней: {future_date}")