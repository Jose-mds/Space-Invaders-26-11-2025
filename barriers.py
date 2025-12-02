import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, 8))   
        self.image.fill((255, 0, 0))        
        self.rect = self.image.get_rect(topleft=(x, y))



shape = [
"  xxxxxxx",
" xxxxxxxxx",
"xxxxxxxxxxx",
"xxxxxxxxxxx",
"xxxxxxxxxxx",
"xxx     xxx",
"xx       xx"
]



def make_barriers():
    barriers = pygame.sprite.Group()

 
    barrier_x_positions = [60, 260, 460, 660]
    barrier_y = 450  

    for bx in barrier_x_positions:
        for row_index, row in enumerate(shape):
            for col_index, char in enumerate(row):
                if char == "x":
                    x = bx + col_index * 8
                    y = barrier_y + row_index * 8
                    block = Block(x, y)
                    barriers.add(block)

    return barriers
