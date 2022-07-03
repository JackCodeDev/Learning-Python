# Create Screen
# Create and move paddle
# Create another paddle
# Create Ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle missed
# Keep score
from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Score
from wall import Wall
screen = Screen()
screen.setup(height=600, width= 800)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)
wall_1 = Wall(0, 300)
wall_2 = Wall(0, -300)

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_1.go_right, "Right")
screen.onkey(paddle_1.go_left, "Left")

screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")
screen.onkey(paddle_2.go_right, "d")
screen.onkey(paddle_2.go_left, "a")

score = Score()
new_ball = Ball()


game_on = True
while game_on:
    time.sleep(new_ball.move_speed)
    screen.update()
    new_ball.move_ball()

    if new_ball.xcor() > 380:
        score.new_score_1()
        new_ball.reset_position()
        # game_on = False
    if new_ball.xcor() < -380:
        score.new_score_2()
        new_ball.reset_position()
        # game_on = False
    if new_ball.ycor() > 280 or new_ball.ycor() < -280:
        new_ball.bounce_y()
    # detect collision with paddle_1
    if new_ball.distance(paddle_1.paddle) < 50 and new_ball.xcor() > 320:
        new_ball.bounce_x()
    # detect collision with paddle_2
    if new_ball.distance(paddle_2.paddle) < 50 and new_ball.xcor() < -320:
        new_ball.bounce_x()

    if score.score_1 > 3 or score.score_2 > 3:
        game_on = False
        score.game_over()















screen.exitonclick()

