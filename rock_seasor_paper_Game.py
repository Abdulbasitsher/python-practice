import random

my_choice = int(input("choose between from zero to two "))

computer_choice = random.randint(0,2)

print(my_choice, computer_choice)
print("rock = 0 paper = 1 seasor = 2")
if my_choice == 0 and computer_choice == 1:
    print("You Won Beacuse Rock beat paper")
elif my_choice == computer_choice:
    print("Its a draw")
elif my_choice == 1 and computer_choice == 2:
    print("you lost beacuse seasor beat paper")
elif my_choice == 0 and computer_choice == 2:
    print("you Won beacuse rock beat seasor")
elif my_choice == 1 and computer_choice == 0:
    print("You loose")
elif my_choice == 2 and computer_choice == 1:
    print("you won")
elif my_choice == 2 and computer_choice == 0:
    print("you loose") 
else:
    print("You Enter Invalid entry")