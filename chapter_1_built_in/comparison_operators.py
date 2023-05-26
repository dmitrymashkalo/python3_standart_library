# Python Comparison Operators:
# A comparison (also called relational) operator determines the equality or difference between values.
# The expression ultimately returns a Boolean value.

# TIPS:
# == -> is equal to
# <= -> is less than or equal to
# >= -> is greater than or equal to
# < -> is less than
# > -> is greater than

# < -> is less than
print(10 < 11) # True

# > -> is greater than
print(10 > 11) # False

# == -> is equal to
print(10 == 10) # True

kitten = 10
tiger = 75

if kitten < tiger:
    print('The kitten weighs less than the tiger')

mouse = 1

if mouse < kitten and mouse < tiger:
    print('The mouse weighs the least')

# Boolean
# False -> 0
# True -> 1
# > -> is greater than
print(False > True) # False
print(True > False) # True

# Looking for first mismatched letter
# A - Z -> 1 - 26
# > -> is greater than
print('Jennifer' > 'Jenny') # False, because 'i = 9' and 'y = 25'

# A - Z -> 1 - 26
# <= -> is less than or equal to
print('a' <= 'b') # True, because 'a = 1' and 'b = 2'