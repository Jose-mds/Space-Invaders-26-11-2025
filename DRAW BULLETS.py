    for bullet in player_bullets:
        pygame.draw.rect(screen, (0, 255, 255), bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    draw_text(f"Lives: {lives}", 10, 10)