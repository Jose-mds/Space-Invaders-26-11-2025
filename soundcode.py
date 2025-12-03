import pygame

pygame.mixer.init()

shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
alien_die_sound = pygame.mixer.Sound("sounds/explode.wav")
player_hit_sound = pygame.mixer.Sound("sounds/hit.wav")

def play_shoot():
    shoot_sound.play()

def play_alien_explode():
    alien_die_sound.play()

def play_player_hit():
    player_hit_sound.play()
