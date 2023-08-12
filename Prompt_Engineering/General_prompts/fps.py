import pygame
import sys
import random

global ENEMY_SPEED  # Declare ENEMY_SPEED as global at the start of the program
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5
JUMP_HEIGHT = 15  # Increase the jump height

# Bullet properties
BULLET_WIDTH = 10
BULLET_HEIGHT = 20
BULLET_COLOR = (255, 255, 255)
BULLET_SPEED = 10

# Enemy properties
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_SPEED = 2  # This is a global variable

# Game over image
GAME_OVER_IMAGE = 'assets/gb.png'

# Game properties
GRAVITY = 1
ENEMY_INCREMENT = 0.1  # Speed increment for each killed enemy

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/cow.png')
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        self.speed_y = 0
        self.jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.jumping:
            self.speed_y = -JUMP_HEIGHT
            self.jumping = True
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        self.speed_y += GRAVITY
        self.rect.y += self.speed_y

        if self.rect.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT
            self.jumping = False

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BULLET_WIDTH, BULLET_HEIGHT])
        self.image.fill(BULLET_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x + PLAYER_WIDTH  # Ensure the bullet is shot from the player's position
        self.rect.y = y

    def update(self):
        self.rect.x += BULLET_SPEED
        if self.rect.x > SCREEN_WIDTH:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    speed = 2  # Class variable for enemy speed

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/ali.png')
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - ENEMY_HEIGHT

    def update(self):
        self.rect.x -= Enemy.speed  # Use Enemy.speed
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
            Enemy.speed += ENEMY_INCREMENT  # Increase enemy speed each time an enemy goes off-screen

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.x, player.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)

    all_sprites.update()



    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        # No need to modify Enemy.speed here; it's handled in the Enemy class

    if pygame.sprite.spritecollide(player, enemies, False):
        player.image = pygame.image.load(GAME_OVER_IMAGE)  # Change player image to game over image
        player.image = pygame.transform.scale(player.image, (PLAYER_WIDTH, PLAYER_HEIGHT))  # Scale the image
        pygame.display.flip()
        pygame.time.wait(5000)  # Wait for 5 seconds
        break
    
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
