# Calculating Length
# len() - Return the length (the number of items) of an object.
# The argument may be a sequence (such as a string, bytes, tuple, list, or range)
# or a collection (such as a dictionary, set, or frozen set).


# Strings
first_name = 'Dmitry'
print(len(first_name))

last_name = 'Mashkalo'
print(len(last_name))

# Strings have a special property __len__.
# And so because it has the length property, we can use the len built-in function.
first_name.__len__()


# Lists
ages = [1, 9, 12, 23, 32, 11, 0]

print(len(ages))

for i in range(0, len(ages)):
    print(ages[i])

# len() function is how many items in the list
print(len(['bob', 'mary', 'roza']))


# Dictionary
candyCollection = {'bob': 10, 'mary': 7, 'roza': 3}

# len() function is how many items in the dictionary.
print(len(candyCollection)) # Three because there's three items in our dictionary.