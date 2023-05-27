# Command Line Arguments
import sys


# Print Arguments
print(f'Number of arguments: {len(sys.argv)} arguments')
print(f'Arguments: {sys.argv}')


# Remove Arguments
sys.argv.remove(sys.argv[0])
print(f'Arguments: {sys.argv}')


# Sum up the Arguments
arguments = sys.argv

sum_up = 0
for arg in arguments:
    try:
        number = int(arg)
        sum_up = sum_up + number
    except Exception:
        print('Bad input!')

print(sum_up)