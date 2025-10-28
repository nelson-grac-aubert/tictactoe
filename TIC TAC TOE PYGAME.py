import pygame

from sys import exit # import the exit() method to stop running code and not stay stuck in the while True loop 

pygame.init()

game_title_font = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((300, 400))

game_title_surface = game_title_font.render("TIC TAC TOE", False, 'White') #('Text you want to display', anti-aliasing, 'color')

while True : 

    for event in pygame.event.get() : # all the possible events that are matched to player inputs 
        if event.type == pygame.QUIT : # if click on red cross to close window 
            pygame.quit() # polar oposite on pygame.init()
            exit()

    screen.blit(game_title_surface, (100,50))