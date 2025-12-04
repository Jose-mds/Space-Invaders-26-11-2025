import pygame
import random
import sys
from barriers import make_barriers

pygame.init()

WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

#sounds
laser_sound = pygame.mixer.Sound("sounds/laser.wav")
laser_sound.set_volume(0.3)
hit_sound = pygame.mixer.Sound("sounds/hit.mp3")
hit_sound.set_volume(0.3)
pygame.mixer.music.load("sounds/bgmusic.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
game_over_sound = pygame.mixer.Sound("sounds/gameover.mp3")
game_over_sound.set_volume(0.2)

#PLAYER
player_img = pygame.image.load("images/defender.png")
player_img = pygame.transform.scale(player_img, (50, 30))

player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 7

player_bullets = []
player_bullet_speed = -7

lives = 3
respawn = 0


#ALIENS
alien_images = [
    pygame.transform.scale(pygame.image.load("images/invader1.png"), (40, 30)),
    pygame.transform.scale(pygame.image.load("images/invader2.png"), (40, 30)),
    pygame.transform.scale(pygame.image.load("images/invader3.png"), (40, 30)),
]

aliens = []
for x in range(6):
    for y in range(3):
        img = alien_images[y]
        rect = img.get_rect(topleft=(80 + x * 70, 80 + y * 60))
        aliens.append({"rect": rect, "img": img})

alien_direction = 1
alien_speed = 3
alien_drop = 20
alien_timer = 0
alien_cooldown = 3

#ALIEN BULLETS
alien_bullets = []
alien_bullet_speed = 5


#BARRIERS
barriers = make_barriers()


def draw_button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button colour change on hover
    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        colour = (180, 180, 180)
        if click[0] == 1:
            return True   # button clicked
    else:
        colour = (120, 120, 120)

    pygame.draw.rect(screen, colour, (x, y, w, h))
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + (w - label.get_width()) // 2,
                        y + (h - label.get_height()) // 2))
    return False

def reset_game():
    global player_x, player_y, lives, respawn_cooldown
    global player_bullets, alien_bullets, aliens

    player_x = WIDTH // 2
    player_y = HEIGHT - 80
    lives = 3
    respawn_cooldown = 0
    player_bullets = []
    alien_bullets = []
    barriers = make_barriers()

    # recreate aliens
    aliens = []
    for x in range(6):
        for y in range(3):
            img = alien_images[y % 3]
            rect = img.get_rect(topleft=(80 + x * 70, 80 + y * 60))
            aliens.append({"rect": rect, "img": img})

#TEXT
font = pygame.font.SysFont(None, 32)
def text(txt, x, y):
    img = font.render(txt, True, (255, 255, 255))
    screen.blit(img, (x, y))


#GAME LOOP
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and respawn == 0:
                bullet = pygame.Rect(player_x + 23, player_y, 4, 12)
                player_bullets.append(bullet)
                laser_sound.play()

    #PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    #PLAYER BULLETS AND COLLISIONS
    for bullet in player_bullets[:]:
        bullet.y += player_bullet_speed

        if bullet.y < 0:
            player_bullets.remove(bullet)
            continue

        # hit alien
        for alien in aliens[:]:
            if bullet.colliderect(alien["rect"]):
                player_bullets.remove(bullet)
                aliens.remove(alien)
                hit_sound.play()
                break
                

        # hit barrier
        for block in barriers:
            if bullet.colliderect(block.rect):
                try:
                    player_bullets.remove(bullet)
                except:
                    pass
                barriers.remove(block)
                break

    #ALIEN MOVEMENT
    alien_timer += 1
    if alien_timer >= alien_cooldown:
        alien_timer = 0

        # check edges
        hit_edge = False
        for alien in aliens:
            if alien["rect"].right >= WIDTH - 10 and alien_direction == 1:
                hit_edge = True
            if alien["rect"].left <= 10 and alien_direction == -1:
                hit_edge = True

        if hit_edge:
            alien_direction *= -1
            for alien in aliens:
                alien["rect"].y += alien_drop
            alien_cooldown = max(5, alien_cooldown - 2)
        else:
            for alien in aliens:
                alien["rect"].x += alien_direction * alien_speed

    #ALIEN SHOOTING
    columns = {}
    for alien in aliens:
        col = alien["rect"].x // 70
        if col not in columns or alien["rect"].y > columns[col]["rect"].y:
            columns[col] = alien

    for alien in columns.values():
        if random.randint(1, 150) == 1:
            rect = alien["rect"]
            alien_bullets.append(pygame.Rect(rect.x + 20, rect.y + 30, 4, 12))
            laser_sound.play()

    #ALIEN BULLETS COLLISIONS
    for bullet in alien_bullets[:]:
        bullet.y += alien_bullet_speed

        if bullet.y > HEIGHT:
            alien_bullets.remove(bullet)
            continue

        # hit barriers
        for block in barriers:
            if bullet.colliderect(block.rect):
                alien_bullets.remove(bullet)
                barriers.remove(block)
                break

        # hit player
        if respawn == 0:
            player_rect = pygame.Rect(player_x, player_y, 50, 30)
            if bullet.colliderect(player_rect):
                lives -= 1
                respawn = 60
                alien_bullets.remove(bullet)
                hit_sound.play()

    if respawn > 0:
        respawn -= 1

    #GAME OVER
    if lives <= 0:
        screen.fill((0, 0, 0))
        text("GAME OVER", WIDTH//2 - 90, HEIGHT//2 - 40)
        game_over_sound.play()

        if draw_button("TRY AGAIN", WIDTH//2 - 100, HEIGHT//2 + 20, 200, 50):
            reset_game()
            barriers = make_barriers()

        pygame.display.update()
        continue

    #WIN
    if len(aliens) == 0:
        screen.fill((0, 0, 0))
        text("YOU WIN!", WIDTH//2 - 70, HEIGHT//2 - 40)
        game_over_sound.play()

        if draw_button("PLAY AGAIN", WIDTH//2 - 100, HEIGHT//2 + 20, 200, 50):
            reset_game()
            barriers = make_barriers()

        pygame.display.update()
        continue

    #DRAW
    if respawn % 10 < 5:
        screen.blit(player_img, (player_x, player_y))

    for alien in aliens:
        screen.blit(alien["img"], alien["rect"])

    for bullet in player_bullets:
        pygame.draw.rect(screen, (0, 255, 255), bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    barriers.draw(screen)
    

    text(f"Lives: {lives}", 10, 10)

    pygame.display.update()
    clock.tick(60)
