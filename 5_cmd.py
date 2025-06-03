#!/usr/bin/env python3
import os
import sys
import logging
from collections import namedtuple
import argparse

# Определяем namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir', 'full_path'])

def setup_logging(log_file="directory_info.log"):
    """Настройка логирования"""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # Добавим вывод логов также в консоль
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def scan_directory(directory_path, recursive=False):
    """
    Сканирует указанную директорию и возвращает список объектов FileInfo
    
    Args:
        directory_path (str): Путь к директории для сканирования
        recursive (bool): Флаг, указывающий на необходимость рекурсивного сканирования
        
    Returns:
        list: Список объектов FileInfo
    """
    logging.info(f"Начало сканирования директории: {directory_path}")
    
    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        return []
    
    file_info_list = []
    
    try:
        # Получаем имя родительской директории
        parent_dir = os.path.basename(directory_path)
        
        # Сканируем содержимое директории
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            is_dir = os.path.isdir(item_path)
            
            if is_dir:
                # Если это директория, расширение пустое
                name = item
                extension = ""
                logging.info(f"Найдена директория: {item_path}")
                
                # Если включен рекурсивный режим, сканируем поддиректорию
                if recursive:
                    logging.info(f"Рекурсивное сканирование директории: {item_path}")
                    subdir_info = scan_directory(item_path, recursive)
                    file_info_list.extend(subdir_info)
            else:
                # Если это файл, разделяем имя и расширение
                name, ext = os.path.splitext(item)
                # Убираем точку из расширения
                extension = ext[1:] if ext else ""
                logging.info(f"Найден файл: {item_path} (имя: {name}, расширение: {extension})")
            
            # Создаем объект FileInfo и добавляем его в список
            file_info = FileInfo(
                name=name,
                extension=extension,
                is_directory=is_dir,
                parent_dir=parent_dir,
                full_path=item_path
            )
            file_info_list.append(file_info)
            
            # Логируем информацию о файле/директории
            logging.info(f"Добавлен объект: {file_info}")
        
        logging.info(f"Завершено сканирование директории: {directory_path}")
        logging.info(f"Всего обнаружено объектов в {directory_path}: {len(file_info_list)}")
        
        return file_info_list
    
    except Exception as e:
        logging.error(f"Ошибка при сканировании директории {directory_path}: {e}")
        return []

def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(
        description="Скрипт для сканирования директорий и сохранения информации о файлах"
    )
    parser.add_argument("directory", help="Путь до директории для сканирования")
    parser.add_argument("--log", default="directory_info.log", 
                        help="Путь к файлу логирования (по умолчанию: directory_info.log)")
    parser.add_argument("--recursive", "-r", action="store_true",
                        help="Рекурсивное сканирование поддиректорий")
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Настраиваем логирование
    setup_logging(args.log)
    
    # Сканируем директорию
    files_info = scan_directory(args.directory, args.recursive)
    
    # Выводим результаты
    print(f"\nРезультаты сканирования директории: {args.directory}")
    print(f"Режим сканирования: {'рекурсивный' if args.recursive else 'плоский'}")
    print(f"Всего объектов: {len(files_info)}")
    print(f"Информация сохранена в файл: {args.log}")
    
    # Дополнительно выводим статистику
    dir_count = sum(1 for info in files_info if info.is_directory)
    file_count = len(files_info) - dir_count
    
    print(f"Директорий: {dir_count}")
    print(f"Файлов: {file_count}")
    
    # Выводим список уникальных расширений файлов
    extensions = {}
    for info in files_info:
        if info.extension:
            extensions[info.extension] = extensions.get(info.extension, 0) + 1
    
    if extensions:
        print("\nНайдены расширения файлов:")
        for ext, count in sorted(extensions.items(), key=lambda x: x[1], reverse=True):
            print(f" - {ext}: {count} файлов")

if __name__ == "__main__":
    main()
