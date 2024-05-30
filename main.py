import pygame
import os

pygame.init()

WIDTH = 900
HEIGHT = 500
vel = 5

gun_sound1 = pygame.mixer.Sound('g.mp3')
gun_sound2 = pygame.mixer.Sound('g2.mp3')

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("An Inspiration game")
clock = pygame.time.Clock()

red_bullets = []
yellow_bullets = []
BULLET_VEL = 7

SIZE_01 = 70
SIZE_02 = 70
bg = pygame.image.load("bg.png")

SPACESHIP_RED = pygame.image.load(os.path.join("spaceship_red.png"))
RED = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_RED, (SIZE_01, SIZE_02)), 90)

SPACESHIP_BLACK = pygame.image.load(os.path.join("aircraft.png"))
BLACK = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_BLACK, (SIZE_01, SIZE_02)), 270)

def bullets_movement(yellow_bullets, red_bullets, red, black):
    bullet_to_remove = []

    for bullet in yellow_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            bullet_to_remove.append(bullet)
    
    for bullet in bullet_to_remove:
        yellow_bullets.remove(bullet)
    bullet_to_remove.clear()

    for bullet in red_bullets:
        bullet.x += BULLET_VEL
        if black.colliderect(bullet):
            bullet_to_remove.append(bullet)
    
    for bullet in bullet_to_remove:
        red_bullets.remove(bullet)

def game_Window(yellow_bullets, red_bullets, black, red):
    WIN.blit(bg, (0, 0))
    WIN.blit(RED, (red.x, red.y))
    WIN.blit(BLACK, (black.x, black.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)

    pygame.display.update()

def spaceship_red_movement(keys, red):
    if keys[pygame.K_a] and red.x > vel:
        red.x -= vel
    if keys[pygame.K_d] and red.x < WIDTH - SIZE_01 - vel:
        red.x += vel
    if keys[pygame.K_w] and red.y > vel:
        red.y -= vel
    if keys[pygame.K_s] and red.y < HEIGHT - SIZE_02 - vel:
        red.y += vel
    
def spaceship_black_movement(keys, black):
    if keys[pygame.K_LEFT] and black.x > vel:
        black.x -= vel
    if keys[pygame.K_RIGHT] and black.x < WIDTH - SIZE_01 - vel:
        black.x += vel
    if keys[pygame.K_UP] and black.y > vel:
        black.y -= vel
    if keys[pygame.K_DOWN] and black.y < HEIGHT - SIZE_02 - vel:
        black.y += vel

def main():
    black = pygame.Rect(700, 100, SIZE_01, SIZE_02)
    red = pygame.Rect(300, 100, SIZE_01, SIZE_02)
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    gun_sound1.play()

                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(black.x + black.width, black.y + black.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    gun_sound2.play()
                
        keys = pygame.key.get_pressed()

        spaceship_black_movement(keys, black)
        spaceship_red_movement(keys, red)
        bullets_movement(yellow_bullets, red_bullets, red, black)
        game_Window(yellow_bullets, red_bullets, black, red)

    pygame.quit()

if __name__ == "__main__":
    main()
