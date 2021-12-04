import sys,time
import random

import pygame
from pygame. locals import QUIT

WINDOWS_WIDTH = 799
WINDOWS_HIGHT = 584
Gamer_coordinate = [405,80]
Clock = pygame.time.Clock()

def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HIGHT))
    pygame.display.set_caption("Gold miner")

    background = pygame.image.load("image/back.png").convert()
    player_gamer = pygame.image.load("image/clip.png").convert()
    screen.blit(background,[0, 0])

    angle = 0
    clip_turn = 0

    w, h = player_gamer.get_size()

    while True:
        Clock.tick(120)
        pygame.display.flip()
        if angle < 55 and clip_turn == 1:
            angle += 1
        if angle > -55 and clip_turn ==0:
            angle -= 1
        if angle == 55:
            clip_turn = 0
        if angle == -55:
            clip_turn =1

        screen.blit(background, [0, 0])
        blitRotate(screen, player_gamer, Gamer_coordinate, (w / 2, h / 2), angle)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()



















if __name__ =='__main__':
    main()