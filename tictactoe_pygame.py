import pygame

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((300, 400))
clock = pygame.time.Clock()
running = True

# create title text 
font = pygame.font.Font(None, 32)
title = font.render('TIC TAC TOE', True, 'white')
title_rect = title.get_rect()
title_rect.center = (150,20)

def draw_grid() : 
    pygame.draw.line(screen, 'white', (100, 100), (100,400),5)
    pygame.draw.line(screen, 'white', (200, 100), (200,400),5)
    pygame.draw.line(screen, 'white', (0, 200), (400,200),5)
    pygame.draw.line(screen, 'white', (0, 300), (400,300),5)

while running:
    
    # set window caption
    pygame.display.set_caption('TIC TAC TOE')

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Black")

    # constant elements
    draw_grid()
    screen.blit(title, title_rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)  

pygame.quit()