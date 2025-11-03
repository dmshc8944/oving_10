from emne import Emne
from studieplan import Studieplan

# Глобальные списки для хранения данных
emner = []  # Список всех предметов
studieplaner = []  # Список всех учебных планов
filnavn = "studieplaner.txt"  # Имя файла для сохранения/загрузки

# Создаем начальный учебный план по умолчанию
standard_plan = Studieplan(1, "Dataingeniør")
studieplaner.append(standard_plan)