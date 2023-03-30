import pygame
from dino import Dino
from cactus import Cactus
from ground import Ground
from os import sys
import numpy as np
class DinoEnv:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 300))
        pygame.display.set_caption("Google Dino Game with RL")
        self.clock = pygame.time.Clock()
        self.game_speed = 5
        self.dino = Dino(50, 190)
        self.cactus = Cactus(900, 215, self.game_speed)
        self.ground = Ground(0, 250, self.game_speed)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.dino)
        self.all_sprites.add(self.cactus)
        self.all_sprites.add(self.ground)

    def reset(self):
        self.game_speed = 5
        self.dino.rect.y = 190
        self.cactus.rect.x = 900
        return self.get_state()

    def get_state(self):
        dino_rect = self.dino.rect
        cactus_rect = self.cactus.rect
        distance_to_cactus = cactus_rect.left - dino_rect.right
        print(distance_to_cactus, self.dino.jump_height, self.game_speed)
        return np.array([distance_to_cactus, self.dino.jump_height, self.game_speed])


    def step(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.clock.tick(60)

        if action == 1:  # Jump action
            if not self.dino.jump:
                self.dino.jump = True

        self.game_speed += 0.001
        self.cactus.game_speed = self.game_speed
        self.ground.game_speed = self.game_speed
        self.all_sprites.update()

        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

        reward = 1
        done = False
        if pygame.sprite.collide_rect(self.dino, self.cactus):
            reward = -100
            done = True

        next_state = self.get_state()
        return next_state, reward, done


    def close(self):
        pygame.quit()
