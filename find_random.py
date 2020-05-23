import numpy as np

random = np.random.randint(10)

print(random)

guess = int(input("Enter an integer number:"))
    
if (guess > random):
    print("Your number is bigger than random number")
elif (guess < random):
    print("Your number is smaller than random number")
else:
    print("congratulations you found it")    
