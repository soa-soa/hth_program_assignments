# https://docs.python.org/3/library/turtle.html#
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# creating the game screen
screen = turtle.Screen()
screen.title("The Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(5,5)

pen = turtle.Turtle()
pen.speed(0)
pen.shape()
pen.color()
pen.penup()
pen.hideturtle()
pen.goto(0, 250)

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def goup():
    if head.direction != "up":
        head.direction = "down"

def godown():
    if head.direction != "down":
        head.direction = "up"

def move():
    if head.direction == "up":
        y = head.ycor()
    if head.direction == "down":
        y = head.ycor()
    if head.direction == "left":
        x = head.xcor()
    if head.direction == "right":
        x = head.xcor()

screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(goup, "a")
screen.onkeypress(goup, "s")
screen.onkeypress(goup, "d")

segments = []

# main gameplay
# while True:
    