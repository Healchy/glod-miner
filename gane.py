import sys,time
import random

import pygame
from pygame. locals import QUIT

WINDOWS_WIDTH = 799
WINDOWS_HIGHT = 584
Gamer_coordinate = [385,80]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HIGHT))
    pygame.display.set_caption("Gold miner")

    background = pygame.image.load("image/back.png").convert()
    player_gamer = pygame.image.load("image/clip.png").convert()
    screen.blit(background,[0, 0])
    screen.blit(player_gamer, Gamer_coordinate)
    angle = 0

    pygame.display.flip()
    while True:
        angle += 0.05
        pygame.transform.rotate(player_gamer,angle)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


    pygame.display.update()


















if __name__ =='__main__':
    main()