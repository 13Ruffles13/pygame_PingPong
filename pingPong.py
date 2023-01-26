import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#Main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Update window
    pygame.display.flip()
    clock.tick(60)