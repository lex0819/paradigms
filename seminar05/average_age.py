from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z,age, average_age, sum_age, count_people')

+ age('Maria', 30)
+ age('Poul', 40)
+ age('Alex', 20)

average_age(X) <= (sum_age(Y), count_people(Z)) & (Y==sum_(X['Y']) for X in age(X['X'], X['Y'])) & (Z==len_(age))


# What is average age of the people?
print("What is average age of the people?", average_age(X))