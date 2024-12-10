import pygame
from time import sleep

pygame.init()
okno = pygame.display.set_mode((500,500))
pygame.display.set_caption("haahaahahahahah")
run = True
x = 200
y = 200
vec = pygame.rect(300,250,x,y)

while run:

    pygame.draw.rect(okno,(255,0,0),vec)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    