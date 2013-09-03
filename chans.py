# -*- coding: utf-8 -*-
import pyglet, random
from pyglet.window import key
from juego import recursos
# Posición de las columnas donde puede caer el huevo
cols = [270,390,525]
# Inicialización de la ventana con un tamaño de 800x600 px
ventana =  pyglet.window.Window(800, 600)
puntos = 0
fallas = 0
killed = False

tecla = key.KeyStateHandler()
ventana.push_handlers(tecla)
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

mini_fail_1.visible = False
mini_fail_2.visible = False
mini_fail_3.visible = False

fails = [mini_fail_1, mini_fail_2, mini_fail_3]
# Definición de sprites y sus posiciones
huevo = pyglet.sprite.Sprite(img=recursos.egg, x=cols[random.randint(0, 2)], y=700)
ch_izq = pyglet.sprite.Sprite(img=recursos.chansey_left, x=300, y=184)
ch_der = pyglet.sprite.Sprite(img=recursos.chansey_right, x=500, y=184)
ch_cen = pyglet.sprite.Sprite(img=recursos.chansey_center, x=400, y=177)

ch_izq.visible = False
ch_der.visible = False

fondo = pyglet.sprite.Sprite(img=recursos.bg, x=0, y=0)

# Envento de redibujado
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

	mini_fail_1.draw()
	mini_fail_2.draw()
	mini_fail_3.draw()

	ch_cen.draw()
	ch_izq.draw()
	ch_der.draw()

	huevo.draw()

def actualizar(dt):
	global puntos
	global killed
	caidaHuevo(dt)
	if killed:
		pass
	else:
		if tecla[key.LEFT]:
			ch_izq.visible = True
			ch_der.visible = False
			ch_cen.visible = False
			if huevo.y < 150 and huevo.x == cols[0]:
				resetHuevo()
				puntos = puntos + 1
				puntos_label.text = "Puntos: " + str(puntos)

		elif tecla[key.RIGHT]:
			ch_izq.visible = False
			ch_der.visible = True
			ch_cen.visible = False
			if huevo.y < 150 and huevo.x == cols[2]:
				resetHuevo()
				puntos = puntos + 1
				puntos_label.text = "Puntos: " + str(puntos)
		else:
			ch_izq.visible = False
			ch_der.visible = False
			ch_cen.visible = True
			if huevo.y < 150 and huevo.x == cols[1]:
				resetHuevo()
				puntos = puntos + 1
				puntos_label.text = "Puntos: " + str(puntos)
		limiteHuevo()

def caidaHuevo(dt):
	huevo.y -= 100 * dt

def limiteHuevo():
	global fails
	global fallas
	if huevo.y < 130:
		resetHuevo()
		if fallas < 3:
			fails[fallas].visible = True
			fallas = fallas + 1
		else:
			killAll()

def resetHuevo():
	huevo.x = cols[random.randint(0, 2)]
	huevo.y = 700

def killAll():
	global killed 
	killed = True
	fondo.visible = False
	mini_1.visible = False
	mini_2.visible = False
	mini_3.visible = False
	mini_fail_1.visible = False
	mini_fail_2.visible = False
	mini_fail_3.visible = False
	ch_cen.visible = False
	ch_izq.visible = False
	ch_der.visible = False
	huevo.visible = False
	puntos_label.text = ""
	nivel_label.text = "Game Over"
	nivel_label.y = 300
	fails_label.text = ""

# Corriendo el juego
if __name__ == '__main__':
	pyglet.clock.schedule_interval(actualizar, 1/120.0)
	pyglet.app.run()