import turtle
from turtle import *
import time
import random
from random import randint

wn = turtle.Screen()
wn.title("dodge! by Isaac and Adam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0
level = 1


# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(0, 0)


red = turtle.Turtle()
red.speed(0)
red.shape("square")
red.color("red")
red.shapesize(stretch_wid=2, stretch_len=2)
red.penup()
red.goto(-290, 270)
red.dx = 0.02
red.dy = -0.02


red2 = turtle.Turtle()
red2.speed(0)
red2.shape("square")
red2.color("red")
red2.shapesize(stretch_wid=2, stretch_len=2)
red2.penup()
red2.goto(-290, 270)
red2.dx = 0.1
red2.dy = -0.2

gren = turtle.Turtle()
gren.speed(0)
gren.shape("square")
gren.color("green")
gren.shapesize(stretch_wid=2, stretch_len=2)
gren.penup()
gren.goto(-290, 270)
gren.dx = 0.2
gren.dy = -0.1


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "deaths: 0  points: 0  level: 1", align="center", font=("Courier", 24, "normal")
)


# functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    red.dx += 0.001


def paddle_a_right():
    X = paddle_a.xcor()
    X += 20
    paddle_a.setx(X)


def paddle_a_left():
    X = paddle_a.xcor()
    X -= 20
    paddle_a.setx(X)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_a_right, "d")

wn.listen()
wn.onkeypress(paddle_a_left, "a")


while True:
    wn.update()

    red.setx(red.xcor() + red.dx)
    red.sety(red.ycor() + red.dy)

    red2.setx(red2.xcor() + red2.dx)
    red2.sety(red2.ycor() + red2.dy)

    red.setx(red.xcor() + red.dx)
    red.sety(red.ycor() + red.dy)

    red2.setx(red2.xcor() + red2.dx)
    red2.sety(red2.ycor() + red2.dy)

    gren.setx(gren.xcor() + red.dx)
    gren.sety(gren.ycor() + red.dy)

    gren.setx(gren.xcor() + gren.dx)
    gren.sety(gren.ycor() + gren.dy)

    if red.ycor() > 290:
        red.sety(290)
        red.dy *= -1

    if red.ycor() < -290:
        red.sety(-290)
        red.dy *= -1

    if red.xcor() > 390:
        red.setx(390)
        red.dx *= -1

    if red.xcor() < -390:
        red.setx(-390)
        red.dx *= -1

    if red2.ycor() > 290:
        red2.sety(290)
        red2.dy *= -1

    if red2.ycor() < -290:
        red2.sety(-290)
        red2.dy *= -1

    if red2.xcor() > 390:
        red2.setx(390)
        red2.dx *= -1

    if red2.xcor() < -390:
        red2.setx(-390)
        red2.dx *= -1

    if gren.ycor() > 290:
        gren.sety(290)
        gren.dy *= -1

    if gren.ycor() < -290:
        gren.sety(-290)
        gren.dy *= -1

    if gren.xcor() > 390:
        gren.setx(390)
        gren.dx *= -1

    if gren.xcor() < -390:
        gren.setx(-390)
        gren.dx *= -1

    # if paddle_a.xcor()

    if paddle_a.xcor() == (0):
        paddle_a.color("blue")

    if (
        red.xcor() - 25 <= paddle_a.xcor()
        and paddle_a.xcor() <= red.xcor() + 25
        and red.ycor() - 25 <= paddle_a.ycor()
        and paddle_a.ycor() <= red.ycor() + 25
    ):
        paddle_a.goto(randint(-390, 0), randint(0, 390))
        score_a += 1
        score_b -= 1
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if (
        red2.xcor() - 25 <= paddle_a.xcor()
        and paddle_a.xcor() <= red2.xcor() + 25
        and red2.ycor() - 25 <= paddle_a.ycor()
        and paddle_a.ycor() <= red2.ycor() + 25
    ):
        paddle_a.goto(randint(-390, 0), randint(0, 390))
        score_a += 1
        score_b -= 1
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}  level: {level} ",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if paddle_a.xcor() > 390:
        paddle_a.goto(380, paddle_a.ycor())

    if paddle_a.xcor() < -390:
        paddle_a.goto(-390, paddle_a.ycor())

    if paddle_a.ycor() > 290:
        paddle_a.goto(paddle_a.xcor(), 290)

    if paddle_a.ycor() < -290:
        paddle_a.goto(paddle_a.xcor(), -280)

    if (
        gren.xcor() - 25 <= paddle_a.xcor()
        and paddle_a.xcor() <= gren.xcor() + 25
        and gren.ycor() - 25 <= paddle_a.ycor()
        and paddle_a.ycor() <= gren.ycor() + 25
    ):
        paddle_a.goto(randint(-390, 0), randint(0, 390))
        score_b += 1
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}  level: {level}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if score_b == 1:
        level += 1
        red.dx += 0.2
        red.dy += 0.2
        red2.dx += 0.2
        red2.dx += 0.2
        score_b += 2
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}  level: {level}",
            align="center",
            font=("Courier", 24, "normal"),
        )
