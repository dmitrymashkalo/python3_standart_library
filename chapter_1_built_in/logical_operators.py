# Python Logical Operators: And, Or, Not.
# Logical Operator: A logical operator takes one or more boolean values and operates on them.

isRaining = False
isSunny = False

# AND
# true and true -> true
# false and true -> false
# true and false -> false
# false and false -> false

if isRaining and isSunny:
    print('We might see a rainbow')

# OR
# true and true -> true
# false and true -> true
# true and false -> true
# false and false -> false

if isRaining or isSunny:
    print('It might be rainy or it might be sunny')

# NOT
# true -> false
# false -> true

if not isRaining:
    print('It is not raining')

# is Adult example
ages = [7, 12, 18, 23, 87, 3, 43, 32]

for age in ages:
    isAdult = age > 17
    if not isAdult:
        print(f'Being {age} does not make you an adult')