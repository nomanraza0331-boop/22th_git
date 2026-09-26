import turtle

# ----------------------------
# Window
# ----------------------------
wn = turtle.Screen()
wn.title("Single Player Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# ----------------------------
# Player Paddle
# ----------------------------
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.shapesize(stretch_wid=5, stretch_len=1)
player.penup()
player.goto(-350, 0)

# ----------------------------
# AI Paddle
# ----------------------------
ai = turtle.Turtle()
ai.shape("square")
ai.color("white")
ai.shapesize(stretch_wid=5, stretch_len=1)
ai.penup()
ai.goto(350, 0)

# ----------------------------
# Ball
# ----------------------------
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# ----------------------------
# Score
# ----------------------------
player_score = 0
ai_score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)

def update_score():
    pen.clear()
    pen.write(
        f"Player: {player_score}   AI: {ai_score}",
        align="center",
        font=("Courier", 20, "normal")
    )

update_score()

# ----------------------------
# Player Controls
# ----------------------------
def player_up():
    if player.ycor() < 250:
        player.sety(player.ycor() + 25)

def player_down():
    if player.ycor() > -250:
        player.sety(player.ycor() - 25)

wn.listen()
wn.onkeypress(player_up, "w")
wn.onkeypress(player_down, "s")

# ----------------------------
# Main Game Loop
# ----------------------------
while True:
    wn.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # AI Movement
    if ai.ycor() < ball.ycor() - 10:
        ai.sety(min(ai.ycor() + 0.18, 250))
    elif ai.ycor() > ball.ycor() + 10:
        ai.sety(max(ai.ycor() - 0.18, -250))

    # Top & Bottom Bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right Wall (Player Scores)
    if ball.xcor() > 390:
        player_score += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = -0.25
        ball.dy = 0.25

    # Left Wall (AI Scores)
    if ball.xcor() < -390:
        ai_score += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = 0.25
        ball.dy = -0.25

    # Player Paddle Collision
    if (-350 < ball.xcor() < -340 and
        player.ycor() - 50 < ball.ycor() < player.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    # AI Paddle Collision
    if (340 < ball.xcor() < 350 and
        ai.ycor() - 50 < ball.ycor() < ai.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # Gradually Increase Ball Speed
    if abs(ball.dx) < 0.8:
        if ball.dx > 0:
            ball.dx += 0.00005
        else:
            ball.dx -= 0.00005

        if ball.dy > 0:
            ball.dy += 0.00005
        else:
            ball.dy -= 0.00005