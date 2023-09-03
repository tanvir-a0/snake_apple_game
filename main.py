import pygame
import time
from pygame.locals import *


def draw_block():
    #surface.fill((255,255,5))
    surface.blit(block,(block_x,block_y))
    pygame.display.update()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500,500))
    surface.fill((255,255,5))
    
    block = pygame.image.load("resources/block.jpg").convert()
    block_x =  100
    block_y =  100
    surface.blit(block,(block_x, block_y))
    
    pygame.display.flip() #that means we are kinda uploading our screen with


    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_x = block_x
                    block_y = block_y - 10

                if event.key == K_DOWN:
                    block_x = block_x
                    block_y = block_y + 10

                if event.key == K_LEFT:
                    block_x = block_x - 10
                    block_y = block_y

                if event.key == K_RIGHT:
                    block_x = block_x + 10 
                    block_y = block_y

                draw_block()

            elif event.type == QUIT:
                running = False

            pass


    