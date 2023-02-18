import turtle
import os 

# Create the window
window = turtle.Screen()
window.title("Pong by Maycon")
window.bgcolor("black")
window.setup(width=900, height=600)
window.tracer(0)
#score 

score_a = 0
score_b = 0


# Create the left paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Create the right paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2
# create a pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write( "Player A :   {}   Player B : {} " .format(score_a, score_b), align =  "center", font=(   "currie ", 22, "normal")) 



# Create the obstacle turtle
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("red")
obstacle.shapesize(stretch_wid=4, stretch_len=1)
obstacle.penup()
obstacle.goto(0, 0)

# Initialize the obstacle direction
obstacle_direction = 1

# Functions for moving the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the obstacle up or down
    obstacle.sety(obstacle.ycor() + obstacle_direction * 10)

    # Reverse the obstacle direction if it hits the top or bottom of the screen
    if obstacle.ycor() > 290 or obstacle.ycor() < -290:
        obstacle_direction *= -1

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision detection with obstacle 
    if ball.distance(obstacle) < 20:
        ball.dx *= -1

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("play pong.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write( "Player A :   {}   Player B : {} " .format(score_a, score_b), align =  "center", font=(   "currie ", 22, "normal")) 

    if ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write( "Player A :   {}   Player B : {} " .format(score_a, score_b), align =  "center", font=(   "currie ", 22, "normal")) 

    # Collision detection with paddles
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1 

        input()
