import sys
from time import sleep
import pygame

def print_lyrics():
    lines = [
        ("My granny called, she said, Travvy, you work too hard", 0.02),
        ("I'm worried you forget about me", 0.03),
        ("I'm falling in and out of clouds, don't worry, I'ma get it, granny, uh", 0.09),
        ("What happened? Now my daddy happy, mama called me up", 0.06),
        ("That money coming and she love me, I done made it now", 0.08),
        ("I done found life's meaning now", 0.88)  
    ]

    delays = [0, 0.4, 0.3, 0.3, 0.4, 0.3]  # Intervalos entre cada frase

    pygame.mixer.init()
    pygame.mixer.music.load("90210.mp3")
    pygame.mixer.music.play()

    sleep(2)  # Aguarda 2 segundos antes de começar a exibir a letra

    for i, (line, char_delay) in enumerate(lines):
        start_time = pygame.mixer.music.get_pos() / 1000  # Obtém o tempo atual da música em segundos
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        if i < len(delays):
            sleep(delays[i])  # Aguarda o intervalo específico após cada frase
        print('')

        # Calcula o tempo de espera até o próximo início de linha
        end_time = pygame.mixer.music.get_pos() / 1000
        wait_time = start_time + char_delay - end_time
        if wait_time > 0:
            sleep(wait_time)

    pygame.mixer.music.stop()

print_lyrics()
