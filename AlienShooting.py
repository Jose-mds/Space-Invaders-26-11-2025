    for alien in aliens:
        if random.randint(1, 1000) < alien_shoot_chance:
            rect = alien["rect"]
            alien_bullets.append(pygame.Rect(rect.x + 20, rect.y + 30, 4, 10))