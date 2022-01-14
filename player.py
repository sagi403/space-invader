from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pos = (0, -250)
        self.create_player()
        self.score = 0

    def create_player(self):
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(self.pos)
        self.setheading(90)
        self.shapesize(stretch_wid=4, stretch_len=1)

    def player_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def player_left(self):
        self.goto(self.xcor() - 20, self.ycor())



