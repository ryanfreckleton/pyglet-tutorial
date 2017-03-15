from collections import namedtuple

import math

import pyglet

from pyglet.window import key

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

pyglet.resource.path = ['resources/']
pyglet.resource.reindex()

window = pyglet.window.Window(800, 600)
ship_img = pyglet.resource.image('ship.png')
asteroid_img = pyglet.resource.image('asteroid.png')
player_ship = pyglet.sprite.Sprite(img=ship_img, x=400, y=300)
player_ship.alive = True
player_ship.vel_x = 0
player_ship.vel_y = 0

asteroid = pyglet.sprite.Sprite(img=asteroid_img, x=300, y=400)
sound = pyglet.resource.media('explosion.wav', streaming=False)

center_image(player_ship)
center_image(asteroid)

@window.event
def on_draw():
    window.clear()
    if player_ship.alive:
        player_ship.draw()
    asteroid.draw()

@window.event
def on_key_press(symbol, modifiers):
    global player_ship
    if   symbol == key.W: player_ship.vel_y = 5
    elif symbol == key.A: player_ship.vel_x = -5
    elif symbol == key.S: player_ship.vel_y = -5
    elif symbol == key.D: player_ship.vel_x = 5

@window.event
def on_key_release(symbol, modifiers):
    global player_ship
    if   symbol == key.W: player_ship.vel_y = 0
    if   symbol == key.A: player_ship.vel_x = 0
    if   symbol == key.S: player_ship.vel_y = 0
    if   symbol == key.D: player_ship.vel_x = 0

def update(dt):
    global asteroid, player_ship, flag
    if player_ship.x > asteroid.x:
        asteroid.x += 1
    else:
        asteroid.x -= 1

    if player_ship.y > asteroid.y:
        asteroid.y += 1
    else:
        asteroid.y -= 1

    player_ship.x += player_ship.vel_x
    player_ship.y += player_ship.vel_y

    if player_ship.alive and math.hypot(asteroid.x - player_ship.x, asteroid.y - player_ship.y) < 50:
        sound.play()
        player_ship.alive = False


if __name__== '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
