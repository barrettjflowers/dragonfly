import pygame
from window import *

#Player
player = pygame.image.load('source/graphics/dragon.png').convert_alpha()
player_scale = x, y = 71, 60
player = pygame.transform.scale(player, player_scale)
player_rect = player.get_rect()
player_x = 400
player_y = 400