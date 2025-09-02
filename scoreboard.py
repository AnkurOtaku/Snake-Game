from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'normal')
POSITION = (0,270)

class Scoreboard(Turtle):

    def __init__(self, score=0):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.home()
        self.write('Press Num 0 to start Snake Game', False, ALIGN, FONT)
        self.goto(POSITION)

    def show_score(self):
        self.clear()
        self.goto(POSITION)
        self.write(f'Score : {self.score} HIGH SCORE: {self.high_score}', False, ALIGN , FONT)

    def increase_score(self):
        self.score+=1
        if self.score> self.high_score:
            self.high_score = self.score
        self.show_score()

    def game_over(self):
        self.score = 0
        self.show_score()
        self.restart_instructions()

    def restart_instructions(self):
        self.home()
        self.write('Press Num 0 to start Snake Game Again', False, ALIGN, FONT)