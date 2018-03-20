# Imports
import pygame
import intersects
import random
import os

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Predicament Park"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 43)
GREY = (191, 191, 191)
YELLOW = (255, 209, 26)


#Fonts
GAME_FONT = pygame.font.Font(None, 50)

#Stages
START = 0
PLAYING = 1
END = 2
PAUSE = 3

# Make a block
block =  [40, 40, 40, 40]
vel = [0, 0]
speed = 3
score1 = 0
block_color = BLACK

#Lives in the game
lives = 5

#The white cards
IN_CARD = [0, 240, 800, 120]
OUT_CARD = [0, 240, 800, 120]
WIN_CARD = [0, 240, 800, 120]
DEATH_CARD = [0, 240, 800, 120]
SUICIDE_CARD = [0, 240, 800, 120]
PAUSE_CARD = [0, 240, 800, 120]
GREEN_CARD = [0, 0, 800, 600]
SCORE_CARD = [0, 60, 800, 70]

# make a wall
wall1 =  [0, 0, 40, 800]
wall2 =  [0, 0, 800, 40]
wall3 =  [0, 560, 800, 40]
wall4 =  [760, 0, 40, 420]
wall5 =  [40, 120, 40, 40]
wall6 =  [120, 40, 40, 40]
wall7 =  [340, 80, 80, 140]
wall8 =  [280, 220, 80, 80]
wall9 =  [380, 280, 80, 280]
wall10 =  [460, 400, 80, 80]
wall11 =  [460, 480, 20, 80]
wall12 =  [180, 460, 200, 100]
wall13a =  [100, 400, 100, 60]
#wall13b =  [40, 420, 60, 40]
wall14 =  [180, 320, 20, 80]
wall15 =  [40, 280, 80, 40]
wall16 =  [120, 160, 40, 160]
wall17 =  [160, 260, 40, 60]
#wall18 =  [200, 260, 80, 40]
wall19 =  [160, 120, 60, 40]
wall20 =  [220, 120, 20, 40]
wall21 =  [240, 80, 60, 80]
wall22 =  [280, 160, 20, 60]
wall23 =  [470, 80, 60, 140]
wall24 =  [580, 80, 140, 40]
wall25 =  [660, 120, 60, 140]
wall26a =  [580, 260, 20, 100]
wall26b =  [620, 280, 40, 80]
wall26c =  [660, 260, 60, 100]
wall26d = [600, 280, 20, 80]
#wall27 =  [500, 300, 80, 20]
wall28 =  [500, 260, 40, 40]
wall29 =  [580, 360, 60, 200]
wall30 =  [640, 460, 120, 20]
wall31 =  [680, 400, 80, 20]
wall32 =  [760, 460, 40, 120]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13a, wall14, wall15, wall16, wall17, wall19, wall20,
         wall21, wall22, wall23, wall24, wall25, wall26a, wall26b, wall26c, wall26d, wall28, wall29, wall30,
         wall31, wall32]

#the teleporting walls
t1 = [40, 240, 80, 40,  60, 320]
t2 = [40, 400, 60, 20, 480, 520]
t3 = [360, 220, 20, 80, 260, 420]
t4 = [200, 260, 80, 40, 640, 480]
t5 = [760, 420, 40, 40, 300, 180]
t6 = [500, 300, 80, 20, 720, 200]
t7 = [600, 260, 60, 20, 120, 460]
t8 = [40, 420, 60, 40, 500, 220]

teleports = [t1, t2, t3, t4, t5, t6, t7, t8]

#The making of the coins
coin1 = [740, 40, 20, 20]
coin2 = [620, 140, 20, 20]
coin3 = [420, 260, 20, 20]
coin4 = [360, 300, 20, 20]
coin5 = [240, 400, 20, 20]
coin6 = [200, 440, 20, 20]
coin7 = [140, 340, 20, 20]
coin8 = [60, 480, 20, 20]
coin9 = [120, 520, 20, 20]
coin10 = [40, 540, 20, 20]
coin11 = [360, 440, 20, 20]
coin12 = [200, 300, 20, 20]
coin13 = [560, 540, 20, 20]
coin14 = [540, 340, 20, 20]
coin15 = [720, 120, 20, 20]
coin16 = [540, 160, 20, 20]
coin17 = [40, 360, 20, 20]
coin18 = [100, 360, 20, 20]
coinEND= [720, 480, 40, 80]

#these coins take the life of the "block"
bitA = [140, 140, 20, 20]
bitB = [220, 100, 20, 20]
bitC = [360, 40, 20, 20]
bitD = [420, 140, 20, 20]
bitE = [540, 260, 20, 20]
bitF = [520, 480, 20, 20]

bit_coins = [bitA, bitB, bitC, bitD, bitE, bitF]

name = input("Whats your Player name? ")
#option = input("If you want to see the controls press O ")

#Add something to this and add to global and it restarts what you put in 
def setup():
    global block_pos, block_vel, size, stage, time_remaining, ticks, coins, bit_coins
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START
    time_remaining = 40
    ticks = 0
    
    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coinEND]
    bit_coins = [bitA, bitB, bitC, bitD, bitE, bitF]
    
#Varibles needed for the loop
win = False
timer_stuff = False
life = True
escape = False
ending = False


# Game loop
setup()

done = False

while not done:
    #Event processing (React to key presses, mouse clicks, etc.)


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            elif stage == END :
                if event.key == pygame.K_SPACE:
                    setup()
                    block[0] = 40
                    block[1] = 40
                    win = False
                    life = True
                    escape = False
                    score1 = 0
                    lives = 5

                    
            elif event.key == pygame.K_TAB:
                 stage = PAUSE
            elif event.key == pygame.K_x:
                 escape = True
            elif event.key == pygame.K_c:
                life = False
            elif event.key == pygame.K_7:
                win = True
            elif event.key == pygame.K_1:
                timer_stuff = True 

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_TAB:
                stage = PLAYING
                    
    state = pygame.key.get_pressed()
    
    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]
            


    if stage == PLAYING:
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
    
                    
    #Teleporting around the game board
    if block[0] == 60 and block[1] == 210:
        block[0] = (60)
        block[1] = (320)
    
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
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
        
        ''' resolve collisions'''
        for w in walls:
            if intersects.rect_rect(block, w):                    
                if vel[1] > 0:
                    block[1] = w[1] - block[3]
                if vel[1] < 0:
                    block[1] = w[1] + w[3]

        ''' ONLY TELEPORTER STUFF '''
        for t in teleports:
            rect = t[:4]
            if intersects.rect_rect(block, rect):
                block[0] = t[4]
                block[1] = t[5]

        ''' timer stuff '''
        if stage == PLAYING:
            ticks += 1

            if ticks % refresh_rate == 0:
                time_remaining -= 1

            if time_remaining == 0:
                timer_stuff = True
                
        '''the coins will get affected by the block here'''
        #how do i restart the coins 
        hit_list = []
            
        for c in coins:
            if intersects.rect_rect(block, c):
                hit_list.append(c)

        hit_list = [c for c in coins if intersects.rect_rect(block, c)]

        for hit in hit_list:
            coins.remove(hit)
            score1 += 2
        
        if len(coins) == 0:
            win = True

        '''this is the bad coins or bit_coins'''
        #this gives negative lives
        neg_list = []
            
        for bit in bit_coins:
            if intersects.rect_rect(block, bit):
                neg_list.append(bit)

        neg_list = [bit for bit in bit_coins if intersects.rect_rect(block, bit)]

        for neg in neg_list:
            bit_coins.remove(neg)
            lives -= 1
            score1 -= 1 

        if lives == 0:
            life = False
               
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(GREY)

    pygame.draw.rect(screen, block_color, block)

    #displays objects that the block will interact with
    for w in walls:
        pygame.draw.rect(screen, GREEN, w)
        
    for t in teleports:
       rectangle = t[:4]
       pygame.draw.rect(screen, GREEN, rectangle)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    for bit in bit_coins:
        pygame.draw.rect(screen, YELLOW, bit)

    #this displays stats of the game
    if stage == PLAYING:
        ''' timer text '''
        timer_text = GAME_FONT.render(str(time_remaining), True, WHITE)
        screen.blit(timer_text, [200, 5])

        '''The score text '''
        score_text = GAME_FONT.render(name + ": " + str(score1), True, WHITE)
        screen.blit(score_text, [300, 5])

        '''The life indicator'''
        life_text = GAME_FONT.render("Lives = " + str(lives), True, WHITE)
        screen.blit(life_text, [600, 5])
        
    #Coins that can't be reached and have no other purpose in the except to trick the player
    C1 = [160, 180, 20, 20]
    C2 = [200, 160, 20, 20]
    C3 = [240, 160, 20, 20]
    C4 = [240, 220, 20, 20]
    pygame.draw.rect(screen, YELLOW, C1)
    pygame.draw.rect(screen, YELLOW, C2)
    pygame.draw.rect(screen, YELLOW, C3)
    pygame.draw.rect(screen, YELLOW, C4)
                    
    ''' Game text actions '''
    #this display shows at every beginning of the game
    if stage == START:
        pygame.draw.rect(screen, GREEN, GREEN_CARD)
        pygame.draw.rect(screen, WHITE, IN_CARD)
        text1 = GAME_FONT.render("Player One! You must learn!", True, BLACK)
        text2 = GAME_FONT.render("(Press SPACE to test yourself!)", True, BLACK)
        screen.blit(text1, [180, 260])
        screen.blit(text2, [160, 300]) 
                                 
    #this display only shows when your time equals zero
    if time_remaining == 0:
        pygame.draw.rect(screen, GREEN, GREEN_CARD)
        pygame.draw.rect(screen, WHITE, OUT_CARD)
        pygame.draw.rect(screen, WHITE, SCORE_CARD)
        text1 = GAME_FONT.render("Time's up.", True, BLACK)
        text2 = GAME_FONT.render("(Press SPACE to start from the begining.)", True, BLACK)
        screen.blit(text1, [300, 270])
        screen.blit(text2, [70, 310])
        text3 = GAME_FONT.render(name + ": " + str(score1), True, BLACK)
        text4 = GAME_FONT.render("lives: " + str(lives), True, BLACK)
        text5 = GAME_FONT.render("Your time: " + str(time_remaining), True, BLACK)
        screen.blit(text3, [10, 80])
        screen.blit(text4, [300, 80])
        screen.blit(text5, [475, 80])
        stage = END
    #this display only shows when you have collected all the coins
    elif win == True:
        pygame.draw.rect(screen, GREEN, GREEN_CARD)
        pygame.draw.rect(screen, WHITE, WIN_CARD)
        pygame.draw.rect(screen, WHITE, SCORE_CARD)
        text1 = GAME_FONT.render("YOU'VE WON I'M SO HAPPY", 1, BLACK)
        text2 = GAME_FONT.render("(Press SPACE to find other ways.)", 1, BLACK)
        screen.blit(text1, [180, 270])
        screen.blit(text2, [140, 310])
        text3 = GAME_FONT.render(name + ": " + str(score1), True, BLACK)
        text4 = GAME_FONT.render("lives: " + str(lives), True, BLACK)
        text5 = GAME_FONT.render("Your time: " + str(time_remaining), True, BLACK)
        screen.blit(text3, [10, 80])
        screen.blit(text4, [300, 80])
        screen.blit(text5, [475, 80])
        stage = END
    #this display only shows when your total number of lives equals zero
    elif life == False:
        pygame.draw.rect(screen, GREEN, GREEN_CARD)
        pygame.draw.rect(screen, WHITE, DEATH_CARD)
        pygame.draw.rect(screen, WHITE, SCORE_CARD)
        text1 = GAME_FONT.render("Your life is done for", True, BLACK)
        text2 = GAME_FONT.render("(Press SPACE to be reborn!)", True, BLACK)
        screen.blit(text1, [260, 270])
        screen.blit(text2, [180, 310])
        text3 = GAME_FONT.render(name + ": " + str(score1), True, BLACK)
        text4 = GAME_FONT.render("lives: " + str(lives), True, BLACK)
        text5 = GAME_FONT.render("Your time: " + str(time_remaining), True, BLACK)
        screen.blit(text3, [10, 80])
        screen.blit(text4, [300, 80])
        screen.blit(text5, [475, 80])
        stage = END
    #this display only when X is pressed
    elif escape == True:
        pygame.draw.rect(screen, GREEN, GREEN_CARD)
        pygame.draw.rect(screen, WHITE, SUICIDE_CARD)
        pygame.draw.rect(screen, WHITE, SCORE_CARD)
        text1 = GAME_FONT.render("You messed up didn't you? It's alright though.", True, BLACK)
        text2 = GAME_FONT.render("(Just press SPACE to be forgiven.)", True, BLACK)
        screen.blit(text1, [30, 270])
        screen.blit(text2, [120, 310])
        text3 = GAME_FONT.render(name + ": " + str(score1), True, BLACK)
        text4 = GAME_FONT.render("lives: " + str(lives), True, BLACK)
        text5 = GAME_FONT.render("Your time: " + str(time_remaining), True, BLACK)
        screen.blit(text3, [10, 80])
        screen.blit(text4, [300, 80])
        screen.blit(text5, [475, 80])
        stage = END
    #this display only shows when the game is paused
    elif stage == PAUSE:
        pygame.draw.rect(screen, GREEN, GREEN_CARD)
        pygame.draw.rect(screen, WHITE, PAUSE_CARD)
        text1 = GAME_FONT.render("PAUSE", True, BLACK)
        text2 = GAME_FONT.render("(Release to RESUME)", True, BLACK)
        screen.blit(text1, [355, 270])
        screen.blit(text2, [230, 310])
        stage = PAUSE
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
