import pygame
import time
from pygame.locals import *

display_width = 500
display_height = 500

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((display_width,display_height))
        self.surface.fill((255,255,5))
        self.snake = Snake(self.surface)
        self.snake.draw()


    def run(self):
        running = True
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)


class Snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = int(display_width/2)
        self.y = int(display_height/2)
        self.direction = "up"

    def walk(self):
        if self.direction == "up":
            self.move_up()
        if self.direction == "down":
            self.move_down()
        if self.direction == "left":
            self.move_left()
        if self.direction == "right":
            self.move_right()

        self.draw()

    def draw(self):
        self.parent_screen.blit(self.block,(self.x, self.y))
        self.parent_screen.fill((255,255,5))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()
        self.direction = "left"

    def move_right(self):
        self.x += 10
        self.draw()
        self.direction = "right"

    def move_up(self):
        self.y -= 10
        self.draw()
        self.direction = "up"

    def move_down(self):
        self.y += 10
        self.draw()
        self.direction = "down"

    

if __name__ == "__main__":
    game = Game()
    game.run()

    


    