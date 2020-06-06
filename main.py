from paddle import Paddle
from ball import Ball
import pygame
from random import randint

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
png_files = ["ad.png", "aw.png", "nb.png", "ss.png"]  # image files to be used as ball

size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

active = True

clock = pygame.time.Clock()

paddle_1 = Paddle(white, 10, 100)
paddle_1.rect.x = 20
paddle_1.rect.y = 250

paddle_2 = Paddle(white, 10, 100)
paddle_2.rect.x = 770
paddle_2.rect.y = 250

# ball = Ball(white, 10, 10)  alternative to image files
ball = Ball("Nb.png")
ball.rect.x = randint(350, 450)
ball.rect.y = randint(250, 350)

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle_1)
all_sprites.add(paddle_2)
all_sprites.add(ball)

score_1 = 0
score_2 = 0

if __name__ == "__main__":

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        key_stroke = pygame.key.get_pressed()
        if key_stroke[pygame.K_w]:
            paddle_1.move_up(5)
        if key_stroke[pygame.K_s]:
            paddle_1.move_down(5)
        if key_stroke[pygame.K_UP]:
            paddle_2.move_up(5)
        if key_stroke[pygame.K_DOWN]:
            paddle_2.move_down(5)

        all_sprites.update()

        if ball.rect.x >= 1200:
            score_1 += 1
        if ball.rect.x <= -400:
            score_2 += 1
        if ball.rect.x >= 1200 or ball.rect.x <= -400:
            ball.reset()
        if ball.rect.y >= 500:
            ball.speed[1] = -ball.speed[1]
        if ball.rect.y <= 0:
            ball.speed[1] = -ball.speed[1]

        if pygame.sprite.collide_mask(ball, paddle_1) or pygame.sprite.collide_mask(ball, paddle_2):
            ball.bounce()

        screen.fill(black)

        font = pygame.font.SysFont("Comicsans", 80)
        score_1_text = font.render(str(score_1), 1, white)
        screen.blit(score_1_text, (200, 10))
        score_2_text = font.render(str(score_2), 1, white)
        screen.blit(score_2_text, (600, 10))
        game_over_text = font.render("Game Over.", 1, white)
        if score_1 == 5 or score_2 == 5:
            ball.rect.x = 0
            ball.rect.y = 0
            screen.blit(game_over_text, (230, 300))

        pygame.draw.line(screen, white, [(width / 2), 0], [(width / 2), 600], 2)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

pygame.quit()
