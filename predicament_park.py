# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Predicament Park"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 40


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

    
# Make a block
block =  [60, 60, 40, 40]
vel = [0, 0]
speed = 5

# make a wall
wall1 =  []
wall2 =  []
wall3 =  []
wall4 =  []
wall5 =  [40, 120, 40, 40]
wall6 =  [120, 40, 40, 40]
wall7 =  []
wall8 =  [280, 220, 100, 80]
wall9 =  [380, ]
wall10 =  [460, 400, 80, 80]
wall11 =  [460, 460, 20, 80]
wall12 =  [180, 460, 200, 100]
wall13 =  [40, 400, 160, 60]
wall14 =  [180, 320, 20, 80]
wall15 =  [40, 240, 80, 80]
wall16 =  [120, 160, 40, 40]
wall17 =  [160, 260, 40, 60]
wall18 =  [200, 260, 80, 80]
wall19 =  [160, 120, 60, 40]
wall20 =  [220, 120, 20, 40]
wall21 =  [240, 80, 60, 80]
wall22 =  [280, 160, 20, 60]
wall23 =  []
wall24 =  [580, 80, 120, 40]
wall25 =  [660, 120, 60, 140]
wall26 =  []
wall27 =  [500, 300, 80, 80]
wall28 =  [500, 260, 40, 40]
wall29 =  []
wall30 =  [640, 460, 20, 80]
wall31 =  [680, 400, 80, 20]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
         wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30,
         wall31]

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    if left:
        vel[0]  = -speed
    elif right:
        vel[0]  = speed
    else:
        vel[0]  = 0

    if up:
        vel[1] = -speed
    elif down:
        vel[1]  = speed
    else:
        vel[1]  = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block in horizontal direction '''
    block[0] += vel[0]

    ''' resolve collisions '''
    for w in walls:
        if intersects.rect_rect(block, w):        
            if vel[0]> 0:
                block[0] = w[0] - block[2]
            elif vel[0] < 0:
                block[0] = w[0] + w[2]

    ''' move the block in vertical direction '''
    block[1] += vel[1]
    
    ''' resolve collisions '''
    for w in walls:
        if intersects.rect_rect(block, w):                    
            if vel[1] > 0:
                block[1] = w[1] - block[3]
            if vel[1] < 0:
                block[1] = w[1] + w[3]

    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, block)

    for w in walls:
        pygame.draw.rect(screen, RED, w)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
