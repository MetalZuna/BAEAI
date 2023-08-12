import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Snake settings
snake_pos = [400, 300]  # Starting position
snake_body = [[400, 300], [390, 300], [380, 300]]
direction = 'RIGHT'
change_to = direction
speed = 15

# Snake color
snake_color = (0, 255, 0)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Detect keystrokes
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    # Changing direction
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    
    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    # Remove the condition related to food_pos for now
    snake_body.pop()

        
    # Drawing the snake
    window.fill((0, 0, 0))  # Background color
    for pos in snake_body:
        pygame.draw.rect(window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    # Update the game display
    pygame.display.flip()
    clock.tick(speed)


# Quit Pygame
pygame.quit()
