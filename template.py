import pygame
import sys

screen1=pygame.display.set_mode((700,700))
pygame.display.set_caption("New1")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()