from turtle import Screen
from turtle_pro.snake_game.snake import Snake
from turtle_pro.snake_game.food import Food
from turtle_pro.snake_game.score_board import Score
import time

screen = Screen()
name = screen.textinput(prompt="Enter your name",title="player name")
food = Food()
scoreB = Score()
scoreB.player = name
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game by SAT")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # Detection collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreB.increment()

    # Detection collision with wal.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreB.game_over()
        scoreB.write_data()
        is_game_on = False
        if scoreB.score > scoreB.high_score:
            scoreB.high_score = scoreB.score
            scoreB.player = name
            scoreB.update_score()

    # Detection  collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreB.write_data()
            scoreB.game_over()
            is_game_on = False



screen.exitonclick()
