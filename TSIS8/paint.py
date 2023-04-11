import pygame

pygame.init()
running = True

WINDOW_WIDTH, WINDOW_HEIGHT = (600, 500)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

color = BLUE
shape = 'line'

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('Paint by me')
screen.fill(BLACK)

width = 20

previous, current = None, None

while running:

    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if alt_pressed and pressed[pygame.K_b]:
                color = BLUE
            if alt_pressed and pressed[pygame.K_r]:
                color = RED
            if alt_pressed and pressed[pygame.K_g]:
                color = GREEN
            
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'


        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:
                previous = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                current = pygame.mouse.get_pos()
                if previous:
                    if shape == 'line':
                        pygame.draw.line(screen, color, previous, current, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, BLACK, previous, current, width)
                    previous = current
            if event.type == pygame.MOUSEBUTTONUP:
                previous = None
        else:

            if event.type == pygame.MOUSEBUTTONDOWN:
                previous = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                current = pygame.mouse.get_pos()
                if shape == 'circle':
                    x = (previous[0]+current[0])/2
                    y = (previous[1]+current[1])/2
                    rx = abs(previous[0]-current[0])/2
                    ry = abs(previous[1]-current[1])/2
                    r = (rx + ry)/2
                    pygame.draw.circle(screen, color, (x, y), r, width)
                if shape == 'rectangle':
                    x = min(previous[0], current[0])
                    y = min(previous[1], current[1])
                    lx = abs(previous[0]-current[0])
                    ly = abs(previous[1]-current[1])
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
    pygame.display.flip()
    clock.tick(fps)

