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
head.shape("square")
head.color("black")
head.penup
head.goto(0,0)
head.direction="stop"

#snake food
food = turtle.Turtle()
food.goto(0,100)