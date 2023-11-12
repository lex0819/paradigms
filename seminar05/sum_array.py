#
# sum all items of the array [1,2,3,4,5,6,7,8,9,10]
#
from pyDatalog import pyDatalog

pyDatalog.create_atoms('sum_array,N,F')


# Prolog logic style
+ (sum_array[0]==0)
(sum_array[N] == F) <= (N >0) & (F == N+sum_array[N-1])
print("\nProlog logic style sum result: ", sum_array[10]==N)


# Python function style
print("\nPython function style result: ", sum(range(1,11)))
