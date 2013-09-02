import pyglet

pyglet.resource.path = ['recursos']
pyglet.resource.reindex()

chansey_right = pyglet.resource.image("chans-right.png")
chansey_left = pyglet.resource.image("chans-left.png")
chansey_center = pyglet.resource.image("chans-center.png")
mini_egg = pyglet.resource.image("mini-egg.png")
mini_egg_fail = pyglet.resource.image("mini-egg-fail.png")
egg = pyglet.resource.image("egg.png")
bg = pyglet.resource.image("fondo.png")

def centrar_imagen(imagen):
	imagen.anchor_x = imagen.width  / 2
	imagen.anchor_y = imagen.height / 2

centrar_imagen(chansey_right)
centrar_imagen(chansey_left)
centrar_imagen(chansey_center)
centrar_imagen(egg)
centrar_imagen(mini_egg)
centrar_imagen(mini_egg_fail)