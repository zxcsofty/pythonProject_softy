import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 480
HEIGHT = 600
FPS = 60

# Загрузка всей игровой графики
background = pygame.image.load('sources/starfield.png')
background_rect = background.get_rect()
player_img = pygame.image.load('sources/player.png')
meteor_img = pygame.image.load('sources/mob.png')
bullet_img = pygame.image.load('sources/bullet.png')


meteor_images = []
meteor_list =['meteorBrown_big1.png','meteorBrown_med1.png',
              'meteorBrown_med1.png','meteorBrown_med3.png',
              'meteorBrown_small1.png','meteorBrown_small2.png',
              'meteorBrown_tiny1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load('sources/mob.png'))