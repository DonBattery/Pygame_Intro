# Basic Pygame Template 

# Import Pygame and its locals
import pygame
from pygame.locals import *
# Import OS for positioning the window
import os

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = screen_width, screen_height = 640, 480

# Set the window caption
pygame.display.set_caption('BadCat RULEZ')

# Tell the OS to display the window in the middle of the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Inicilaize the screen
screen = pygame.display.set_mode(screen_size)

# Inicialize game clock
clock = pygame.time.Clock()

# Set the frame per secound value
FPS = 60

# Main game loop
running = True
while running:
    # Get the pygame-events and handle them (for example closing the window, or pressing ESC will force the main loop to end)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False
    # Write game logic here :
 
    # Clear the screen before drawing
    screen.fill((180, 220, 71)) 
    # Write draw code here :
 
    # Update the screen with the drawn graphics
    pygame.display.flip()
    # Regulate the game speed to a given FPS
    clock.tick(FPS)
 
# Close the window and quit
pygame.quit()