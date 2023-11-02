def great(name):
    print("Hi!")
    print(name)
    print("How are you?")


def rate_movie(score):
    if score > 8:
        return "Film is best"
    elif score > 6:
        return "Film is good"
    else:
        return "Film is not bad or bad"


print(rate_movie(9))


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_to_n(100))


def say_hello():  # Это подпрограмма
    print("Привет!")


def show_message(message):  # Это процедура
    print(message)


show_message("This is message")


def add(a, b):  # Это функция
    return a + b


result = add(3, 4)
print(result)


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} говорит Гав!")


dog = Dog("Бобик")
dog.bark()
