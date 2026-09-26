import turtle
import random

# -----------------------------
# Window Setup
# -----------------------------
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.tracer(0)

# -----------------------------
# Player
# -----------------------------
player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -300)

# -----------------------------
# Bullet
# -----------------------------
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.3, stretch_len=0.8)
bullet.penup()
bullet.hideturtle()

bullet_speed = 20
bullet_state = "ready"

# -----------------------------
# Enemies
# -----------------------------
enemies = []

for _ in range(8):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.goto(random.randint(-300, 300), random.randint(150, 300))
    enemies.append(enemy)

enemy_speed = 2

# -----------------------------
# Score
# -----------------------------
score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-320, 320)

def update_score():
    pen.clear()
    pen.write(f"Score: {score}", font=("Arial", 16, "normal"))

update_score()

# -----------------------------
# Controls
# -----------------------------
def move_left():
    x = player.xcor()
    x -= 20
    if x < -320:
        x = -320
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 320:
        x = 320
    player.setx(x)

def fire_bullet():
    global bullet_state

    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 15)
        bullet.showturtle()

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# -----------------------------
# Collision Function
# -----------------------------
def collision(t1, t2):
    return t1.distance(t2) < 20

# -----------------------------
# Game Loop
# -----------------------------
while True:
    screen.update()

    # Move enemies
    edge = False

    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy_speed)

        if enemy.xcor() > 320 or enemy.xcor() < -320:
            edge = True

        # Collision with bullet
        if bullet_state == "fire" and collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)

            enemy.goto(random.randint(-300, 300), random.randint(180, 300))

            score += 10
            update_score()

        # Enemy reaches player
        if enemy.ycor() < -270:
            pen.goto(-80, 0)
            pen.write("GAME OVER", font=("Arial", 28, "bold"))
            screen.update()
            turtle.done()

    # Reverse enemy direction
    if edge:
        enemy_speed *= -1
        for enemy in enemies:
            enemy.sety(enemy.ycor() - 30)

    # Move bullet
    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + bullet_speed)

    if bullet.ycor() > 340:
        bullet.hideturtle()
        bullet_state = "ready"

turtle.done()