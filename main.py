import pygame
import random
from pygame import mixer


def display_score():

    current_time = int((pygame.time.get_ticks() / 1000)) - start_time  # Creates the game score timer (Divide by 1000 to make the time into seconds)

    score_surface = game_font.render(f'Score: {current_time}', False, 'Red')  # Creates the surface for the score
    score_rect = score_surface.get_rect(center=(400, 25))  # Creates the rectangle for the score
    screen.blit(score_surface, score_rect)  # Puts the score on screen

    return current_time


def lives_calc():

    lives_surface = game_font.render(f'Lives: {lives}', False, 'Red')
    lives_rect = lives_surface.get_rect(center=(100, 25))
    screen.blit(lives_surface, lives_rect)


lives = 3

start_time = 0

score = 0

pygame.init()  # Starts Space_Explorer (Like starting a car engine)

screen = pygame.display.set_mode((800, 400))  # Creates the display surface

pygame.display.set_caption('Space Explorer')  # Creates the title caption for the display surface

clock = pygame.time.Clock()  # Creates a clock object

game_font = pygame.font.Font('arcade/ARCADE.TTF', 50)  # Creates the font object

# Importing Background Images

background_surface = pygame.image.load('space_background_pack/layers/parallax-space-backgound.png').convert_alpha()  # Imports the background
background_surface_scaled = pygame.transform.scale(background_surface, (800, 400))  # Scales the size of the background

background_object_big_planet = pygame.image.load('space_background_pack/layers/parallax-space-big-planet.png').convert_alpha()  # Imports the big planet
background_object_big_planet_scaled = pygame.transform.scale(background_object_big_planet, (100, 100))

background_object_far_planets = pygame.image.load('space_background_pack/layers/parallax-space-far-planets.png').convert_alpha()  # Imports the far planets

background_object_ring_planet = pygame.image.load('space_background_pack/layers/parallax-space-ring-planet.png').convert_alpha()  # Imports the ring planet
background_object_ring_planet_scaled = pygame.transform.scale(background_object_ring_planet, (100, 200))

background_object_stars = pygame.image.load('space_background_pack/layers/parallax-space-stars.png').convert_alpha()  # Imports the stars

# Creating the text surfaces

text_surface = game_font.render('Space Explorer', False, (150, 0, 0))  # Creates the font surface
text_rect = text_surface.get_rect(center=(400, 50))  # Creates the text rectangle

retry_surface = game_font.render('Press Space to Start', False, (150, 0, 0))
retry_rect = retry_surface.get_rect(center=(400, 300))

# Importing Enemy Images

game_enemy_lava = pygame.image.load('Planets/Lava.png').convert_alpha()  # Imports the game obstacle
game_enemy_lava_x_position = random.randint(900, 1600)  # Sets the spawn point of the obstacle to the far right
game_enemy_lava_y_position = random.randint(0, 350)  # Sets the spawn point of the obstacle to the near middle
lava_rect = game_enemy_lava.get_rect(center=(game_enemy_lava_x_position, game_enemy_lava_y_position))

game_enemy_lava_2 = pygame.image.load('Planets/Lava.png').convert_alpha()
game_enemy_lava_x_position_2 = random.randint(900, 1600)
game_enemy_lava_y_position_2 = random.randint(0, 350)
lava_2_rect = game_enemy_lava_2.get_rect(center=(game_enemy_lava_x_position_2, game_enemy_lava_y_position_2))

####

game_enemy_baren = pygame.image.load('Planets/Baren.png').convert_alpha()
game_enemy_baren_x_position = random.randint(900, 1600)
game_enemy_baren_y_position = random.randint(0, 350)
baren_rect = game_enemy_baren.get_rect(center=(game_enemy_baren_x_position, game_enemy_baren_y_position))

game_enemy_baren_2 = pygame.image.load('Planets/Baren.png').convert_alpha()
game_enemy_baren_x_position_2 = random.randint(900, 1600)
game_enemy_baren_y_position_2 = random.randint(0, 350)
baren_2_rect = game_enemy_baren_2.get_rect(center=(game_enemy_baren_x_position_2, game_enemy_baren_y_position_2))

####

game_enemy_black_hole = pygame.image.load('Planets/Black_hole.png').convert_alpha()
game_enemy_black_hole_x_position = random.randint(900, 1600)
game_enemy_black_hole_y_position = random.randint(0, 350)
black_hole_rect = game_enemy_black_hole.get_rect(center=(game_enemy_black_hole_x_position, game_enemy_black_hole_y_position))

game_enemy_black_hole_2 = pygame.image.load('Planets/Black_hole.png').convert_alpha()
game_enemy_black_hole_x_position_2 = random.randint(900, 1600)
game_enemy_black_hole_y_position_2 = random.randint(0, 350)
black_hole_2_rect = game_enemy_black_hole_2.get_rect(center=(game_enemy_black_hole_x_position_2, game_enemy_black_hole_y_position_2))

####

game_enemy_ice = pygame.image.load('Planets/Ice.png').convert_alpha()
game_enemy_ice_x_position = random.randint(900, 1600)
game_enemy_ice_y_position = random.randint(0, 350)
ice_rect = game_enemy_ice.get_rect(center=(game_enemy_ice_x_position, game_enemy_ice_y_position))

game_enemy_ice_2 = pygame.image.load('Planets/Ice.png').convert_alpha()
game_enemy_ice_x_position_2 = random.randint(900, 1600)
game_enemy_ice_y_position_2 = random.randint(0, 350)
ice_2_rect = game_enemy_ice_2.get_rect(center=(game_enemy_ice_x_position_2, game_enemy_ice_y_position_2))

####

game_enemy_terran = pygame.image.load('Planets/Terran.png').convert_alpha()
game_enemy_terran_x_position = random.randint(900, 1600)
game_enemy_terran_y_position = random.randint(0, 350)
terran_rect = game_enemy_terran.get_rect(center=(game_enemy_terran_x_position, game_enemy_terran_y_position))

game_enemy_terran_2 = pygame.image.load('Planets/Terran.png').convert_alpha()
game_enemy_terran_x_position_2 = random.randint(900, 1600)
game_enemy_terran_y_position_2 = random.randint(0, 350)
terran_2_rect = game_enemy_terran_2.get_rect(center=(game_enemy_terran_x_position_2, game_enemy_terran_y_position_2))

player_surface = pygame.image.load('ShooterFull/Ships/6/Pattern3/Red/Right/6.png').convert_alpha()  # Imports the player ship
player_rect = player_surface.get_rect(center=(0, 220))  # Takes a surface and draws a rectangle around it

player_surface_scaled = pygame.transform.scale(player_surface, (350, 200))  # Creates the image for the game over screen
player_surface_scaled_rect = player_surface_scaled.get_rect(center=(400, 160))

object_rect_list = [lava_rect, lava_2_rect, baren_rect, baren_2_rect, black_hole_rect, black_hole_2_rect, ice_rect, ice_2_rect, terran_rect, terran_2_rect]

game_active = False

# Game Sounds

death_sound = pygame.mixer.Sound('videogame-death-sound-43894.mp3')
move_sound = pygame.mixer.Sound('sfx_jump_07-80241.mp3')
hit_sound = pygame.mixer.Sound('vibrating-thud-39536.mp3')

while True:  # Main game loop

    # Event Loop

    for event in pygame.event.get():  # Loops through a list of pygame player events

        if event.type == pygame.QUIT:  # Checks if the QUIT event is present

            pygame.quit()  # Quits pygame

            exit()

        if game_active:

            if event.type == pygame.KEYDOWN:  # Checks to see if a key is pressed

                if event.key == pygame.K_UP:  # Checks to see if up arrow is pressed

                    player_rect.y -= 20

                    move_sound.play()

                if event.key == pygame.K_DOWN:  # Checks to see if down arrow is pressed

                    player_rect.y += 20

                    move_sound.play()

                if event.key == pygame.K_LEFT:  # Checks to see if the left arrow key is pressed

                    player_rect.x -= 20

                    move_sound.play()

                if event.key == pygame.K_RIGHT:  # Checks to see if the right arrow key is pressed

                    player_rect.x += 20

                    move_sound.play()

        else:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    lives = 3

                    mixer.music.load('2019-12-11_-_Retro_Platforming_-_David_Fesliyan.mp3')  # Loads the game music
                    pygame.mixer.music.play(-1)  # Plays the game music on loop

                    game_active = True

                    start_time = int((pygame.time.get_ticks() / 1000))  # Resets the player score time to 0

                    # Resetting the player position

                    player_rect.left = 0
                    player_rect.y = 200

                    # Resetting all the enemy positions

                    lava_rect.left = random.randint(900, 1600)
                    lava_rect.y = random.randint(0, 350)

                    lava_2_rect.left = random.randint(900, 1600)
                    lava_2_rect.y = random.randint(0, 350)

                    ####

                    baren_rect.left = random.randint(900, 1600)
                    baren_rect.y = random.randint(0, 350)

                    baren_2_rect.left = random.randint(900, 1600)
                    baren_2_rect.y = random.randint(0, 350)

                    ####

                    black_hole_rect.left = random.randint(900, 1600)
                    black_hole_rect.y = random.randint(0, 350)

                    black_hole_2_rect.left = random.randint(900, 1600)
                    black_hole_2_rect.y = random.randint(0, 350)

                    ####

                    ice_rect.left = random.randint(900, 1600)
                    ice_rect.y = random.randint(0, 350)

                    ice_2_rect.left = random.randint(900, 1600)
                    ice_2_rect.y = random.randint(0, 350)

                    ####

                    terran_rect.left = random.randint(900, 1600)
                    terran_rect.y = random.randint(0, 350)

                    terran_2_rect.left = random.randint(900, 1600)
                    terran_2_rect.y = random.randint(0, 350)

    if game_active:

        screen.blit(background_surface_scaled, (0, 0))  # Put one surface with another

        screen.blit(background_object_big_planet_scaled, (50, 50))

        screen.blit(background_object_far_planets, (200, 150))

        screen.blit(background_object_ring_planet_scaled, (600, 100))

        screen.blit(background_object_stars, (500, 25))

        score = display_score()  # Calls the function to display the player score

        lives_calc()

        # pygame.draw.rect(screen, 'Black', text_rect)  # Draws a rectangle behind the title text
        # pygame.draw.rect(screen, 'Black', text_rect, 10)  # Draws the outside of the rectangle
        # screen.blit(text_surface, text_rect)  # Puts the game title onto the screen

        screen.blit(player_surface, player_rect)

        lava_rect.x -= 5  # Decreases the obstacle\'s position so it moves left
        if lava_rect.right < -100:  # Checks if the obstacle went off-screen
            lava_rect.left = random.randint(900, 1600)  # Resets the obstacle to the far right
            lava_rect.y = random.randint(0, 350)  # Sets the y position to a random number within the height
        screen.blit(game_enemy_lava, lava_rect)  # Imports the game enemy to the surface

        lava_2_rect.x -= 8
        if lava_2_rect.right < -100:
            lava_2_rect.left = random.randint(900, 1600)
            lava_2_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_lava_2, lava_2_rect)

        ####

        baren_rect.x -= 6
        if baren_rect.right < -100:
            baren_rect.left = random.randint(900, 1600)
            baren_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_baren, baren_rect)

        baren_2_rect.x -= 9
        if baren_2_rect.right < -100:
            baren_2_rect.left = random.randint(900, 1600)
            baren_2_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_baren_2, baren_2_rect)

        ####

        black_hole_rect.x -= 4
        if black_hole_rect.right < -100:
            black_hole_rect.left = random.randint(900, 1600)
            black_hole_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_black_hole, black_hole_rect)

        black_hole_2_rect.x -= 7
        if black_hole_2_rect.right < -100:
            black_hole_2_rect.left = random.randint(900, 1600)
            black_hole_2_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_black_hole_2, black_hole_2_rect)

        ####

        ice_rect.x -= 7
        if ice_rect.right < -100:
            ice_rect.left = random.randint(900, 1600)
            ice_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_ice, ice_rect)

        ice_2_rect.x -= 9
        if ice_2_rect.right < -100:
            ice_2_rect.left = random.randint(900, 1600)
            ice_2_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_ice_2, ice_2_rect)

        ####

        terran_rect.x -= 4
        if terran_rect.right < -100:
            terran_rect.left = random.randint(900, 1600)
            terran_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_terran, terran_rect)

        terran_2_rect.x -= 7
        if terran_2_rect.right < -100:
            terran_2_rect.left = random.randint(900, 1600)
            terran_2_rect.y = random.randint(0, 350)
        screen.blit(game_enemy_terran_2, terran_2_rect)

        for rect in object_rect_list:

            if player_rect.colliderect(rect): # Checks if there is a collision between the player rect and the planet rect

                lives -= 1

                hit_sound.play()

                rect.left = random.randint(900, 1600)
                rect.y = random.randint(0, 350)

            if lives == 0:

                game_active = False

                pygame.mixer.music.stop()

                death_sound.play()

        # Checking if player goes off-screen

        if player_rect.bottom >= 400:

            player_rect.bottom = 35

        if player_rect.top <= 0:

            player_rect.top = 365

        if player_rect.left < 0:

            player_rect.left = 0

        if player_rect.right > 800:

            player_rect.right = 800

    else:

        game_over_surface = game_font.render(f'Your Score: {score} seconds!', False, (150, 0, 0))
        game_over_rect = game_over_surface.get_rect(center=(400, 300))

        screen.fill((0, 0, 0))

        if score == 0:

            screen.blit(text_surface, text_rect)

            screen.blit(player_surface_scaled, player_surface_scaled_rect)

            screen.blit(retry_surface, retry_rect)

        else:

            screen.blit(text_surface, text_rect)

            screen.blit(player_surface_scaled, player_surface_scaled_rect)

            screen.blit(game_over_surface, game_over_rect)

    pygame.display.update()  # Updates the display surface

    clock.tick(60)  # Tells the loop to not run more than 60 times a second (Max frame rate)
