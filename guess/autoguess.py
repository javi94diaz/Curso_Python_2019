import random
import math
from time import sleep

results_list = list()

for i in range(0,10):
    max_limit = 100
    min_limit = 1

    target = random.randint(min_limit, max_limit)
    print(target)

    print("Guess a number between " + str(min_limit) + " and " + str(max_limit) + ": ")
    count = 0

    guess = math.ceil((max_limit - min_limit)/2 + min_limit)
    print("The initial guess is " + str(guess))

    while guess!=target:
        
        if guess > target:
            max_limit = guess
            guess = math.floor((max_limit - min_limit)/2 + min_limit)

        if guess < target:
            min_limit = guess
            guess = math.ceil((max_limit - min_limit)/2 + min_limit)
        
        print("The new guess is " + str(guess))
        count+=1
        sleep(0.01)

    print("Correct! Solved in " + str(count+1), end='')
    if count == 0:
        print(" try")
    else:
        print(" tries")
    
    results_list.append(count+1)
    print(results_list)

print("Average of tries is: " + str(sum(results_list)/len(results_list)))