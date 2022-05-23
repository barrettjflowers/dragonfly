import pygame
import random
from window import screen


'''barrier = pygame.image.load('source/graphics/barrier.png').convert_alpha()
barrier_scale = x, y = 600, 100
barrier = pygame.transform.scale(barrier, barrier_scale)
barrier_rect = barrier.get_rect()

random_int = random.randint(-width, -50)

bpos_x = random_int
bpos_y = -barrier_rect.bottom
barrier_pos = (bpos_x, bpos_y)

barrier_r = pygame.image.load('source/graphics/barrier.png').convert_alpha()
barrier_r = pygame.transform.scale(barrier_r, barrier_scale)
barrier_r = pygame.transform.flip(barrier, True, False)
barrierr_rect = barrier_r.get_rect()
bpos_rx = bpos_x + barrier_rect.right + 125
bpos_ry = 0'''


def Barrier(blit):

    blit = False

    Barrier.barrier = pygame.image.load('source/graphics/barrier.png').convert_alpha()
    Barrier.barrier_scale = x, y = 600, 100
    Barrier.barrier = pygame.transform.scale(Barrier.barrier, Barrier.barrier_scale)
    Barrier.barrier_rect = Barrier.barrier.get_rect()

    Barrier.random_int = (random.randint(-600, -50))

    Barrier.bpos_x =(Barrier.random_int)
    Barrier.bpos_y = (-Barrier.barrier_rect.bottom)
    Barrier.barrier_pos = (Barrier.bpos_x, Barrier.bpos_y)

    Barrier.barrier_r = pygame.image.load('source/graphics/barrier.png').convert_alpha()
    Barrier.barrier_r = pygame.transform.scale(Barrier.barrier_r, Barrier.barrier_scale)
    Barrier.barrier_r = pygame.transform.flip(Barrier.barrier, True, False)
    Barrier.barrierr_rect = Barrier.barrier_r.get_rect()
    Barrier.bpos_rx =(Barrier.bpos_x + Barrier.barrier_rect.right + 125)
    Barrier.bpos_ry = (0)

    if blit == True:
        screen.blit(Barrier.barrier, (Barrier.bpos_x, Barrier.bpos_y))
        screen.blit(Barrier.barrier_r,(Barrier.bpos_rx, Barrier.bpos_ry))