from turtle import Screen
from tkinter import messagebox
import time
from player import Player
from player_missile import PlayerMissile
from enemy import Enemy
from enemy_missile import EnemyMissile
import random

screen = Screen()

screen.setup(800, 600)
screen.bgpic("images/stars.png")
screen.title("Space Invader")
screen.tracer(0)

player = Player()
player_missile = PlayerMissile()
enemy = Enemy()
enemy_missile = EnemyMissile()

screen.listen()
screen.onkey(player.player_right, "Right")
screen.onkey(player.player_left, "Left")

game_on = True
index = -1

while game_on:
    if not player_missile.missile_launch:
        screen.onkey(lambda x=None: player_missile.initiate_missile(player.xcor()), "Up")
    else:
        screen.onkey(None, "Up")
        player_missile.launch()
    enemy.moving_pattern()

    num = random.randint(0, 20)
    if num == 10:
        enemy_missile.initiate_missiles(enemy.all_enemy)
    for missile in enemy_missile.all_enemy_missile:
        enemy_missile.launch(missile)

        # Enemy missile hit the ground
        if missile.ycor() < -280:
            enemy_missile.explode_impact(missile)

        # Enemy missile and player missile collide
        if missile.distance(player_missile) < 20:
            enemy_missile.explode_impact(missile)
            player_missile.explode_impact()
            player.score += 1

        # Enemy missile hit the player, game over
        if missile.distance(player) < 40:
            game_on = False
            messagebox.showinfo(title="Game Over", message=f"Your score is: {player.score}")
            break

    time.sleep(player_missile.move_speed)
    screen.update()

    # Player missile reach the top wall
    if player_missile.ycor() > 280:
        player_missile.explode_impact()

    # Enemy touch the side wall
    try:
        if enemy.all_enemy[index][0].xcor() > 330 or enemy.all_enemy[0][0].xcor() < -330:
            enemy.bounce_side_wall()
    except IndexError:
        index -= 1

    # Missile hit the enemy
    for col in enemy.all_enemy:
        for enemy_ship in col:
            if enemy_ship.distance(player_missile) < 40:
                enemy.missile_hit(enemy_ship)
                player_missile.explode_impact()
                col.remove(enemy_ship)
                player.score += 10

    if not enemy.all_enemy[0]:
        game_on = False
        messagebox.showinfo(title="Game Over", message=f"You win\nYour score is: {player.score}")


screen.exitonclick()
