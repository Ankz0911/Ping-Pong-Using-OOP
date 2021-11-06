from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.goto(x_cor, y_cor)
        self.left(90)
        self.shapesize(stretch_len=5)
        self.color('white')
        self.penup()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
