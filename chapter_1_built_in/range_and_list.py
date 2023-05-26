# Range - range instance that holds all nums counting by one between 0 and first input.
# List - lists numbers from the inputted tuple

numberedContestnants = range(30)
print(list(numberedContestnants))

for item in list(numberedContestnants):
    print(f'Contestnant {item} is here!')

luckyWinner = range(7, 30, 5) #(start, end, step)
print(list(luckyWinner))