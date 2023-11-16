from random import randint

# Создание списка,
# его сортировка по возрастанию
# и вывод на экран
arrNum = []
for i in range(10):
    arrNum.append(randint(1, 50))
arrNum.sort()
print(arrNum)

# искомое число
print("\nPlease enter one number from the array: ")
value = int(input())


def binary_search(arr: list) -> int:
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1

    while arr[mid] != value and low <= high:
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1
    else:
        return mid


res = binary_search(arrNum)

if res == -1:
    print("No value")
else:
    print("Index of the element is ", res)
