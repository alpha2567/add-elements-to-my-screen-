import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 30)
text = font.render("Hello Codingal!", True, BLACK)
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (220, 170, 200, 100))
    screen.blit(text, (190, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()