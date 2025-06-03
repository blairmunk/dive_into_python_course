#!/usr/bin/env python3
import argparse

def process_data(number, text, repeat=1, verbose=False):
    """
    Обрабатывает входные данные согласно заданной логике.
    
    Args:
        number (int): Целое число для обработки
        text (str): Строка для обработки
        repeat (int): Количество повторений строки
        verbose (bool): Флаг для вывода дополнительной информации
    
    Returns:
        str: Результат обработки
    """
    if verbose:
        print(f"Выполняется обработка данных...")
        print(f"Число {number} будет использовано для операций.")
    
    # Пример использования числа - модификация строки
    modified_text = text.upper() if number % 2 == 0 else text.lower()
    
    if verbose:
        print(f"Строка преобразована в: '{modified_text}'")
        print(f"Повторяем строку {repeat} раз(а)...")
    
    # Повторяем строку указанное количество раз
    result = modified_text * repeat
    
    return result

def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(
        description='Скрипт для обработки числа и строки с дополнительными опциями'
    )
    
    # Добавляем обязательные позиционные аргументы
    parser.add_argument('number', type=int, help='Целое число')
    parser.add_argument('text', type=str, help='Строка для обработки')
    
    # Добавляем дополнительные опции
    parser.add_argument('--verbose', action='store_true', 
                        help='Выводить дополнительную информацию о процессе')
    parser.add_argument('--repeat', type=int, default=1,
                        help='Количество повторений строки в выводе (по умолчанию: 1)')
    
    # Дополнительная опция форматирования вывода
    parser.add_argument('--format', choices=['plain', 'json', 'csv'], default='plain',
                        help='Формат вывода результата (по умолчанию: plain)')
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Получаем значения аргументов
    number = args.number
    text = args.text
    verbose = args.verbose
    repeat = args.repeat
    output_format = args.format
    
    # Выводим дополнительную информацию, если установлен флаг verbose
    if verbose:
        print(f"Информация о входных параметрах:")
        print(f"Число: {number}")
        print(f"Строка: '{text}'")
        print(f"Количество повторений: {repeat}")
        print(f"Формат вывода: {output_format}")
    
    # Обрабатываем данные
    result = process_data(number, text, repeat, verbose)
    
    # Выводим результат в выбранном формате
    if output_format == 'plain':
        print(f"Результат обработки:")
        print(result)
    elif output_format == 'json':
        import json
        output = {
            'number': number,
            'text': text,
            'repeat': repeat,
            'result': result
        }
        print(json.dumps(output, indent=2))
    elif output_format == 'csv':
        print(f"number,text,repeat,result")
        print(f"{number},\"{text}\",{repeat},\"{result}\"")

if __name__ == "__main__":
    main()

