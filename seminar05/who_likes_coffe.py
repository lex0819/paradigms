from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,likes')

+ likes('Vasya', 'tea')
+ likes('Masha', 'coffe')
+ likes('Vasya', 'coffe')

# Request: Who likes coffe?
print("Who likes coffe? ",likes(X, 'coffe'))