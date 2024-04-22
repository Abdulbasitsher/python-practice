print("Welcomre to Calculator")

def multiplier(num1, num2):
    print(num1*num2)

def divider(num1, num2):
    print(num1*num2)
    
def adder(num1, num2):
    print(num1+num2)

def subtractor(num1,num2):
    print(num1-num2)
    

i = 'y'

while i == 'y':
    symbol = input("Which operationm do you want to be performed  '/' '+' '-' '*' ")
    
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter Second number"))
    
    if symbol == '/':
        divider(num1,num2)
    elif symbol == '+':
        adder(num1, num2)
    elif symbol == '-':
        subtractor(num1,num2)
    elif symbol == '*':
        multiplier(num1,num2)
    else:
        print("You Entered invalid Entry")
    i =  input("Press Y for continue and N   For Exit")
    
       