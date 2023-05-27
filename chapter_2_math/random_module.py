# Random Module
import random


# Random Numbers
print(random.random()) # Generates a random float number between 0 and 1 (exclusive)

decider = random.randrange(3) # Generates a random integer from 0 to 2 representing coin flip

if decider == 0:
    print('HEADS')
else:
    print('TAILS')

print(f'You rolled a {random.randrange(1, 7)}') # Generates a random integer from 1 to 6 (inclusive) representing a dice roll


# Random Choices
lotteryWinners = random.sample(range(100), 5) # Randomly selects 5 unique numbers from the range 0 to 99
print(lotteryWinners)

possiblePets = ['cat', 'dog', 'fish']
print(random.choice(possiblePets)) # Randomly selects and outputs one element from the list

cards = ['ace', 'king', 'queen', 'jack']
random.shuffle(cards) # Shuffles the order of elements in the list
print(cards)