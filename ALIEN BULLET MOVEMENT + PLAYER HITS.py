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