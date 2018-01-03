# Some Pygame Music 

import pygame
from pygame.locals import *
import os

pygame.init()

# This function will load an image from a file and convert it to a Pygame surface
# It also can convert the image to Alpha so "transparent" pixels won't be drawn to the screen
def load_image(file, mode = ''):
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if mode == 'A':   
        return surface.convert_alpha()
    else:
        return surface.convert()

# Simple button class, with a clicked and unclicked image and a position
class Button(pygame.sprite.Sprite):

    def __init__(self, img1, img2, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img1 = img1
        self.img2 = img2        
        self.image = self.img1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click_timer = 0

    # If the button is clicked it will change image    
    def got_clicked(self):
        self.image = self.img2
        self.click_timer = 25
    
    # After 25 frames the button will be change its image back to the original
    def update(self): 
        if self.click_timer > 0:
            self.click_timer -= 1
            if self.click_timer == 0:
                self.image = self.img1 

# Load some sound effect from wav-files
# The effect will be played when the Effect.play() function is called
effect1 = pygame.mixer.Sound('SoundEffects\cartoon1.wav')
effect2 = pygame.mixer.Sound('SoundEffects\cartoon2.wav')
effect3 = pygame.mixer.Sound('SoundEffects\cartoon3.wav')
effect4 = pygame.mixer.Sound('SoundEffects\cartoon4.wav')

# Load a music file, play it and immediatly pause it (so technically no music will be played now, button5 can start it)
pygame.mixer.music.load('Music\shine _like_a_star.mp3')
pygame.mixer.music.play()        
pygame.mixer.music.pause()
music_paused = True

screen_size = screen_width, screen_height = 640, 480

pygame.display.set_caption('Sound Blaster')

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

FPS = 60

# Lets make some Button object, and position them on the screen
button1 = Button(load_image('Graphics\\button1_1.png', 'A'), load_image('Graphics\\button1_2.png', 'A'), screen_width // 9, screen_height // 2)
button2 = Button(load_image('Graphics\\button2_1.png', 'A'), load_image('Graphics\\button2_2.png', 'A'), screen_width // 9 * 3, screen_height // 2)
button3 = Button(load_image('Graphics\\button3_1.png', 'A'), load_image('Graphics\\button3_2.png', 'A'), screen_width // 9 * 5, screen_height // 2)
button4 = Button(load_image('Graphics\\button4_1.png', 'A'), load_image('Graphics\\button4_2.png', 'A'), screen_width // 9 * 7, screen_height // 2)

# Make a Sprite-Group for these buttons
all_button = pygame.sprite.Group()
all_button.add(button1, button2, button3, button4)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            running = False

        # If the 1 - 4 button is pressed on the keyboard a sound effect will be played, and the corresponding Button object will also be pressed
        if event.type == pygame.KEYDOWN and event.key == K_1:
            button1.got_clicked()
            effect1.play()
        if event.type == pygame.KEYDOWN and event.key == K_2:
            button2.got_clicked()
            effect2.play()
        if event.type == pygame.KEYDOWN and event.key == K_3:
            button3.got_clicked()
            effect3.play()
        if event.type == pygame.KEYDOWN and event.key == K_4:
            button4.got_clicked()
            effect4.play()            
        # If the 5 key is pressed on the keyboard the music will be unpaused / paused according to its current state
        if event.type == pygame.KEYDOWN and event.key == K_5:
            if music_paused:
                pygame.mixer.music.unpause()
                music_paused = False
            else:
                pygame.mixer.music.pause()
                music_paused = True
        
        # Get all the pressed buttons on the mouse
        mouse_buttons = pygame.mouse.get_pressed()

        # Get the mouse's position
        mouse_pos = pygame.mouse.get_pos()

        # If the left button is clicked, and the mouse-cursor is on any Button object, it will get pressed and a sound effect will be played
        if mouse_buttons[0] and button1.rect.collidepoint(mouse_pos):
            button1.got_clicked()
            effect1.play()
        if mouse_buttons[0] and button2.rect.collidepoint(mouse_pos):
            button2.got_clicked()
            effect2.play()
        if mouse_buttons[0] and button3.rect.collidepoint(mouse_pos):
            button3.got_clicked()
            effect3.play()
        if mouse_buttons[0] and button4.rect.collidepoint(mouse_pos):
            button4.got_clicked()
            effect4.play()
    
    # Update the state of the buttons (they will "unpress" themselves after 25 frame)
    all_button.update()

    # Clear screen
    screen.fill((0, 0, 0)) 

    # Draw out the current state of the buttons
    all_button.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()