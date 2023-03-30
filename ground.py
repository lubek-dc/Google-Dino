import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, game_speed):
        super().__init__()
        image = pygame.image.load('ground.png').convert_alpha()
        self.image = pygame.transform.scale(image, (1600, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game_speed = game_speed

    def update(self):
        self.rect.x -= self.game_speed

        if self.rect.x < -self.rect.width:
            self.rect.x = 0
