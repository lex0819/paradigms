from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z,ancestor, parent')

# parent's relationships
+ parent('Maria', 'John')
+ parent('John', 'Sergey')

ancestor(X,Y) <= parent(X,Y)
ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)

# Who is ancestor of Sergey?
print("Who is ancestor of Sergey?", ancestor(X, 'Sergey'))
