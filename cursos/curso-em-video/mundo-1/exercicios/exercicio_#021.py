# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time
from cores import AZUL_BOLD, LIMPAR

pygame.mixer.init()
pygame.mixer.music.load(r"c:\Users\Music\faahhhhhh.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)

print(f"{AZUL_BOLD}Áudio finalizado.{LIMPAR}") 