font = pygame.font.SysFont(None, 30)
def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))