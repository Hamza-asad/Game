#Task 15
#Task name: mygame.py
#Written by: Hamza Asad
#Date: 2020/02/20

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Imports generate random numbers. 

# Initialize the pygame modules to get everything started.
pygame.init() 

# The screen that will be created needs a width and a height.
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height)) 

# This creates the player and gives it the image found in this folder. 
player = pygame.image.load("player.jpg")
enemy = pygame.image.load("enemy.png")
enemy1 = pygame.image.load("enemy.png")
monster = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (this is done so that the characters are kept within the screen boundary)
#Player height and width
player_height = player.get_height()
player_width = player.get_width()
#enemy height and width
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
#Enemy1 height and width
enemy1_height = enemy.get_height()
enemy1_width = enemy.get_width()
#monster height and width
monster_height = monster.get_height()
monster_width = monster.get_width()
#prize height and width
prize_height = prize.get_height()
prize_width = prize.get_width()

#prints out the height and width of each images
#Player
print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))
#Enemy 
print("This is the height of the enemy image: " +str(enemy_height))
print("This is the width of the enemy image: " +str(enemy_width))
#enemy1
print("This is the height of the enemy image: " +str(enemy1_height))
print("This is the width of the enemy image: " +str(enemy1_width))
#monster
print("This is the height of the monster image: "+str(monster_height))
print("This is the width of the monster image: " +str(monster_width))
#prize
print("This is the height of the prize image: " +str(prize_height))
print("This is the width of the prize image: " +str(prize_width))

# Store the positions of the player, enemy, monster and prize as variables.
player_x_pos = 100
player_y_pos = 50
# Make the enemy start off screen and at a random y position.
enemy_x_pos =  screen_width
enemy_y_pos =  random.randint(0, screen_height - enemy_height)
#add another enemy
enemy1_x_pos = screen_width
enemy1_y_pos = random.randint(0, screen_height - enemy_height)
#make the monster start off at a random y position
monster_x_pos = screen_width
monster_y_pos = random.randint(0, screen_height - monster_height)
#make the prize start off from a random y position
prize_x_pos = screen_width
prize_y_pos = random.randint(0,screen_height - enemy_height)

# This checks if the up or down key is pressed.
# make these keys a Boolean so it can be used to move the player.
key_up = False
key_down = False
key_left= False
key_right = False

# This is the game loop.
# You need to refresh/update the screen window and apply changes to represent real time game play. 
# Use the while loop 
while 1:

# Clears the screen.
    screen.fill(0) 
    # This draws the player, enemy, monster, and prize image to the screen at the postion specfied.
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy1, (enemy1_x_pos, enemy1_y_pos))
    screen.blit(monster, (monster_x_pos, monster_y_pos))
    screen.blit(prize, (prize_x_pos, prize_y_pos))
    
    # This updates the screen.
    pygame.display.flip()
    
    # This loops through events in the game.
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user presses down a key
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                key_up = True
            if event.key == pygame.K_DOWN:
                key_down = True
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_RIGHT:
                key_right = True

        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                key_up = False
            if event.key == pygame.K_DOWN:
                key_down = False
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False
            
    # check key pressed values and move player accordingly.
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if key_up == True:
        if player_y_pos > 0 : # This makes sure that the user does not move the player above the window.
            player_y_pos -= 2
    if key_down == True:
        if player_y_pos < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            player_y_pos += 2
    if key_left == True:
        if player_x_pos > 0 :
            player_x_pos -= 2
    if key_right == True:
        if player_x_pos < screen_width - player_width:
            player_x_pos +=2
    
    # To do this we need bounding boxes around the images of the player,prize and enemy.
    # Bounding box for the player:
    player_box = pygame.Rect(player.get_rect())
    player_box.top = player_y_pos
    player_box.left = player_x_pos
    
    #Bounding box for the enemy:
    enemy_box = pygame.Rect(enemy.get_rect())
    enemy_box.top = enemy_y_pos
    enemy_box.left = enemy_x_pos

    #bounding box for the 2nd enemy 
    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy1_box.top = enemy1_y_pos
    enemy1_box.left = enemy1_x_pos

    # bounding box for the monster
    monster_box = pygame.Rect(monster.get_rect())
    monster_box.top = monster_y_pos
    monster_box.left = monster_x_pos

    #bounding box for prize
    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prize_y_pos
    prize_box.left = prize_x_pos

    #Test collision of the boxes:
    if player_box.colliderect(enemy_box):
        print("You lose!")
        pygame.quit()
        exit(0)

    #Test collision of the monster:
    if player_box.colliderect(monster_box):
        print("You lose!")
        pygame.quit()
        exit(0)
        
    #test collision for enemy1
    if player_box.colliderect(enemy1_box):
        print("You lose!")
        pygame.quit()
        exit(0)
        
    #If the enemy is off the screen the user wins the game:
    if enemy_x_pos < 0 - enemy_width:
        print("You win!")
        pygame.quit()
        exit(0)
    
    #IF enemy1 is off the screen the user wins the game
    if enemy1_x_pos < 0 - enemy1_width:
        print("You win!")
        pygame.quit()
        exit(0)

    #if the prize collides with the player , the user wins the game
    if player_box.colliderect(prize_box):
        print("You win!")
        pygame.quit()
        exit(0)
    
    # Make the enemy and prize approach the player
    enemy_x_pos -= 0.20
    enemy1_x_pos -= 0.14
    monster_x_pos -= 0.18
    prize_x_pos -= 0.15


