import logging

# Создаем логгер
logger = logging.getLogger('my_logger')
# Устанавливаем базовый уровень логирования (будет обрабатывать все сообщения)
logger.setLevel(logging.DEBUG)

# Создаем обработчик для DEBUG и INFO сообщений
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)  # Установка уровня DEBUG для обработчика
# Фильтр, который пропускает только DEBUG и INFO сообщения
class DebugInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.INFO

debug_info_handler.addFilter(DebugInfoFilter())

# Создаем обработчик для WARNING и выше сообщений
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)  # Установка уровня WARNING для обработчика

# Создаем форматтер для настройки внешнего вида сообщений
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Применяем форматтер к обоим обработчикам
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

