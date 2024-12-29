import pygame, random, time
pygame.init()

WIDTH = 1800
HEIGHT = 1200

screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load("Lesson 7/images/background.png")
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

score = 0
font = pygame.font.SysFont('comicsans', 40)
start = time.time()

class Bin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Lesson 7/images/bin.png")
        self.image = pygame.transform.scale(self.image,(125,125))
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


for i in range(50):
    x = random.randint(50,1750)
    y = random.randint(50, 1150)
    img = random.choice(images)
    recycle = Recycle(x, y, img)
    recyclegroup.add(recycle)

for i in range(30):
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
        if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                bin.rect.center = pos
    timegone = time.time()-start
    if timegone >= 16:
        if score > 30:
            screen.blit(bg,(0,0))
            text = font.render(f"Time Up!, You did well :) -- Your Score is:{score}",1, "Blue")
            screen.blit(text,(600,600))
        else:
            screen.blit(bg,(0,0))
            text = font.render(f"Time Up!, You didn't do that great :( -- Your Score is:{score}",1, "Blue")
            screen.blit(text,(600,600))
    else:
        screen.blit(bg,(0,0))
        text = font.render(f"Score:{score}",1, "White")
        screen.blit(text,(20,50))
        recyclehit = pygame.sprite.spritecollide(bin, recyclegroup, True)
        non_recyclehit = pygame.sprite.spritecollide(bin, non_recyclegroup, True)
        for item in recyclehit:
            score += 1
            text = font.render(f"Score:{score}",1, "White")
        for item in non_recyclehit:
            score -= 1
            text = font.render(f"Score:{score}",1, "White")
        bingroup.draw(screen)
        recyclegroup.draw(screen)
        non_recyclegroup.draw(screen)
    pygame.display.update()
