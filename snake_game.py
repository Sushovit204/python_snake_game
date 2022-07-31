import turtle

#screen setup
wnd=turtle.Screen()
wnd.title("Snake Game by @Sushovit204")
wnd.bgcolor("blue")
wnd.setup(width=500, height=500)
wnd.tracer(0)

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

# Pen
pen=turtle.Turtle
pen.speed(0)
pen.shape("oval")
pen.color("brown")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0  High Score: 0", align="centre", font=("Courier", 22, "normal"))

#Functions
def _go_up():
    if head.direction !="down":
        head.direction = "up"

def _go_down():
    if head.direction != "up":
        head.direction = "down"

def _go_left():
    if head.direction != "right":
        head.direction = "left"

def _go_right():
    if head.direction != "left":
        head.direction = "right"

def _move_():
    if head.direction() == "up":
        y = head.ycor()
        head.sety(y +20)

    if head.direction() =="down":
        y = head.ycor()
        head.setx(y - 20)

    if head.direction() =="left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction() =="right":
        x = head.xcor
        head.setx(x + 20)

 #Key-bindings for the movements of snake   
     