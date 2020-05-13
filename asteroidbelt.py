import pygame
import sys
import random
from pygame import mixer


pygame.init()

pygame.display.set_caption("Asteroid Belt")
icon = pygame.image.load('/Users/David Uribe/Desktop/guitartuner/finalproject/icon.png')
pygame.display.set_icon(icon)

mixer.music.load("/Users/David Uribe/Desktop/guitartuner/finalproject/spacetheme.wav")
mixer.music.play(-1)




WIDTH = 1280
HEIGHT = 720


WHITE = (255,255,255)

asteroid_speed = 10

background = pygame.image.load("/Users/David Uribe/Desktop/guitartuner/finalproject/space2.png")


player_pos = [WIDTH/2, 620]
playerImg = pygame.image.load('/Users/David Uribe/Desktop/guitartuner/finalproject/player.png')

enemyImg = pygame.image.load('/Users/David Uribe/Desktop/guitartuner/finalproject/asteroid.png')


enemy_pos = [random.randint(0,WIDTH-50), 0]
asteroid_list = [enemy_pos]


screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0


new_font = pygame.font.SysFont("monospace", 35)
over_font = pygame.font.SysFont('monospace', 64)

clock = pygame.time.Clock()

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (500, 100))

def set_difficulty(score, asteroid_speed):
    if score < 20:
        asteroid_speed = 6
    elif score < 40:
        asteroid_speed = 10
    elif score < 60:
        asteroid_speed = 13
    else:
        asteroid_speed = 20
    return asteroid_speed



def move_asteroid(asteroid_list):
    delay = random.random()
    if len(asteroid_list) < 10 and delay < 0.1:
        x_pos = random.randint(0,WIDTH-50
    )
        y_pos = 0
        asteroid_list.append([x_pos, y_pos])

def make_asteroid(asteroid_list):
    for enemy_pos in asteroid_list:
        screen.blit(enemyImg,(enemy_pos[0], enemy_pos[1]))

def update_asteroid_pos(asteroid_list, score):
    for i, enemy_pos in enumerate(asteroid_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += asteroid_speed
        else:
            asteroid_list.pop(i)
            score += 1
    return score

def collision_check(asteroid_list, player_pos):
    for enemy_pos in asteroid_list:
        if isCollision(enemy_pos, player_pos):
            return True
    return False

def isCollision(player_pos, enemy_pos):
    player_x = player_pos[0]
    player_y = player_pos[1]

    enemy_x = enemy_pos[0]
    enemy_y = enemy_pos[1]

    if (enemy_x >= player_x and enemy_x < (player_x + 50)) or (player_x >= enemy_x and player_x < (enemy_x+50)):
         if (enemy_y >= player_y and enemy_y < (player_y + 50)) or (player_y >= enemy_y and player_y < (enemy_y+50 )):
            return True
    return False

while not game_over:

    screen.fill(WHITE)
    screen.blit(background,(0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_RIGHT:
                x += 50

            player_pos = [x,y]

    

    move_asteroid(asteroid_list)
    score = update_asteroid_pos(asteroid_list, score)
    asteroid_speed = set_difficulty(score, asteroid_speed)

    text = "Score:" + str(score)
    label = new_font.render(text, 1, WHITE)
    screen.blit(label, (WIDTH-1200, HEIGHT-40))

    if collision_check(asteroid_list, player_pos):
        game_over = True
        game_over_text()
        

    make_asteroid(asteroid_list)

    screen.blit(playerImg,(player_pos[0], player_pos[1]))

    
    clock.tick(40)
    pygame.display.update()