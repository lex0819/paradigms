"""
Чистые функции (Pure Functions):
Они не изменяют состояние программы или внешние переменные.
"""
def add(a, b):
    return a + b

result = add(3, 4)  # В результате нет побочных эффектов
print("result", result)


"""
Неизменяемость (Immutable Data): 
после создания объекта его нельзя изменить. 
Вместо этого создается новый объект с измененным состоянием.
"""
# Создание нового списка с измененным элементом
original_list = [1, 2, 3]


new_list = [x * 2 for x in original_list]  # Не изменяет оригинальный список
print("original_list", original_list)
print("new_list", new_list)


"""
Функции высших порядков (Higher-Order Functions): 
Это функции, которые принимают другие функции в качестве аргументов 
или возвращают их в качестве результатов.
"""
def apply(func, x):
    return func(x)

def square(x):
    return x ** 2

result = apply(square, 5)  # Применение функции square через функцию apply
print("apply(square, 5)", result)


"""
Рекурсия: Функциональное программирование активно использует рекурсию для решения задач.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)  # Вычисление факториала через рекурсию
print("factorial", result)


"""
Функции первого класса (First-Class Functions): 
Функции рассматриваются как обычные значения и могут быть присвоены переменным, 
переданы как аргументы и возвращены из других функций.
"""
# Функция, которая принимает функцию как аргумент
def apply(func, x):
    return func(x)

# Обычная функция, которая возводит число в квадрат
def square(x):
    return x ** 2

# Функция, которая возводит число в куб
def cube(x):
    return x ** 3

# Присвоение функций переменным
my_function1 = square
my_function2 = cube

# Использование функций как аргументов
result1 = apply(my_function1, 5)  # Вызов apply с функцией square
result2 = apply(my_function2, 3)  # Вызов apply с функцией cube

print("square(x)", result1)  # Вывод: 25 (5 в квадрате)
print("cube(x)", result2)  # Вывод: 27 (3 в кубе)


"""
Лямбда-функции: Лямбда-функции (анонимные функции) позволяют создавать короткие и одноразовые функции без явного определения имени функции.
"""
def add(x, y):
    return x + y

add = lambda x, y: x + y  # Лямбда-функция для сложения двух чисел
result = add(3, 4)  # Вызов лямбда-функции