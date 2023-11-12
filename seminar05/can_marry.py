from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, can_marry')

# Data Base of pairs who can marry
+ can_marry('Maria', 'John')
+ can_marry('Anna', 'Peter')
+ can_marry('Daria', 'Peter')

# rule of marry
can_marry(X, Y) <= can_marry(Y, X)

# Who can marry Peter with?
print("Who can marry Peter with?", can_marry('Peter', X))