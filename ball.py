import pygame
from random import randint, choice
black = (0, 0, 0)
png_files = ["ad.png", "aw.png", "nb.png", "ss.png"]


class Ball(pygame.sprite.Sprite):

    def __init__(self, file):
        super().__init__()

        self.image = pygame.image.load(file)
        self.image.set_colorkey(black)

        self.speed = [randint(4, 8), randint(-6, 6)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = randint(-4, 4)
        self.image = pygame.image.load(choice(png_files))  # ball image changes with each bounce

    def reset(self):
        self.rect.x = 350
        self.rect.y = 280







