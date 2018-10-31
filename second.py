import sys

for line in sys.stdin:
    numbers = line.split()

numbers = list(map(int, numbers))

average = sum(numbers)/len(numbers)
print(average)
