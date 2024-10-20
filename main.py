from turtle import Screen
from food import Food
import time

from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280
            or snake.head.ycor() < -280):
        scoreboard.score_reset()
        snake.snake_reset()


    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.score_reset()
            snake.snake_reset()























screen.exitonclick()