from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('yellow')
        self.speed(0) #fastest

    def refresh(self, snake):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

        # refresh food when food generates on snake segments
        for segment in snake.segments:
            if self.distance(segment.pos()) < 10 :
                print(f'food: {self.pos()},seg: {segment.pos()}')
                self.refresh(snake)