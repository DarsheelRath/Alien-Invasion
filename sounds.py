import pygame
from time import sleep
class Sounds:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
    def bullet_noise(self):
        """Plays the bullet noise"""
        m = True
        while m:
            
            pygame.mixer.music.load('/Users/darsheelrath/Documents/Coding/alien_invasion/sounds/bullet_shot.wav')
            pygame.mixer.music.play()
            
            break
    def collide_noise(self):
        """Plays the collision noise"""
        m = True
        while m:
            
            pygame.mixer.music.load('/Users/darsheelrath/Documents/Coding/alien_invasion/sounds/alien_collided.wav')
            pygame.mixer.music.play()
            
            break

