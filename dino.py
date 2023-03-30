import pygame

class Dino(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load('dino.png').convert_alpha()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jump = False
        self.jump_height = 13
        self.gravity = 1

    def update(self):
        if self.jump:
            self.rect.y -= self.jump_height
            self.jump_height -= self.gravity

            if self.rect.y >= 190:  # The dino's original y-position
                self.rect.y = 190
                self.jump = False
                self.jump_height = 13

