from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 18, 'normal')
POSITION = (0,270)

class Scoreboard(Turtle):

    def __init__(self, score=0):
        super().__init__()
        self.score = 0
        with open('high_score.txt', mode='r') as data:
            self.high_score = int(data.read())
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
            with open('high_score.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.show_score()

    def game_over(self):
        self.show_score()
        self.score = 0
        self.restart_instructions()

    def restart_instructions(self):
        self.home()
        self.write('Press Num 0 to start Snake Game Again', False, ALIGN, FONT)