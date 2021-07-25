import pygame as pg, random

ANCHO = 800
ALTO = 600

NEGRO = (0, 0, 0)

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("The Quest")
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("images/naveLukeSky.png").convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.centerx = 75
		self.rect.bottom = ANCHO // 2
		self.speed_y = 0

	def update(self):
		self.speed_y = 0
		keystate = pg.key.get_pressed()
		if keystate[pg.K_UP]:
			self.speed_y = -5
		if keystate[pg.K_DOWN]:
			self.speed_y = 5
		self.rect.y += self.speed_y
		if self.rect.bottom > ALTO:
			self.rect.bottom = ALTO
		if self.rect.top < 0:
			self.rect.top = 0

class Meteor(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pg.image.load("images/asteroide.png").convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ALTO - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)

	def update(self):
		self.rect.y += self.speedy


# Cargar fondo.
background = pg.image.load("images/fondo.png").convert()


all_sprites = pg.sprite.Group()
meteor_list = pg.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
	meteor = Meteor()
	all_sprites.add(meteor)
	meteor_list.add(meteor)

# Game Loop
running = True
while running:
	# Keep loop running at the right speed
	clock.tick(60)
	# Process input (events)
	for event in pg.event.get():
		# check for closing window
		if event.type == pg.QUIT:
			running = False
		

	# Update
	all_sprites.update()




	#Draw / Render
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)
	# *after* drawing everything, flip the display.
	pg.display.flip()

pg.quit()
