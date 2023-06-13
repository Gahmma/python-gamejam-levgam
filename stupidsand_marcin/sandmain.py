import pygame
import random


pygame.init()


width = 400
height = 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("")

font_size = 20
font = pygame.font.SysFont(None, font_size)

ascii_characters = "#@$%&"

falling_characters = []

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.random() < 0.1:
        character = random.choice(ascii_characters)
        x = random.randint(0, width - font_size)
        y = 0
        falling_characters.append((character, x, y))

    for i in range(len(falling_characters)):
        character, x, y = falling_characters[i]
        y += font_size
        falling_characters[i] = (character, x, y)

    window.fill((0, 0, 0))

    for character, x, y in falling_characters:
        text_surface = font.render(character, True, (255, 255, 255))
        window.blit(text_surface, (x, y))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()



