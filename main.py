from collections import namedtuple

import pyglet

from pyglet.window import key

pyglet.resource.path = ['resources/']
pyglet.resource.reindex()

window = pyglet.window.Window(800, 600)
ship_img = pyglet.resource.image('ship.png')
player_ship = pyglet.sprite.Sprite(img=ship_img, x=400, y=300)

@window.event
def on_draw():
    window.clear()
    player_ship.draw()

@window.event
def on_key_press(symbol, modifiers):
    global player_ship
    if   symbol == key.W: player_ship.y += 10
    elif symbol == key.A: player_ship.x += -10
    elif symbol == key.S: player_ship.y += -10
    elif symbol == key.D: player_ship.x += 10


if __name__== '__main__':
    pyglet.app.run()
