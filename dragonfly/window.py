import pygame

size = width, height = 600, 700
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Dragon Fly')
clock = pygame.time.Clock()

#Background
background_surface = pygame.image.load('source/graphics/background.png').convert_alpha()
background_surface = pygame.transform.scale(background_surface, size)
screen_rect = background_surface.get_rect()