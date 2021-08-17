from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import math
import time

THRESHOLD_FOOD = 15  # 15px
THRESHOLD_SCREEN = 280
GAME_SPEED = 0.1
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("The Classic Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Detect collision with food
    snake_x, snake_y = snake.head.position()
    food_x, food_y = food.position()

    dist = math.sqrt((snake_x - food_x) ** 2 + (snake_y - food_y) ** 2)
    if dist <= THRESHOLD_FOOD:
        food.new()
        snake.enlarge()
        scoreboard.update()

    # Detect Collision with wall
    if snake_x > THRESHOLD_SCREEN or snake_x < -THRESHOLD_SCREEN or snake_y > THRESHOLD_SCREEN or snake_y <-THRESHOLD_SCREEN:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
