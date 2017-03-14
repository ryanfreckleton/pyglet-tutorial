import pyglet

window = pyglet.window.Window(800, 600)
label = pyglet.text.Label("Hello, World!",
            x=window.width//2,
            y=window.height//2)

@window.event
def on_draw():
    window.clear()
    label.draw()

if __name__== '__main__':
    pyglet.app.run()
