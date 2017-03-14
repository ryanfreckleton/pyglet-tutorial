from collections import namedtuple

import pyglet

from pyglet.window import key

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = pyglet.window.Window(800, 600)
player = Player(window.width//2, window.height//2)
label = pyglet.text.Label("Player", x=player.x, y=player.y)

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    global label
    if   symbol == key.W: label.y += 10
    elif symbol == key.A: label.x += -10
    elif symbol == key.S: label.y += -10
    elif symbol == key.D: label.x += 10


if __name__== '__main__':
    pyglet.app.run()
