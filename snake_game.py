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



