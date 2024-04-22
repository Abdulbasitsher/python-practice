from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def right_angled():
    tim.right(30)
    
    

def left_angled():
    tim.right(30)
    

def up_angled():
    
    tim.right(30)

def below_angled():
    tim.right(30)

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_upward():
    tim.left(90)
    tim.forward(10
                )
def move_downward():
    tim.right(90)
    tim.forward(10)
    
tim.shape("turtle")
screen.listen()    
screen.onkey(right_angled,key='d')
screen.onkey(left_angled,key='a')
screen.onkey(up_angled,key='w')
screen.onkey(below_angled,key='s')
screen.onkey(move_forward,'Up')
screen.onkey(move_downward,'Down')
screen.onkey(move_backward,'Left')
screen.onkey(move_forward,'Right')


screen.exitonclick()
