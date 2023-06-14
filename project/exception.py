
class ParsingError(Exception):
   """Создаем класс исключения ошибки загрузки данных"""

   def __str__(self):
      return "Ошибка загрузки данных"