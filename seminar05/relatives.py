from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, grandparent')

# parent's relationships
+ parent('Maria', 'John')
+ parent('John', 'Sergey')

# grandparent's relationships
grandparent(X, Y) <= parent(X, Z) & parent(Z, Y)

# Who is grandfather or grandmother for Sergey?
print("Who is grandfather or grandmother for Sergey?", grandparent(X, 'Sergey'))
