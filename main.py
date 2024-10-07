from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import self
from pygame import mixer

#Initialize the game
pygame.init()

#create screen
SCREENWIDTH = 800
SCREENHEIGHT = int(SCREENWIDTH * 0.8)
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))


#Title
pygame.display.set_caption("Screen Movement")


#music
#mixer.music.load('')
#mixer.music.play(-1)


#The player and objects
ufoImg = pygame.image.load('ufo.png')
playerX = 75
playerY = 350
move_speed = 1
player1 = pygame.Rect((75, 350, 50, 50))

def ufo():
    screen.blit(ufoImg,(400,400))

# Text
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#total number of rooms and floors
floor_amount = 5
room_amount = 5

#current floor and room the player starts at
current_floor = 1
current_room = 1

#12 different colors for rooms
colors = [
    (192,192,255),
    (192,255,192),
    (255,192,192),
    (255,255,192),
    (255,192,255),
    (192,255,255),
    (0,0,128),
    (0,128,0),
    (128,0,0),
    (128,128,0),
    (128,0,128),
    (0,128,128)
]

c = len(colors)

def show_floor(x,y):
    location_text = font.render("Floor: " + str(current_floor) + ", Room: " + str(current_room),True,(0,0,0))
    screen.blit(location_text, (x,y))

#GameLoop
run = True
while run:

    #depending on the room, the color changes (every 3 rooms and every 4 floors)
    if (current_room % 3 == 1) & (current_floor % 4 == 1):
        screen.fill(colors[0]) #light blue
    elif (current_room % 3 == 2) & (current_floor % 4 == 1):
        screen.fill(colors[1]) #light green
    elif (current_room % 3 == 0) & (current_floor % 4 == 1):
        screen.fill(colors[2]) #light red
    elif (current_room % 3 == 1) & (current_floor % 4 == 2):
        screen.fill(colors[3]) #light yellow
    elif (current_room % 3 == 2) & (current_floor % 4 == 2):
        screen.fill(colors[4]) #light magenta
    elif (current_room % 3 == 0) & (current_floor % 4 == 2):
        screen.fill(colors[5]) #light cyan
    elif (current_room % 3 == 1) & (current_floor % 4 == 3):
        screen.fill(colors[6]) #dark blue
    elif (current_room % 3 == 2) & (current_floor % 4 == 3):
        screen.fill(colors[7]) #dark green
    elif (current_room % 3 == 1) & (current_floor % 4 == 0):
        screen.fill(colors[9]) #dark yellow
    elif (current_room % 3 == 2) & (current_floor % 4 == 0):
        screen.fill(colors[10]) #dark magenta
    elif (current_room % 3 == 0) & (current_floor % 4 == 0):
        screen.fill(colors[11]) #dark cyan
    else:
        screen.fill(colors[8]) # dark red

    #checker effect which draws the ufo
    if ((current_room % 2 == 0) & (current_floor % 2 == 1) |
            (current_room % 2 == 1) & (current_floor % 2 == 0)):
        ufo()

    #draw the player
    pygame.draw.rect(screen, (0,255,0), player1)

    #Player  Movement
    key = pygame.key.get_pressed()

    if key[pygame.K_a] | key[pygame.K_LEFT] == True:
        player1.move_ip(-move_speed,0)
    elif key[pygame.K_d] | key[pygame.K_RIGHT] == True:
        player1.move_ip(move_speed, 0)
    elif key[pygame.K_w] | key[pygame.K_UP] == True:
        player1.move_ip(0, -1)
    elif key[pygame.K_s] | key[pygame.K_DOWN] == True:
        player1.move_ip(0, 1)

    # Move between rooms
    if player1.x > SCREENWIDTH - 60:
        if current_room < room_amount:
            player1.x = 10
            current_room += 1
        else:
            player1.x = SCREENWIDTH - 60
    elif player1.x < 10:
        if current_room > 1:
            player1.x = SCREENWIDTH - 60
            current_room -= 1
        else:
            player1.x = 10

    # Move between floors
    if player1.y < 1:
        if current_floor < floor_amount:
            player1.y = SCREENHEIGHT - 60
            current_floor += 1
        else:
            player1.y = 10
    elif player1.y > SCREENHEIGHT - 60:
        if current_floor > 1:
            player1.y = 60
            current_floor -= 1
        else:
            player1.y = SCREENHEIGHT - 60


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Display location
    show_floor(textX,textY)

    pygame.display.update()

pygame.quit()
