import time

a = time.time()
time.sleep(5)
b = time.time()
print(a)
print(type(a))
print(b)
print(type(b))
print(b - a)
print(type(b - a))
print(int(b - a))
print(type(int(b - a)))

