import random
letters = ['a','b','c']
numbers = ['1','2']
symbols = ['@','#','%',"&"]

for n in range(1,4)
    
    password[n] = random.choice(letters)
    password[n+1] = random.choice(numbers)
    password[n+2] = random.choice(symbols)
    if n + 2 >= 3:
        break