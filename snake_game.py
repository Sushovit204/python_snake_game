from shutil import move
import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

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
wnd.listen()
wnd.onkeypress(_go_up,"w")
wnd.onkeypress(_go_down, "s")
wnd.onkeypress(_go_left, "a")
wnd.onkeypress(_go_right, "d")

#Main Game loop
while True:
    wnd.update()

    #Collison check with the border
    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segment.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="centre", font=("Courier", 24, "normal"))


    #Eating the food
    if head.distance(food)<20:
        #food spwaning randomly
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Adding a segement after eating the food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score +=10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        

    #Move the end segment to the first in reverse order
    for index in range (len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[0].goto(x,y)

    move()

    #Check for the collision with the own body segements