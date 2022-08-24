import turtle
from turtle import *
from random import randint

# leave for later
wn = turtle.Screen()
wn.title("dodge! by Isaac and Adam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.listen()

# score
score_a = 0
score_b = 0
level = 1


def create_player():
    player_shape = turtle.Turtle()
    player_shape.speed(0)
    player_shape.shape("square")
    player_shape.penup()
    player_shape.goto(0, 0)

    return player_shape


player_one = create_player()


def create_enemy():
    enemy_shape = turtle.Turtle()
    enemy_shape.speed(0)
    enemy_shape.shape("square")
    enemy_shape.color("red")
    enemy_shape.shapesize(stretch_wid=2, stretch_len=2)
    enemy_shape.penup()
    enemy_shape.goto(randint(-290, 290), randint(-390, 390))
    enemy_shape.dx = 0.02
    enemy_shape.dy = -0.02

    return enemy_shape


enemy_one = create_enemy()
enemy_two = create_enemy()


def create_ally():
    ally_shape = turtle.Turtle()
    ally_shape.speed(0)
    ally_shape.shape("square")
    ally_shape.color("green")
    ally_shape.shapesize(stretch_wid=2, stretch_len=2)
    ally_shape.penup()
    ally_shape.goto(randint(-290, 290), randint(-390, 390))
    ally_shape.dx = 0.2
    ally_shape.dy = -0.1

    return ally_shape


ally_one = create_ally()

# leave for later
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
def move_shape_up(shape):
    def helper():
        y = shape.ycor()
        y += 20
        shape.sety(y)

    return helper


def move_shape_down(shape):
    def helper():
        y = shape.ycor()
        y -= 20
        shape.sety(y)

    return helper


def move_shape_right(shape):
    def helper():
        x = shape.xcor()
        x += 20
        shape.setx(x)

    return helper


def move_shape_left(shape):
    def helper():
        x = shape.xcor()
        x -= 20
        shape.setx(x)

    return helper


def make_shape_moveable(shape, key_up, key_down, key_left, key_right):
    wn.onkeypress(move_shape_up(shape), key_up)
    wn.onkeypress(move_shape_down(shape), key_down)
    wn.onkeypress(move_shape_left(shape), key_left)
    wn.onkeypress(move_shape_right(shape), key_right)


make_shape_moveable(player_one, "w", "s", "a", "d")


while True:
    wn.update()

    enemy_one.setx(enemy_one.xcor() + enemy_one.dx)
    enemy_one.sety(enemy_one.ycor() + enemy_one.dy)

    enemy_two.setx(enemy_two.xcor() + enemy_two.dx)
    enemy_two.sety(enemy_two.ycor() + enemy_two.dy)

    ally_one.setx(ally_one.xcor() + enemy_one.dx)
    ally_one.sety(ally_one.ycor() + enemy_one.dy)

    if enemy_one.ycor() > 290:
        enemy_one.sety(290)
        enemy_one.dy *= -1

    if enemy_one.ycor() < -290:
        enemy_one.sety(-290)
        enemy_one.dy *= -1

    if enemy_one.xcor() > 390:
        enemy_one.setx(390)
        enemy_one.dx *= -1

    if enemy_one.xcor() < -390:
        enemy_one.setx(-390)
        enemy_one.dx *= -1

    if enemy_two.ycor() > 290:
        enemy_two.sety(290)
        enemy_two.dy *= -1

    if enemy_two.ycor() < -290:
        enemy_two.sety(-290)
        enemy_two.dy *= -1

    if enemy_two.xcor() > 390:
        enemy_two.setx(390)
        enemy_two.dx *= -1

    if enemy_two.xcor() < -390:
        enemy_two.setx(-390)
        enemy_two.dx *= -1

    if ally_one.ycor() > 290:
        ally_one.sety(290)
        ally_one.dy *= -1

    if ally_one.ycor() < -290:
        ally_one.sety(-290)
        ally_one.dy *= -1

    if ally_one.xcor() > 390:
        ally_one.setx(390)
        ally_one.dx *= -1

    if ally_one.xcor() < -390:
        ally_one.setx(-390)
        ally_one.dx *= -1

    # if player_one.xcor()

    if player_one.xcor() == (0):
        player_one.color("blue")

    else:
        player_one.color("white")

    if (
        enemy_one.xcor() - 25 <= player_one.xcor()
        and player_one.xcor() <= enemy_one.xcor() + 25
        and enemy_one.ycor() - 25 <= player_one.ycor()
        and player_one.ycor() <= enemy_one.ycor() + 25
    ):
        player_one.goto(randint(-390, 0), randint(0, 390))
        score_a += 1
        score_b -= 1
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if (
        enemy_two.xcor() - 25 <= player_one.xcor()
        and player_one.xcor() <= enemy_two.xcor() + 25
        and enemy_two.ycor() - 25 <= player_one.ycor()
        and player_one.ycor() <= enemy_two.ycor() + 25
    ):
        player_one.goto(randint(-390, 0), randint(0, 390))
        score_a += 1
        score_b -= 1
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}  level: {level} ",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if player_one.xcor() > 390:
        player_one.goto(380, player_one.ycor())

    if player_one.xcor() < -390:
        player_one.goto(-390, player_one.ycor())

    if player_one.ycor() > 290:
        player_one.goto(player_one.xcor(), 290)

    if player_one.ycor() < -290:
        player_one.goto(player_one.xcor(), -280)

    if (
        ally_one.xcor() - 25 <= player_one.xcor()
        and player_one.xcor() <= ally_one.xcor() + 25
        and ally_one.ycor() - 25 <= player_one.ycor()
        and player_one.ycor() <= ally_one.ycor() + 25
    ):
        player_one.goto(randint(-390, 0), randint(0, 390))
        score_b += 1
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}  level: {level}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if score_b == 1:
        level += 1
        enemy_one.dx += 0.2
        enemy_one.dy += 0.2
        enemy_two.dx += 0.2
        enemy_two.dx += 0.2
        score_b += 2
        pen.clear()
        pen.write(
            f"deaths: {score_a}  points: {score_b}  level: {level}",
            align="center",
            font=("Courier", 24, "normal"),
        )
