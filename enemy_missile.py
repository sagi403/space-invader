from turtle import Turtle
import random


class EnemyMissile(Turtle):

    def __init__(self):
        super().__init__()
        self.y_move = -5
        self.penup()
        self.hideturtle()
        self.all_enemy_missile = []

    def initiate_missiles(self, enemy):
        pos_x, pos_y = enemy[random.randint(0, len(enemy) - 1)][0].position()
        new_missile = Turtle("arrow")
        new_missile.color("white")
        new_missile.setheading(270)
        new_missile.shapesize(stretch_wid=0.25, stretch_len=3)
        new_missile.penup()
        new_missile.goto(pos_x, pos_y - 30)
        self.all_enemy_missile.append(new_missile)

    def launch(self, missile):
        new_y = missile.ycor() + self.y_move
        missile.goto(missile.xcor(), new_y)

    def explode_impact(self, missile):
        self.all_enemy_missile.remove(missile)
        missile.reset()
        missile.penup()
        missile.goto(-1000, -1000)






