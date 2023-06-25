
import random

min_limit = 1
max_limit = 100

y = random.randint(min_limit, max_limit)
#print(y)

x = int(input("Guess a number between " + str(min_limit) + " and " + str(max_limit) + ": "))
count = 0

while x != y:

    if x > y:
        print("Hint: Your number is too big")
    if x < y: 
        print("Hint: Your number is too low")

    x = int(input("Try again!: "))
    count +=1

print("Correct! You did it in " + str(count+1), end='')
if count == 0:
    print(" try")
else:
    print(" tries")

