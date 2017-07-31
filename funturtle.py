##import turtle
##turtle.shape('turtle')
##square=turtle.clone()
##square.shape('square')
###square.goto(100,100)
##square.goto(100,0)
##square.goto(100,100)
##square.goto(0,100)
##square.goto(0,0)
##triangle=turtle.clone()
##triangle.shape("triangle")
##triangle.goto(100,0)
##triangle.stamp()
##triangle.goto(50,50)
##triangle.goto(0,0)
##import turtle
##turtle.shape("turtle")
##square=turtle.clone()
##square.shape("square")
##square.goto(100,0)
##square.stamp()
##square.goto(100,100)
##square.goto(0,100)
##square.goto(0,0)




UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"

UP=0
LEFT=1
DOWN=2
RIGHT=3
direction=UP
def up():
    global direction
    direction=UP
    print("you pressed the up key")
    
def down():
    global direction
    direction=DOWN
    print("you pressed the down key")

def left():
          global direction
          direction=LEFT
          print("you pressed the left key")
def right():
          global direction
          direction=RIGHT
          print("you pressed the right key")
          

