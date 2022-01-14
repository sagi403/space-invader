from turtle import Turtle


class PlayerMissile(Turtle):

    def __init__(self):
        super().__init__()
        self.y_move = 5
        self.penup()
        self.goto(1000, 1000)
        self.hideturtle()
        self.move_speed = 0.03
        self.missile_launch = False

    def initiate_missile(self, player_x):
        self.shape("arrow")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.penup()
        self.goto(player_x, -220)
        self.missile_launch = True

    def launch(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def explode_impact(self):
        self.reset()
        self.penup()
        self.goto(0, -1000)
        self.missile_launch = False

