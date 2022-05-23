import pygame
from window import width

title = pygame.image.load('source/graphics/title.png').convert_alpha()
title_scale = x, y = 490, 100
title = pygame.transform.scale(title, title_scale)
title_rect = title.get_rect()
title_pos = title_x, title_y = (50, 100)

play = pygame.image.load('source/graphics/play.png').convert_alpha()
play_scale = play_x, play_y = 240, 70
play = pygame.transform.scale(play, play_scale)
play_rect = play.get_rect()
play_pos = play_x, play_y = ((width/2 - play_rect.right/2), 250)

title_p = pygame.image.load('source/graphics/title_dragon.png').convert_alpha()
titlep_scale = titlep_x, titlep_y = 190, 160
title_p = pygame.transform.scale(title_p, titlep_scale)
titlep_rect = title_p.get_rect()
titlep_pos = titlep_x, titlep_y = ((width/2 - titlep_rect.right/2), 500)