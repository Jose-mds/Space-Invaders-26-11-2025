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