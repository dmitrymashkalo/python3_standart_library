# Itertools Module
import itertools


# Infinite Counting
for i in itertools.count(1, 1): # (start, step)
    print(i)
    if i == 100:
        break


# Infinite Cycling
x = 0
for i in itertools.cycle('Some text'):
    print(i)
    x += 1
    if x == 50:
        break


# Infinite Repeating
for i in itertools.repeat(True):
    print(i)
    x += 1
    if x == 100:
        break


# Permutations - A way, especially one of several possible variations,
# in which a set or number of things can be ordered or arranged.
# Order matters - some copies with same inputs but in different order.
election = {
    1: 'Bard',
    2: 'Karen',
    3: 'Erin'
}

for i in itertools.permutations(election):
    print(i)

for i in itertools.permutations(election.values()):
    print(i)


# Combinations - are kind of like permutations in that they list a set of items,
# but for combinations, no set has the exact same elements as another.
# Order does not matter - no copies with same inputs.
colors = ['Red', 'Blue', 'Purple', 'Orange', 'Yellow', 'Pink']

for i in itertools.combinations(colors, 2):
    print(i)
