def restart_game():
    """Simple reset function"""
    main()  # restart the whole game


def show_end_screen(message):
    screen.fill((0, 0, 0))
    text(message, WIDTH // 2 - 80, HEIGHT // 2 - 40)
    text("PRESS ENTER TO RESTART", WIDTH // 2 - 170, HEIGHT // 2 + 10)
    text("PRESS ESC TO QUIT", WIDTH // 2 - 140, HEIGHT // 2 + 50)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart_game()
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
