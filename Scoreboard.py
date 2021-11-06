from turtle import Turtle

FONT = ('Arial', 20, 'normal')


class Scoreboard_Left(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-200, 200)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(self.score, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, font=FONT)


class Scoreboard_Right(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(200, 200)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(self.score, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, font=FONT)
