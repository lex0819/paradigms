# Импортируем функции из модуля functools
from functools import reduce

# Список студентов
students = [
    {"name": "Alice", "age": 22, "score": 95},
    {"name": "Bob", "age": 21, "score": 88},
    {"name": "Charlie", "age": 23, "score": 92},
    {"name": "David", "age": 22, "score": 78},
]

# Используем reduce для суммирования баллов по всем студентам
total_score = reduce(lambda x, y: x + y["score"], students, 0)

print("\nОбщий суммарный балл всех студентов:", total_score)


# Пример 1: Обработка данных с использованием функционального программирования

# Функция для фильтрации студентов младше 22 лет
def filter_young_students(student):
    return student["age"] < 22


# Функция для вычисления среднего балла студентов
def calculate_average_score(students):
    total_score = reduce(lambda x, y: x + y, [student["score"] for student in students], 0)
    return total_score / len(students)


# Получить список студентов моложе 22-х лет
young_students = list(filter(filter_young_students, students))

# Вычислить средний балл по всем студентам
average_score = calculate_average_score(students)

print("\nПример 1: Обработка данных с использованием функционального программирования")
print("\nсписок студентов моложе 22-х лет", young_students)
print("\nсредний балл по всем студентам", average_score)
