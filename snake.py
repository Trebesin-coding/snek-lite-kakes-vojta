import pygame
import random
from sys import exit

pygame.init()
running = True
screen_height = 800
screen_width = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
elapsed_time = 0
green_coin_time = 0
gold_coin_time = 0
green_coin_time_despawn = 0
gold_coin_time_despawn = 0
gold_coin_time_spawn = random.randint(10, 30) * 1000
pause = False
font = pygame.font.Font("PixelifySans-Regular.ttf", 25)
win_font = pygame.font.Font("PixelifySans-Regular.ttf", 80)

coin_surf = pygame.image.load("coin.png").convert_alpha()
green_coin_surf = pygame.image.load("green_coin.png").convert_alpha()
gold_coin_surf = pygame.image.load("gold_coin.png").convert_alpha()  

coin_x = random.randint(0, screen_width - 40)
coin_y = random.randint(0, screen_height - 40)
coin_rect = coin_surf.get_rect(midbottom=(coin_x, coin_y))
coin_existence = True

green_coin_x = (screen_width * 40)
green_coin_y = (screen_height * 40)
green_coin_existence = False
green_coin_rect = green_coin_surf.get_rect(midbottom=(green_coin_x, green_coin_y))

gold_coin_x = (screen_width * 40)
gold_coin_y = (screen_height * 40)
gold_coin_existence = False
gold_coin_rect = gold_coin_surf.get_rect(midbottom=(gold_coin_x, gold_coin_y))

player_surf = pygame.image.load("snake.png").convert_alpha()
player_speed = 5
player_score = 0
player_x = screen_width / 2
player_y = screen_height / 2
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_rect.top -= player_speed
    if key[pygame.K_s]:
        player_rect.bottom += player_speed
    if key[pygame.K_a]:
        player_rect.left -= player_speed
    if key[pygame.K_d]:
        player_rect.right += player_speed
    if key[pygame.K_x]:
        exit()
  

    screen.fill("white")
    score = font.render(f"Score: {player_score}", False, "#000000") 
    screen.blit(score, (screen_width-400, 10))
    screen.blit(player_surf, player_rect)
    screen.blit(coin_surf, coin_rect)
    screen.blit(green_coin_surf, green_coin_rect)
    screen.blit(gold_coin_surf, gold_coin_rect)
        

    elapsed_time += clock.get_time()
    if elapsed_time > 100:
        pause = False 


    if player_rect.colliderect(coin_rect) and not pause:
        player_score += 1 
        elapsed_time = 0
        pause = True
        coin_existence = False

    if player_rect.colliderect(green_coin_rect) and not pause:
        player_score += 100 
        elapsed_time = 0
        green_coin_time = 0
        green_coin_time_despawn = 0
        green_coin_x = (screen_width * 40)
        green_coin_y = (screen_height * 40)
        green_coin_rect = green_coin_surf.get_rect(midbottom=(green_coin_x, green_coin_y))
        green_coin_existence = False
        pause = True

    if player_rect.colliderect(gold_coin_rect) and not pause:
        player_score += 1000 
        elapsed_time = 0
        gold_coin_time = 0
        gold_coin_time_despawn = 0
        gold_coin_x = (screen_width * 40)
        gold_coin_y = (screen_height * 40)
        gold_coin_rect = gold_coin_surf.get_rect(midbottom=(gold_coin_x, gold_coin_y))
        gold_coin_existence = False
        pause = True
        

    if player_score >= 1000:
         screen.fill("yellow")
         win_screen = win_font.render(f"You´ve won", False, "#000000")
         screen.blit(win_screen, (screen_width/3, screen_height/3))
         
         
    if not coin_existence:
        coin_x = random.randint(0, screen_width - 40)
        coin_y = random.randint(0, screen_height - 40)
        coin_existence =  True
        coin_rect = coin_surf.get_rect(midbottom=(coin_x, coin_y))



    if not green_coin_existence:
        green_coin_time += clock.get_time()
        if green_coin_time > 3000:
            green_coin_x = random.randint(0, screen_width - 40)
            green_coin_y = random.randint(0, screen_height - 40)
            green_coin_rect = green_coin_surf.get_rect(midbottom=(green_coin_x, green_coin_y))
            green_coin_existence = True
            green_coin_time = 0

    if green_coin_existence:        
        green_coin_time_despawn += clock.get_time()
        if green_coin_time_despawn >= 2000:
            green_coin_x = (screen_width * 40)
            green_coin_y = (screen_height * 40)
            green_coin_rect = green_coin_surf.get_rect(midbottom=(green_coin_x, green_coin_y))
            green_coin_existence = False
            green_coin_time_despawn = 0



    if not gold_coin_existence:
        gold_coin_time += clock.get_time()
        if gold_coin_time >= gold_coin_time_spawn:
            gold_coin_x = random.randint(0, screen_width - 40)
            gold_coin_y = random.randint(0, screen_height - 40)
            gold_coin_rect = gold_coin_surf.get_rect(midbottom=(gold_coin_x, gold_coin_y))
            gold_coin_existence = True
            gold_coin_time = 0
            gold_coin_time_spawn = random.randint(10, 30) * 1000

    if gold_coin_existence:
        gold_coin_time_despawn += clock.get_time()
        if gold_coin_time_despawn >= 2000:
            gold_coin_x = (screen_width * 40)
            gold_coin_y = (screen_height * 40)
            gold_coin_rect = gold_coin_surf.get_rect(midbottom=(gold_coin_x, gold_coin_y))
            gold_coin_existence = False
            gold_coin_time_despawn = 0

    pygame.display.update()
    clock.tick(60)
