from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 1000
HEIGHT = 600

screen = Screen()
screen.bgcolor('black')
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()

scoreboard = Scoreboard()

food.refresh(snake)
is_game_on = False

def start_game():
    global is_game_on
    is_game_on = True
    scoreboard.clear()
    scoreboard.show_score()

    while is_game_on:
        time.sleep(0.1)
        snake.move()
        screen.update()

        if snake.head.distance(food) < 15:
            food.refresh(snake)
            scoreboard.increase_score()
            snake.extend()

        if snake.head.xcor() > WIDTH/2-20 or snake.head.xcor() < -1*WIDTH/2+20 or snake.head.ycor() > HEIGHT/2-20 or snake.head.ycor() < -1*HEIGHT/2+20:
            is_game_on = False
            scoreboard.game_over()
            for segment in snake.segments:
                segment.clear()
                segment.reset()
            snake.__init__()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10 :
                is_game_on = False
                scoreboard.game_over()
                for segment in snake.segments:
                    segment.clear()
                    segment.reset()
                snake.__init__()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(start_game, "0")
screen.exitonclick()