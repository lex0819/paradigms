numbers = [3, 5, 4, 1, 2]

# Императивный код здесь
def sort_list_imperative(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

print(f'Result of sort_list_imperative is {sort_list_imperative(numbers)}')


# Декларативный код здесь
def sort_list_declarative(numbers):
    sorted(numbers, reverse=True)
    return numbers

print(f'Result of sort_list_declarative is {sort_list_declarative(numbers)}')
