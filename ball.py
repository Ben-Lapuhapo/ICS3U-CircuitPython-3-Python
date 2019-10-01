# Created by Ben Lapuhapo
# Created on Oct 2019
# Pibadge

import ugame
import stage
import digitalio
import board
import time

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
bank = stage.Bank.from_bmp16("ball.bmp")
background = stage.Grid(bank, 10, 8)
ball = stage.Sprite(bank, 1, 8, 8)
game = stage.Stage(ugame.display, 12)
game.layers = [ball, background]
game.render_block()

dx = 2
while True:
    ball.update()
    ball.set_frame(ball.frame % 4 + 1)
    ball.move(ball.x + dx, ball.y)
    if not 0 < ball.x < 144:
        dx = -dx
    game.render_sprites([ball])
    game.tick()
