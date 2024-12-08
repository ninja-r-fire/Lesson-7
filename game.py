import pygame, random
pygame.init()

WIDTH = 1800
HEIGHT = 1200

screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load("Lesson 7/images/background.png")
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

class Bin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Lesson 7/images/bin.png")
        self.image = pygame.transform.scale(self.image,(100,120))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

bin = Bin(WIDTH/2, HEIGHT/2)
bingroup = pygame.sprite.Group()
bingroup.add(bin)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.blit(bg,(0,0))
    bingroup.draw(screen)
    pygame.display.update()