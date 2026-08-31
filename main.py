from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from rong import Deat
import time

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("🐍 Python Snake Game - Use Arrow Keys to Play")
screen.bgcolor("#1a1a2e")  # Dark blue background
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
score = Score()
deat = Deat()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
  
game_is_on = True
deat.goin_posiuon()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.Move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_point()
        score.update_score()
        
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    



screen.exitonclick()