import turtle
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
DOWWN=2
RIGHT=3

def up():
    global direction
    direction=UP
    print("you preesed the up key")
def down():
    global direction
    direction=DOWN
    print("you preesed the down key")

def left():
          global direction
          direction=LEFT
          print("you preesed the left key")
def right():
          global direction
          direction=RIGHT
          print("you preesed the right key")
          
turtle.mainloop()

