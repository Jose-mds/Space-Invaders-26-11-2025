import pygame
from barriers import barrier
from bullets import bullet

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create barrier at position (100, 50)
barrier_groups = []

x_positions = [100, 250, 400, 550]  # positions of the 4 shields
y_position = 450  # distance from the bottom (adjust if needed)

for x in x_positions:
    group = barrier.create_barrier(x, y_position)
    barrier_groups.append(group)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    for group in barrier_groups:
        group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()