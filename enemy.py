from turtle import Turtle

ENEMY_COL = 7
ENEMY_ROW = 3


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.all_enemy = []
        self.hideturtle()
        self.pos_x = -330
        self.pos_y = 120
        self.x_move = 2
        self.generate_enemies()

    def generate_enemies(self):
        enemy_col = []
        for _ in range(ENEMY_COL):
            for _ in range(ENEMY_ROW):
                new_enemy = Turtle("turtle")
                new_enemy.shapesize(stretch_wid=2, stretch_len=1)
                new_enemy.color("red")
                new_enemy.setheading(270)
                new_enemy.penup()
                new_enemy.goto(self.pos_x, self.pos_y)
                self.pos_y += 50
                enemy_col.append(new_enemy)
            self.pos_x += 60
            self.pos_y = 120
            self.all_enemy.append(enemy_col)
            enemy_col = []

    def moving_pattern(self):
        for col in self.all_enemy:
            for enemy in col:
                enemy.goto(enemy.xcor() + self.x_move, enemy.ycor())

    def bounce_side_wall(self):
        self.x_move *= -1

    def missile_hit(self, enemy_ship):
        enemy_ship.reset()
        enemy_ship.penup()
        enemy_ship.hideturtle()



