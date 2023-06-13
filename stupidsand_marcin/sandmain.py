import pygame
import random

# Initialize Pygame
pygame.init()

# Define the window size
width = 400
height = 300

# Define the border size
border_size = 20

# Calculate the inner window size
inner_width = width - (2 * border_size)
inner_height = height - (2 * border_size)

# Create the window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling ASCII Characters")

# Define the font and font size
font_size = 20
font = pygame.font.SysFont(None, font_size)

# Define the ASCII characters to display
ascii_characters = "#@$%&"

falling_characters = []

stationary_characters = []

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.random() < 0.1:
        character = random.choice(ascii_characters)
        x = random.randint(border_size, width - border_size - font_size)
        y = border_size
        falling_characters.append((character, x, y))

    for i in range(len(falling_characters)):
        character, x, y = falling_characters[i]
        y += font_size
        falling_characters[i] = (character, x, y)

        if y >= inner_height + border_size or any(
                (x == char_x and y == char_y) for _, char_x, char_y in stationary_characters):
            stationary_characters.append((character, x, y - font_size))
            falling_characters.pop(i)
            break

    window.fill((0, 0, 0))

    pygame.draw.rect(window, (255, 255, 255), (border_size, border_size, inner_width, inner_height), 2)

    for character, x, y in stationary_characters:
        text_surface = font.render(character, True, (255, 255, 255))
        window.blit(text_surface, (x, y))

    for character, x, y in falling_characters:
        text_surface = font.render(character, True, (255, 255, 255))
        window.blit(text_surface, (x, y))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
