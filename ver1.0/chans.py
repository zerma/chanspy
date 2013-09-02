import pyglet 

ventana =  pyglet.window.Window(800, 600)
puntos_label = pyglet.text.Label(text="Puntos: 0", x=10, y=575)
nivel_label = pyglet.text.Label(text="Chanspy", x=400, y=575, anchor_x='center')

@ventana.event
def on_draw(): 
	ventana.clear()
	puntos_label.draw()
	nivel_label.draw()

pyglet.app.run()