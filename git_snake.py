
# https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900
# https://github.com/RichardHogg/Snake-game-for-beginners/blob/master/snake_game.py
#simple snake game in python 3

import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game by Richard")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  #turns off the screen updates

#Snake head
head = turtle.Turtle()  
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()  
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(0,100)
food.direction = "stop"

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("courier", 24, "normal"))

#functions
def go_up():
    if head.direction !="down":
        head.direction = "up"

def go_down():
    if head.direction !="up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Main game Loop
while True:
    wn.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segments list
        segments.clear()
       
        #reset score
        score = 0

        #reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



    #check for a collision with the food
    if head.distance(food) < 20:
        #move food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001

        #increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #move the end segments first in reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)



    move()

    #check for head collison with the body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()

            #reset score
            score = 0

            #reset the delay
            delay = 0.1

            #update the score
            pen.clear()
            pen.write("Score: {} High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

