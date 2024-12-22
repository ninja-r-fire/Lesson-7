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
        self.image = pygame.transform.scale(self.image,(100,12))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

class Recycle(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = x, y


class Non_Recycle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Lesson 7/images/bag.png")
        self.image = pygame.transform.scale(self.image,(60,61))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

non_recyclegroup = pygame.sprite.Group()
recyclegroup = pygame.sprite.Group()

images = ["Lesson 7/images/pencil.png", "Lesson 7/images/cardboardbag.png", "Lesson 7/images/box.png"]


for i in range(200):
    x = random.randint(50,1750)
    y = random.randint(50, 1150)
    img = random.choice(images)
    recycle = Recycle(x, y, img)
    recyclegroup.add(recycle)

for i in range(100):
    x = random.randint(50,1750)
    y = random.randint(50, 1150)
    non_recycle = Non_Recycle(x, y)
    non_recyclegroup.add(non_recycle)


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
    recyclegroup.draw(screen)
    non_recyclegroup.draw(screen)
    pygame.display.update()
