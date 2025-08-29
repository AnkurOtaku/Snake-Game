from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'normal')
POSITION = (0,270)

class Scoreboard(Turtle):
    score = 0
    def __init__(self, score=0):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.home()
        self.write('Press Num 0 to start Snake Game', False, ALIGN, FONT)
        self.goto(POSITION)

    def show_score(self):
        self.clear()
        self.write(f'Score : {self.score}', False, ALIGN , FONT)

    def increase_score(self):
        self.score+=1
        self.show_score()

    def game_over(self):
        self.show_score()
        self.home()
        self.write('Game Over', False, ALIGN, FONT)