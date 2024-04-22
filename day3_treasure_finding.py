print("Welcome to Treasure finding game")

choice = input("You are in City trasnport center, which sourse of transportation you to use. 'Boat' 'car' 'Airplain; ")

if(choice == 'boat'):
    choise = input("Now you came to island which direction you to go, 'left'  'right' 'middle'")
    if(choise == 'right'):
        print("You Found The TREASURE")
    else:
        print("You Lost")
else:
    print("You Lost The Treasure")