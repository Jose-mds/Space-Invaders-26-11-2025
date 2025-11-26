aliens = []
for x in range(6):
    for y in range(3):
        img = alien_images[y % 3]
        rect = img.get_rect(topleft=(80 + x * 70, 80 + y * 60))
        aliens.append({"rect": rect, "img": img})