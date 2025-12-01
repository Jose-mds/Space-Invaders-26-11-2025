import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

class BarrierShape:
    def __init__(self, shape, block_size = 8, color = (0, 200, 0)):
        self.shape = shape
        self.block_size = block_size
        self.color = color

    def create_barrier(self, x_offset = 0, y_offset = 0):
        group = pygame.sprite.Group()

        for row_index, row in enumerate(self.shape):
            for col_index, char in enumerate(row):
                if char == "x":
                    x = x_offset + col_index * self.block_size
                    y = y_offset + row_index * self.block_size

                    block = Block(self.block_size, self.color, x, y)
                    group.add(block)

        return group

shape = [
    "  xxxxxxx",
    " xxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxx     xxx",
    "xx       xx"
]

barrier = BarrierShape(shape)