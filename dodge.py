import turtle
from turtle import Turtle
from random import randint

# leave for later
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
window = turtle.Screen()
window.title("dodge! by Isaac and Adam")
window.bgcolor("black")
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.tracer(0)

window.listen()

# score
score_a = 0
score_b = 0
level = 1


class Player(Turtle):
    def __init__(self, key_up, key_down, key_left, key_right):
        super(Player, self).__init__()
        self.shape("square")
        self.color("blue")
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.make_moveable()

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

    def move_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

    def make_moveable(self):
        window.onkeypress(self.move_up, self.key_up)
        window.onkeypress(self.move_down, self.key_down)
        window.onkeypress(self.move_left, self.key_left)
        window.onkeypress(self.move_right, self.key_right)

    # player staying within the bounds
    def stay_within_bounds(self):
        x = get_x_bound()
        y = get_y_bound()

        if self.xcor() > x:
            self.goto(x, self.ycor())

        if self.xcor() < -x:
            self.goto(-x, self.ycor())

        if self.ycor() > y:
            self.goto(self.xcor(), y)

        if self.ycor() < -y:
            self.goto(self.xcor(), -y)


player_one = Player("w", "s", "a", "d")


def get_x_bound():
    return SCREEN_WIDTH / 2 - 10


def get_y_bound():
    return SCREEN_HEIGHT / 2 - 10


def add_spawn_turtle_randomly(cls):
    def spawn_turtle_randomly(self):
        x = get_x_bound()
        y = get_y_bound()
        self.goto(randint(-x, x), randint(-y, y))

    cls.spawn_turtle_randomly = spawn_turtle_randomly
    return cls


def add_move(cls):
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    cls.move = move
    return cls


def add_bounce(cls):
    def bounce(self):
        x = get_x_bound()
        y = get_y_bound()

        if self.xcor() > x:
            self.setx(x)
            self.dx *= -1

        if self.xcor() < -x:
            self.setx(-x)
            self.dx *= -1

        if self.ycor() > y:
            self.sety(y)
            self.dy *= -1

        if self.ycor() < -y:
            self.sety(-y)
            self.dy *= -1

    cls.bounce = bounce
    return cls


@add_spawn_turtle_randomly
@add_move
@add_bounce
class Enemy(Turtle):
    def __init__(self):
        super(Enemy, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("red")
        self.speed(0)
        self.penup()
        self.spawn_turtle_randomly()
        self.dx = 0.02
        self.dy = -0.02


enemy_one = Enemy()
enemy_two = Enemy()


@add_spawn_turtle_randomly
@add_move
@add_bounce
class Ally(Turtle):
    def __init__(self):
        super(Ally, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("green")
        self.speed(0)
        self.penup()
        self.spawn_turtle_randomly()
        self.dx = 0.2
        self.dy = -0.1


ally_one = Ally()


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


while True:
    window.update()

    player_one.stay_within_bounds()
    enemy_one.move()
    enemy_one.bounce()
    enemy_two.move()
    enemy_two.bounce()
    ally_one.move()
    ally_one.bounce()

    # handling the collision (death increment)
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

    # score doodles
    if score_b == 10:
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

    if score_b == 15:
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
