from random import randint
print("Welcome to Nmuber Guessing Game")
number = randint(1,100)
j = int(input("how much guesses do you want"))
for i in range(1, j):
    guess = int(input("What do you think that the number will be between 1 and 100"))
    print(number)
    if guess == number:
        result = print("You win")
        break
    elif guess == number-1:
        print("your guess is low")
    elif guess == number-2:
        print("your guess is Too low")
    elif guess == number+1:
        print("your guess is high") 
    elif guess == number+2:
        print("your guess is Too high")
    elif guess > number+2:
        print("your guess is too much high")
    elif guess < number-2:
        print("your guess is too much low")
    
    else:
        print("you enterd invalid entry")