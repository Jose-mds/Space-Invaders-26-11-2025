import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Requirement 2")

clock = pygame.time.Clock()

player_img = pygame.image.load("defender.png")
player_img = pygame.transform.scale(player_img, (50, 30))

alien_images = [
    pygame.image.load("invader1.png"),
    pygame.image.load("invader2.png"),
    pygame.image.load("invader3.png")
]

alien_images = [
    pygame.transform.scale(img, (40, 30))
    for img in alien_images
]

player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 5

lives = 3
respawn_cooldown = 0

player_bullets = []
bullet_speed = -7

aliens = []
for x in range(6):
    for y in range(3):
        img = alien_images[y % 3]
        rect = img.get_rect(topleft=(80 + x * 70, 80 + y * 60))
        aliens.append({"rect": rect, "img": img})

alien_bullets = []
alien_bullet_speed = 5
alien_shoot_chance = 1

font = pygame.font.SysFont(None, 30)
def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and respawn_cooldown == 0:
                bullet = pygame.Rect(player_x + 23, player_y, 4, 10)
                player_bullets.append(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    for bullet in player_bullets[:]:
        bullet.y += bullet_speed

        if bullet.y < 0:
            player_bullets.remove(bullet)

        for alien in aliens[:]:
            if bullet.colliderect(alien["rect"]):
                aliens.remove(alien)
                player_bullets.remove(bullet)
                break

    for alien in aliens:
        if random.randint(1, 1000) < alien_shoot_chance:
            rect = alien["rect"]
            alien_bullets.append(pygame.Rect(rect.x + 20, rect.y + 30, 4, 10))

    for bullet in alien_bullets[:]:
        bullet.y += alien_bullet_speed

        if bullet.y > HEIGHT:
            alien_bullets.remove(bullet)

        if respawn_cooldown == 0:
            player_rect = pygame.Rect(player_x, player_y, 50, 30)
            if bullet.colliderect(player_rect):
                lives -= 1
                respawn_cooldown = 60
                alien_bullets.remove(bullet)

    if respawn_cooldown > 0:
        respawn_cooldown -= 1

    if lives <= 0:
        draw_text("GAME OVER", WIDTH//2 - 80, HEIGHT//2)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    if respawn_cooldown % 10 < 5:
        screen.blit(player_img, (player_x, player_y))

    for alien in aliens:
        screen.blit(alien["img"], alien["rect"])

    for bullet in player_bullets:
        pygame.draw.rect(screen, (0, 255, 255), bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    draw_text(f"Lives: {lives}", 10, 10)

    pygame.display.update()
    clock.tick(60)