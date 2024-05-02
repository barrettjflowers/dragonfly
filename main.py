import pygame
from pygame.constants import K_a, K_d
from player import *
from window import *
from menu import *
from barriers import Barrier

import random
from sys import exit

gravity = 0
velocity = 0
state = True
up = True
menu = True
score = 0
Barrier(False)

pygame.init()

while state:

    # score_up = player_y >= Barrier.bpos_y
    # score_event = pygame.event.Event(score_up)
    # pygame.event.post(score_event)

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -10
                y-=10
                flap = pygame.mixer.Sound("source/audio/flap.wav")
                flap.set_volume(0.20)
                flap.play()
            if event.key == pygame.K_RETURN and menu == True:
                play_y = 260
                select = pygame.mixer.Sound("source/audio/select.wav")
                select.set_volume(0.45)
                select.play()
        if event.type == pygame.KEYUP and menu == True:
            if event.key == pygame.K_RETURN:
                play_y = 250
                pygame.time.delay(150)
                Barrier.random_int = random.randint(-width, -50)
                Barrier.bpos_x = Barrier.random_int
                Barrier.bpos_rx = Barrier.bpos_x + Barrier.barrier_rect.right + 125
                menu = False

    #Controls
    keys = pygame.key.get_pressed()

    if keys[K_a] is True:
        velocity += 0.5
        player_x -= velocity
    elif keys[K_d] is True:
        velocity += 0.5
        player_x += velocity
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            velocity = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            velocity = 0
    if keys[pygame.K_ESCAPE] is True:
        state = False

    #Maximum Velocity
    gravity += 0.5
    player_y += gravity
    if gravity >= 20:
        gravity = 20
    if velocity >= 8:
        velocity = 8 

    #Screen Wrapping
    if player_x + player_rect.right <= 0:
        player_x = width + player_rect.x
    elif player_x + player_rect.left >= width:
        player_x = 0 - player_rect.right

    #Ceiling & Floor
    if (player_y + 50) >= height:
        gravity = -.5
        menu = True
        Barrier.bpos_y = -30
        Barrier.bpos_ry = -30
        player_y = 500

        death = pygame.mixer.Sound("source/audio/death.wav")
        death.set_volume(0.20)
        death.play()
        score = 0
        pygame.time.delay(800)
    if menu == True:
        gravity = -.5
    if player_y + player_rect.top <= 0:
        player_y = 0 - player_rect.top
        gravity = 0

    #Collision
    if player_y >= Barrier.bpos_y and player_y <= Barrier.bpos_y + Barrier.barrier_rect.bottom and player_x <= Barrier.bpos_x + Barrier.barrier_rect.right:
        menu = True
        Barrier.bpos_y = -30
        Barrier.bpos_ry = -30
        player_y = 500
        death = pygame.mixer.Sound("source/audio/death.wav")
        death.set_volume(0.20)
        death.play()
        score = 0
        pygame.time.delay(800)
    elif player_y >= Barrier.bpos_ry and player_y <= Barrier.bpos_y + Barrier.barrierr_rect.bottom and player_x + player_rect.right >= Barrier.bpos_rx:
        menu = True
        Barrier.bpos_y = -30
        Barrier.bpos_ry = -30
        player_y = 500

        death = pygame.mixer.Sound("source/audio/death.wav")
        death.set_volume(0.20)
        death.play()
        score = 0
        pygame.time.delay(800)

    #Title Bobbing
    if titlep_y > 485 and up == True:
        titlep_y -= 0.75
    else:
        titlep_y += 0.75
        up = False
    if titlep_y > 500:
        up = True

    #Draw
    screen.blit(background_surface, (0, 0))
    if menu == False:
        Barrier.bpos_y += 4
        Barrier.bpos_ry = Barrier.bpos_y
        screen.blit(player, (player_x, player_y))
        screen.blit(Barrier.barrier, (Barrier.bpos_x, Barrier.bpos_y))
        screen.blit(Barrier.barrier_r,(Barrier.bpos_rx, Barrier.bpos_ry))
        if Barrier.bpos_y >= height:
            Barrier(True)
            score+=1
            print(score)

    if score:
       white = (255, 255, 255)
       font = pygame.font.SysFont(None, 48)
       img = font.render(str(score), True, white)
       screen.blit(img, (20, 20))

    if menu == True:
        screen.blit(title, (title_x, title_y))
        screen.blit(title_p, (titlep_x, titlep_y))
        screen.blit(play, (play_x, play_y))

    pygame.display.update()
    clock.tick(60)

    # TODO
    # [] Add high score file, read from save.
    # [] Fix score font.
    # [] Add sprite animation for Dragon.
    # [] Add controls screen/ add controls to main menu.