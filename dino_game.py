import pygame
from dino import Dino
from cactus import Cactus
from ground import Ground

pygame.init()
screen = pygame.display.set_mode((800, 300))

pygame.display.set_caption("Google Dino Game")

clock = pygame.time.Clock()
running = True
game_speed = 5

dino = Dino(50, 190)
cactus = Cactus(900, 215, game_speed)
ground = Ground(0, 250, game_speed)

all_sprites = pygame.sprite.Group()
all_sprites.add(dino)
all_sprites.add(cactus)
all_sprites.add(ground)

while running:
    clock.tick(60)

    game_speed += 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino.jump:
                dino.jump = True
    cactus.game_speed = game_speed
    ground.game_speed = game_speed

    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

    if pygame.sprite.collide_rect(dino, cactus):
        running = False

pygame.quit()
