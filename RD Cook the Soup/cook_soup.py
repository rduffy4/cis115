#Ryan Duffy: Cook the Soup!
import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cook the Soup!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
STARTING_BOOST_LEVEL = 100

STARTING_SOUP_VELOCITY = 3
SOUP_ACCELERATION = .5
BUFFER_DISTANCE = 100

TIMER_VELOCITY = 5
TIMER_SIZE = 0

STYLE_WIDTH = 50
STYLE_HEIGHT= 3

COMBO_AMOUNT = 1

combo = 0
high_score = 0

timer_x = (WINDOW_WIDTH // 2)
timer_y = (WINDOW_HEIGHT //2)

style_x = (WINDOW_WIDTH // 2)
style_y = -500
style_y2 = -500
style_y3 = -500
style_y4 = -500
style_y5 = -500
style_y6 = -500
style_y7 = -500
style_y8 = -500

player_boost_velocity = 10

score = 0
points = 0
best_combo = 0

player_pos = (0, 0)
player_fire_pos = (0, 0)

raw_soup_pos = (0, 0)
cooked_soup_pos = (0, 0)

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

soup_velocity = STARTING_SOUP_VELOCITY

#Set colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (127, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (36, 36, 36)

#Set fonts
font = pygame.font.Font("BodoniFLF.ttf", 32)

score_text = font.render("Score: " + str(score), True, VIOLET)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render("Cook the Soup!", True, VIOLET)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

best_combo_text = font.render("Best Combo: " + str(best_combo), True, VIOLET)
best_combo_rect = best_combo_text.get_rect()
best_combo_rect.topright = (WINDOW_WIDTH - 40, 10)

lives_text = font.render("Lives: " + str(player_lives), True, VIOLET)
lives_rect = lives_text.get_rect()
lives_rect.topleft = (10, 10)

high_score_text = font.render("High Score: " + str(high_score), True, VIOLET)
high_score_rect = high_score_text.get_rect()
high_score_rect.topright = (WINDOW_WIDTH - 40, 50)

game_over_text = font.render("FINAL SCORE: " + str(score), True, VIOLET)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, VIOLET)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Set sounds and music
good_soup_sound = pygame.mixer.Sound("good_soup.flac")
bad_soup_sound = pygame.mixer.Sound("bad_soup.flac")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
burn_sound = pygame.mixer.Sound("burn.wav")
pygame.mixer.music.load("bgm.mp3")

#Set images
player_image_right = pygame.image.load("avatar_right.png")
player_image_left = pygame.image.load("avatar_left.png")

timer_coord = (timer_x, timer_y, TIMER_SIZE, TIMER_SIZE)
timer_rect = pygame.draw.rect(display_surface, WHITE, timer_coord)

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

player_fire_right = pygame.image.load("avatar_fire_right.png")
player_fire_left = pygame.image.load("avatar_fire_left.png")

player_fire = player_fire_left
player_fire_rect = player_fire.get_rect()
player_fire_rect.center = (-1024, -1024)

raw_soup_image = pygame.image.load("raw_soup.png")
raw_soup_rect = raw_soup_image.get_rect()
raw_soup_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

cooked_soup_image = pygame.image.load("cooked_soup.png")
cooked_soup_rect = cooked_soup_image.get_rect()
cooked_soup_rect.topleft = (-200, -200)

#The main game loop
pygame.mixer.music.play()
running = True
while running:
    #Check if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Activate Fire Aura
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_pos = player_rect
                player_fire_pos = player_fire_rect

                player_fire_rect = player_pos
                player_rect = player_fire_pos
                
                timer_y = WINDOW_HEIGHT // 2
                timer_coord = (timer_x, timer_y, TIMER_SIZE, TIMER_SIZE)


    #Deactivate Fire Aura
    if (timer_y >= (WINDOW_HEIGHT // 2) + 100) and (player_rect.right < 0):
        player_pos = player_rect
        player_fire_pos = player_fire_rect

        player_fire_rect = player_pos
        player_rect = player_fire_pos

        timer_y = WINDOW_HEIGHT // 2

    style_coord = (style_x, style_y, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect = pygame.draw.rect(display_surface, VIOLET, style_coord)

    style_coord2 = (style_x, style_y2, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect2 = pygame.draw.rect(display_surface, VIOLET, style_coord2)

    style_coord3 = (style_x, style_y3, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect3 = pygame.draw.rect(display_surface, INDIGO, style_coord3)

    style_coord4 = (style_x, style_y4, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect4 = pygame.draw.rect(display_surface, INDIGO, style_coord4)

    style_coord5 = (style_x, style_y5, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect5 = pygame.draw.rect(display_surface, BLUE, style_coord5)

    style_coord6 = (style_x, style_y6, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect6 = pygame.draw.rect(display_surface, BLUE, style_coord6)

    style_coord7 = (style_x, style_y7, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect7 = pygame.draw.rect(display_surface, GREEN, style_coord7)

    style_coord8 = (style_x, style_y8, STYLE_WIDTH, STYLE_HEIGHT)
    style_rect8 = pygame.draw.rect(display_surface, GREEN, style_coord8)

    #Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and WINDOW_WIDTH > player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    if keys[pygame.K_LEFT] and WINDOW_WIDTH > player_fire_rect.left > 0:
        player_fire_rect.x -= player_velocity
        player_fire = player_fire_left
    if keys[pygame.K_RIGHT] and 0 < player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right
    if keys[pygame.K_RIGHT] and 0 < player_fire_rect.right < WINDOW_WIDTH:
        player_fire_rect.x += player_velocity
        player_fire = player_fire_right
    if keys[pygame.K_UP] and WINDOW_HEIGHT > player_rect.top > 100:
        player_rect.y -= player_velocity
    if keys[pygame.K_UP] and WINDOW_HEIGHT > player_fire_rect.top > 100:
        player_fire_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and 0 < player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity
    if keys[pygame.K_DOWN] and 0 < player_fire_rect.bottom < WINDOW_HEIGHT:
        player_fire_rect.y += player_velocity

    #Engage Boost
    if keys[pygame.K_LSHIFT] and boost_level > 0:
        player_velocity = player_boost_velocity
        
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    #Move the timer
    timer_y += TIMER_VELOCITY
    timer_coord = (timer_x, timer_y, TIMER_SIZE, TIMER_SIZE)

    #Move the soup and update soup points
    if 0 < raw_soup_rect.right < WINDOW_WIDTH:
        raw_soup_rect.y += soup_velocity

    if 0 < cooked_soup_rect.right < WINDOW_WIDTH:
        cooked_soup_rect.y += soup_velocity

    #Cooking the Soup
    if keys[pygame.K_SPACE] and (WINDOW_HEIGHT + 32 > raw_soup_rect.top > 100):
        raw_soup_pos = raw_soup_rect
        cooked_soup_pos = cooked_soup_rect
        cooked_soup_rect = raw_soup_pos
        raw_soup_rect = cooked_soup_pos
        burn_sound.play()

    #Player missed the soup
    if raw_soup_rect.top > WINDOW_HEIGHT:
        miss_sound.play()
        raw_soup_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        combo = 0

        style_y = -500
        style_y2 = style_y - 4
        style_y3 = style_y - 8
        style_y4 = style_y - 12
        style_y5 = style_y - 16
        style_y6 = style_y - 20
        style_y7 = style_y - 24
        style_y8 = style_y - 28        

    if cooked_soup_rect.top > WINDOW_HEIGHT:
        miss_sound.play()
        raw_soup_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        cooked_soup_rect.center = (-200, -200)
        combo = 0

        style_y = -500
        style_y2 = style_y - 4
        style_y3 = style_y - 8
        style_y4 = style_y - 12
        style_y5 = style_y - 16
        style_y6 = style_y - 20
        style_y7 = style_y - 24
        style_y8 = style_y - 28

    #Raw Soup collision
    if player_rect.colliderect(raw_soup_rect):
        player_lives -= 1
        soup_velocity = STARTING_SOUP_VELOCITY
        bad_soup_sound.play()
        raw_soup_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        combo = 0

        style_y = -500
        style_y2 = style_y - 4
        style_y3 = style_y - 8
        style_y4 = style_y - 12
        style_y5 = style_y - 16
        style_y6 = style_y - 20
        style_y7 = style_y - 24
        style_y8 = style_y - 28

    #Cooked Soup collision        
    if player_rect.colliderect(cooked_soup_rect) or player_fire_rect.colliderect(cooked_soup_rect):
        combo += COMBO_AMOUNT
        if combo > 1:
            score += combo - 1

            style_y = 85

        if combo > 2:
            style_y2 = style_y - 4
        if combo > 3:
            style_y3 = style_y - 8
        if combo > 4:
            style_y4 = style_y - 12
        if combo > 5:
            style_y5 = style_y - 16
        if combo > 6:
            style_y6 = style_y - 20
        if combo > 7:
            style_y7 = style_y - 24
        if combo > 8:
            style_y8 = style_y - 28

        if combo == 8:
            player_velocity *= 1.5
            soup_velocity /= 3

        points += 1
        score += 1
        if score > high_score:
            high_score = score
        if combo > best_combo:
            best_combo = combo
        good_soup_sound.play()
        cooked_soup_rect.topleft = (-200, -200)
        raw_soup_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        soup_velocity += SOUP_ACCELERATION



    #Update HUD
    score_text = font.render("Score: " + str(score), True, VIOLET)
    best_combo_text = font.render("Best Combo: " + str(best_combo), True, VIOLET)
    lives_text = font.render("Lives: " + str(player_lives), True, VIOLET)
    high_score_text = font.render("High Score: " + str(high_score), True, VIOLET)

    #Check for game over
    if player_lives == 0:
        game_over_text = font.render("FINAL SCORE: " + str(score), True, VIOLET)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause the game until the player presses a key, then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    comno = 0
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    soup_velocity = STARTING_SOUP_VELOCITY

                    pygame.mixer.music.play()
                    is_paused = False
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #Fill the surface
    display_surface.fill(GREY)

    #Blit the HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(best_combo_text, best_combo_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(high_score_text, high_score_rect)
    pygame.draw.line(display_surface, VIOLET, (0, 100), (WINDOW_WIDTH, 100), 3)

    #Blit assests
    display_surface.blit(player_image, player_rect)
    display_surface.blit(player_fire, player_fire_rect)
    display_surface.blit(raw_soup_image, raw_soup_rect)
    display_surface.blit(cooked_soup_image, cooked_soup_rect)
    timer_rect = pygame.draw.rect(display_surface, WHITE, timer_coord)
    style_rect = pygame.draw.rect(display_surface, VIOLET, style_coord)
    style_rect2 = pygame.draw.rect(display_surface, VIOLET, style_coord2)
    style_rect3 = pygame.draw.rect(display_surface, INDIGO, style_coord3)
    style_rect4 = pygame.draw.rect(display_surface, INDIGO, style_coord4)
    style_rect5 = pygame.draw.rect(display_surface, BLUE, style_coord5)
    style_rect6 = pygame.draw.rect(display_surface, BLUE, style_coord6)
    style_rect7 = pygame.draw.rect(display_surface, GREEN, style_coord7)
    style_rect8 = pygame.draw.rect(display_surface, GREEN, style_coord8)

    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()