from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z,friend, is_friend')

+ friend('Alex', 'Igor')
+ friend('Igor', 'Svetlana')
+ friend('Svetlana', 'Alex')

is_friend(X,Y) <= friend(X,Y)
is_friend(X,Y) <= friend(Y,X)

# Request: Who is Igor's fiend?
print("Who is Igor's fiend? ",is_friend(X, 'Igor'))