import pyglet
from juego import recursos
# Posición de las columnas donde puede caer el huevo
cols = [270,390,525]
# Inicialización de la ventana con un tamaño de 800x600 px
ventana =  pyglet.window.Window(800, 600)
# Decalaración de las etiquetas superiores
puntos_label = pyglet.text.Label(text="Puntos: 0", x=10, y=575)
nivel_label = pyglet.text.Label(text="Huevos! Chansey", x=400, y=575, anchor_x='center')
fails_label = pyglet.text.Label(text="Oportunidades:", x=590, y=575)
# Definición de huevos de oportunidades
mini_1 = pyglet.sprite.Sprite(img=recursos.mini_egg, x=730, y=580)
mini_2 = pyglet.sprite.Sprite(img=recursos.mini_egg, x=755, y=580)
mini_3 = pyglet.sprite.Sprite(img=recursos.mini_egg, x=780, y=580)
# Definición de huevos fallidos
mini_fail_1 = pyglet.sprite.Sprite(img=recursos.mini_egg_fail, x=730, y=580)
mini_fail_2 = pyglet.sprite.Sprite(img=recursos.mini_egg_fail, x=755, y=580)
mini_fail_3 = pyglet.sprite.Sprite(img=recursos.mini_egg_fail, x=780, y=580)
# Definición de 
huevo = pyglet.sprite.Sprite(img=recursos.egg, x=cols[1], y=300)
ch_izq = pyglet.sprite.Sprite(img=recursos.chansey_left, x=300, y=184)
ch_der = pyglet.sprite.Sprite(img=recursos.chansey_right, x=500, y=184)
ch_cen = pyglet.sprite.Sprite(img=recursos.chansey_center, x=400, y=177)
fondo = pyglet.sprite.Sprite(img=recursos.bg, x=0, y=0)

@ventana.event
def on_draw():
	ventana.clear()

	fondo.draw()

	puntos_label.draw()
	nivel_label.draw()
	fails_label.draw()

	mini_1.draw()
	mini_2.draw()
	mini_3.draw()

	ch_cen.draw()

	huevo.draw()

pyglet.app.run()