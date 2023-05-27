# Statistics Module
import statistics

# Given [2, 2, 3]. We have two, two and three standing for how many cookies each person has.
# Mean (Average) = 7/3 = 2.333
# Median (Midpoint) = 2
# Mode (Most frequent value) = 2

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(agesData)) # Mean (average) of our data
print(statistics.median(agesData)) # Median (midpoint) of our data
print(statistics.mode(agesData)) # Mode (most frequent value) of our data


