import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#Main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game Shapes
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30) #Middle of the screen
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opp = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opp)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    #Update window
    pygame.display.flip()
    clock.tick(60) #Frames per-second