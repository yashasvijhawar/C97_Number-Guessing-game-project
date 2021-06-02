import random
number = random.randint(1,9)
chance = 0
print("Guess a number(between 1 and 9):")
while chance<5:
    guess = int(input("Enter your Guess"))
    if guess == number:
        print("Congratulations,You won!!")
        break 
    elif guess<number:
        print("Guess was too low,guess a number higher than that!!")

    else :
        print("Guess was too high,guess a number lower than that!!")

    chance+=1
