
# ******************************
# Make your Code
# ******************************
import random 

numbers = []

for i in range(10):
    num = random.randint(0,100)
    numbers.append(num)

minNum = min(numbers)
minNumIndex = numbers.index(minNum)

print(minNum)
print(minNumIndex)

