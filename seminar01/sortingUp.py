# дан список чисел, надо отсортировать его по возрастанию

numbers = [3, 5, 4, 1, 2]

# императивный стиль
def sort_up_imperative(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(i+1, length):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(f'Result of sort_up_imperative is {sort_up_imperative(numbers)}')

# декларативный стиль
def sort_up_declarative(numbers):
    numbers.sort()
    return numbers

print(f'Result of sort_up_declarative is {sort_up_declarative(numbers)}')