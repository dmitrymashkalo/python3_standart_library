# Least to Greatest
pointsInAGame = [0, -2, 14, -6, 12, 43]
sortedPoints = sorted(pointsInAGame)
print(sortedPoints)


# Alphabetically
children = ['Sue', 'Jerry', 'Linda']
print(sorted(children))

# Case important!!! Example:
print(sorted(['Sue', 'jerry', 'linda']))


# Key Parameters
print(sorted('My favorite child name is Linda'.split(), key=str.upper)) # by adding this optional parameter, we were able to make this function case insensitive.
print(sorted(pointsInAGame, reverse=True)) # by adding this optional parameter, we were able to reverse this list.


# Dictionary
leaderBoard = {
    231: 'CKL',
    123: 'ABC',
    432: 'JKC'
}
print(sorted(leaderBoard, reverse=True)) # sort by keys
print(leaderBoard.get(432))


# Example how to sort list of tuples with key=labmda
students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
# sort by the name 
print(sorted(students, key=lambda student:student[0]))
# sort by score
print(sorted(students, key=lambda student:student[1]))
# sort by age
print(sorted(students, key=lambda student:student[2]))