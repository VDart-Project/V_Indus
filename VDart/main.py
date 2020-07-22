import pygame
from pygame import *
import math
import random

pygame.init()
# screen
screen = pygame.display.set_mode((1200, 600))

# Background
opening = pygame.image.load('Opening image.jpg')
background1 = pygame.image.load('Background1-Car.jpg')
background2 = pygame.image.load('Background2-Energy.jpg')
background3 = pygame.image.load('Background3-Health.jpg')
racetrack = pygame.image.load('level1.jpg')
landscape = pygame.image.load('level2.jpg')
future = pygame.image.load('level3.jpg')

# Background_sound
# mixer.music.load('wind1.wav')
# mixer.music.play(-1)


# icon
pygame.display.set_caption("V-Indus")
icon = pygame.image.load('icon1.png')
pygame.display.set_icon(icon)

# Dart

dartImg = pygame.image.load('dart1.png')
dartX = 600
dartY = 450
dartX_change = 0
dartY_change = 0

# Icons

# Icon1

icon1Img = []
icon1X = []
icon1Y = []
icon1X_change = []
icon1Y_change = []
num_of_icon1 = 6

for i in range(num_of_icon1):
    icon1Img.append(pygame.image.load('car.png'))
    icon1X.append(random.randint(0, 1135))
    icon1Y.append(random.randint(50, 150))
    icon1X_change.append(2)
    icon1Y_change.append(20)

# Icon2

icon2Img = []
icon2X = []
icon2Y = []
icon2X_change = []
icon2Y_change = []
num_of_icon2 = 6

for i in range(num_of_icon2):
    icon2Img.append(pygame.image.load('windmill.png'))
    icon2X.append(random.randint(0, 1135))
    icon2Y.append(random.randint(50, 150))
    icon2X_change.append(2)
    icon2Y_change.append(20)

# Icon3

icon3Img = []
icon3X = []
icon3Y = []
icon3X_change = []
icon3Y_change = []
num_of_icon3 = 6

for i in range(num_of_icon3):
    icon3Img.append(pygame.image.load('robot.png'))
    icon3X.append(random.randint(0, 1135))
    icon3Y.append(random.randint(50, 150))
    icon3X_change.append(2)
    icon3Y_change.append(20)

# score1
score1_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text1X = 10
text1Y = 10

# score2
score2_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text2X = 10
text2Y = 10

# score3
score3_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text3X = 10
text3Y = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 88)

# play again text
play_font = pygame.font.Font('freesansbold.ttf', 72)

# You win text
win_font = pygame.font.Font('freesansbold.ttf', 88)

# Next level text
next_font = pygame.font.Font('freesansbold.ttf', 72)


# functions
def show_score1(x, y):
    score1 = font.render("Score:" + str(score1_value), True, (255, 255, 255))
    screen.blit(score1, (x, y))


def show_score2(x, y):
    score2 = font.render("Score:" + str(score2_value), True, (255, 255, 255))
    screen.blit(score2, (x, y))


def show_score3(x, y):
    score3 = font.render("Score:" + str(score3_value), True, (255, 255, 255))
    screen.blit(score3, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (350, 250))


def play_again_text():
    again_text = play_font.render("Press 'A' to play again", True, (255, 255, 255))


def winning_text():
    win_text = win_font.render("YOU WON", True, (0, 255, 255))
    screen.blit(win_text, (350, 250))


def next_level_text():
    next_text = next_font.render("Press 'T' to play next level", True, (255, 255, 255))
    screen.blit(next_text, (350, 400))


def dart(x, y):
    screen.blit(dartImg, (x, y))


def iconf(x, y, i):
    screen.blit(icon1Img[i], (x, y))


def icons(x, y, i):
    screen.blit(icon2Img[i], (x, y))


def icont(x, y, i):
    screen.blit(icon3Img[i], (x, y))


def isCollision1(icon1X, icon1Y, dartX, dartY):
    distance = math.sqrt((math.pow(icon1X - dartX, 2)) + (math.pow(icon1Y - dartY, 2)))
    if distance < 10:
        return True
    else:
        return False


def isCollision2(icon2X, icon2Y, dartX, dartY):
    distance = math.sqrt((math.pow(icon2X - dartX, 2)) + (math.pow(icon2Y - dartY, 2)))
    if distance < 10:
        return True
    else:
        return False


def isCollision3(icon3X, icon3Y, dartX, dartY):
    distance = math.sqrt((math.pow(icon3X - dartX, 2)) + (math.pow(icon3Y - dartY, 2)))
    if distance < 10:
        return True
    else:
        return False


# Main while loop
running = True
starting = True
level1 = False
auto = False
level2 = False
energy = False
level3 = False
health = False

while running:

    # Starting image
    while starting:
        screen.fill((128, 128, 128))
        # Opening image
        screen.blit(opening, (0, 0))

        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                starting = False
                pygame.quit()
                quit()
        first = pygame.key.get_pressed()

        if first[pygame.K_p]:
            level1 = True
            starting = False

        pygame.display.update()

    # Level 1 start
    while level1:
        screen.fill((128, 128, 128))
        # Level 1 start image
        screen.blit(background1, (0, 0))

        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level1 = False
                pygame.quit()
                quit()

        toplay = pygame.key.get_pressed()

        if toplay[pygame.K_c]:
            auto = True
            level1 = False

        pygame.display.update()

    # Level 1
    while auto:
        screen.fill((128, 128, 128))
        # Background
        screen.blit(racetrack, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                auto = False
                pygame.quit()
                quit()

            # player keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dartX_change = -5
            if event.key == pygame.K_RIGHT:
                dartX_change = 5
            if event.key == pygame.K_UP:
                dartY_change = -5
            if event.key == pygame.K_DOWN:
                dartY_change = 5
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dartX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dartY_change = 0

        # Checking for boundaries of dart
        dartX += dartX_change
        dartY += dartY_change

        if dartX <= 0:
            dartX = 0
        elif dartX >= 1070:
            dartX = 1070
        elif dartY <= 0:
            dartY = 0
        elif dartY >= 500:
            dartY = 500

        for i in range(num_of_icon1):

            # You won
            if score1_value == 5:
                for a in range(num_of_icon1):
                    icon1Y[a] = 2000
                winning_text()
                next_level_text()
                mixer.music.stop()

                second = pygame.key.get_pressed()
                if second[pygame.K_t]:
                    level2 = True
                    auto = False
                    break
                break

            # Game over text
            if icon1Y[i] > 550:
                for j in range(num_of_icon1):
                    icon1Y[j] = 2000
                game_over_text()
                play_again_text()
                mixer.music.stop()
                again = pygame.key.get_pressed()
                if again[pygame.K_a]:
                    level1 = True
                    auto = False
                break

            icon1X[i] += icon1X_change[i]

            if icon1X[i] <= 0:
                icon1X_change[i] = 5
                icon1Y[i] += icon1Y_change[i]
            elif icon1X[i] >= 1070:
                icon1X_change[i] = -5
                icon1Y[i] += icon1Y_change[i]

            # Collision
            collision = isCollision1(icon1X[i], icon1Y[i], dartX, dartY)

            if collision:
                # explosion_sound = mixer.Sound('')
                # explosion_sound.play()

                score1_value += 1

                icon1X[i] = random.randint(0, 1070)
                icon1Y[i] = random.randint(50, 150)

            iconf(icon1X[i], icon1Y[i], i)

        dart(dartX, dartY)
        show_score1(text1X, text1Y)
        pygame.display.update()

    # Level 2 start
    while level2:
        screen.fill((128, 128, 128))
        # Level 1 start image
        screen.blit(background2, (0, 0))

        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level2 = False
                pygame.quit()
                quit()

        toplay = pygame.key.get_pressed()

        if toplay[pygame.K_c]:
            energy = True
            level2 = False

        pygame.display.update()

    # Level 2
    while energy:
        screen.fill((128, 128, 128))
        # Background
        screen.blit(landscape, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                energy = False
                pygame.quit()
                quit()

            # player keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dartX_change = -5
            if event.key == pygame.K_RIGHT:
                dartX_change = 5
            if event.key == pygame.K_UP:
                dartY_change = -5
            if event.key == pygame.K_DOWN:
                dartY_change = 5
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dartX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dartY_change = 0

        # Checking for boundaries of dart
        dartX += dartX_change
        dartY += dartY_change

        if dartX <= 0:
            dartX = 0
        elif dartX >= 1070:
            dartX = 1070
        elif dartY <= 0:
            dartY = 0
        elif dartY >= 500:
            dartY = 500

        for i in range(num_of_icon2):

            # You won
            if score2_value == 5:
                for a in range(num_of_icon2):
                    icon2Y[a] = 2000
                winning_text()
                next_level_text()
                mixer.music.stop()

                third = pygame.key.get_pressed()
                if third[pygame.K_t]:
                    level3 = True
                    energy = False
                    break
                break

            # Game over text
            if icon2Y[i] > 550:
                for j in range(num_of_icon2):
                    icon2Y[j] = 2000
                game_over_text()
                play_again_text()
                again = pygame.key.get_pressed()
                if again[pygame.K_a]:
                    level1 = True
                    energy = False
                mixer.music.stop()
                break

            icon2X[i] += icon2X_change[i]

            if icon2X[i] <= 0:
                icon2X_change[i] = 5
                icon2Y[i] += icon2Y_change[i]
            elif icon2X[i] >= 1070:
                icon2X_change[i] = -5
                icon2Y[i] += icon2Y_change[i]

            # Collision
            collision = isCollision2(icon2X[i], icon2Y[i], dartX, dartY)

            if collision:
                # explosion_sound = mixer.Sound('')
                # explosion_sound.play()

                score2_value += 1

                icon2X[i] = random.randint(0, 1070)
                icon2Y[i] = random.randint(50, 150)

            icons(icon2X[i], icon2Y[i], i)

        dart(dartX, dartY)
        show_score2(text2X, text2Y)
        pygame.display.update()

    # Level 3 start
    while level3:
        screen.fill((128, 128, 128))
        # Level 1 start image
        screen.blit(background3, (0, 0))

        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level3 = False
                pygame.quit()
                quit()

        toplay = pygame.key.get_pressed()

        if toplay[pygame.K_c]:
            health = True
            level3 = False

        pygame.display.update()

    # Level 3
    while health:
        screen.fill((128, 128, 128))
        # Background
        screen.blit(future, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                health = False
                pygame.quit()
                quit()

            # player keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dartX_change = -5
            if event.key == pygame.K_RIGHT:
                dartX_change = 5
            if event.key == pygame.K_UP:
                dartY_change = -5
            if event.key == pygame.K_DOWN:
                dartY_change = 5
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dartX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dartY_change = 0

        # Checking for boundaries of dart
        dartX += dartX_change
        dartY += dartY_change

        if dartX <= 0:
            dartX = 0
        elif dartX >= 1070:
            dartX = 1070
        elif dartY <= 0:
            dartY = 0
        elif dartY >= 500:
            dartY = 500

        for i in range(num_of_icon3):

            # You won
            if score3_value == 5:
                for a in range(num_of_icon3):
                    icon3Y[a] = 2000
                winning_text()
                play_again_text()
                mixer.music.stop()

                again = pygame.key.get_pressed()
                if again[pygame.K_a]:
                    level1 = True
                    health = False
                    break
                break

            # Game over text
            if icon3Y[i] > 550:
                for j in range(num_of_icon3):
                    icon3Y[j] = 2000
                game_over_text()
                play_again_text()
                again = pygame.key.get_pressed()
                if again[pygame.K_a]:
                    level1 = True
                    health = False
                mixer.music.stop()
                break

            icon3X[i] += icon3X_change[i]

            if icon3X[i] <= 0:
                icon3X_change[i] = 5
                icon3Y[i] += icon3Y_change[i]
            elif icon3X[i] >= 1070:
                icon3X_change[i] = -5
                icon3Y[i] += icon3Y_change[i]

            # Collision
            collision = isCollision3(icon3X[i], icon3Y[i], dartX, dartY)

            if collision:
                # explosion_sound = mixer.Sound('')
                # explosion_sound.play()

                score3_value += 1

                icon3X[i] = random.randint(0, 1070)
                icon3Y[i] = random.randint(50, 150)

            icont(icon3X[i], icon3Y[i], i)

        dart(dartX, dartY)
        show_score3(text3X, text3Y)
        pygame.display.update()
