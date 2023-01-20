import pygame
import time
import random

pygame.init()

# define colors
white = (255,255,255)
black = (0,0,0)
orange = (255,165,0)
red = (255,0,0)

width,height = 600,500

game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Vedant's snake game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu',30)
score_font = pygame.font.SysFont('ubuntu',25)

def print_score(score):
    text = score_font.render("Score : "+str(score),True,orange)
    game_display.blit(text,[0,0])

def draw_snake(snake_size,snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display,white,[pixel[0],pixel[1],snake_size,snake_size])

def run_game():

    game_over = False
    game_close = False

    X = width/2
    Y = height/2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0,width-snake_size)/10.0) * 10.0
    target_y = round(random.randint(0,height-snake_size)/10.0) * 10.0

    while not game_over:
        
        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over !!! press 1 for quit and 2 for restart",True,red)
            game_display.blit(game_over_message,[50, height/3])
            print_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_close = False
                        game_over = True

                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                print("Key Pressed ",event.key)
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0

                if event.key == pygame.K_UP:
                    y_speed = -snake_size
                    x_speed = 0
                
                if event.key == pygame.K_DOWN:
                    y_speed = snake_size
                    x_speed = 0
            
        if X >= width or X < 0 or Y >= height or Y<0:
            game_close = True

        X += x_speed
        Y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display,orange,[target_x,target_y,snake_size,snake_size])

        snake_pixels.append([X,Y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if [X,Y] == pixel:
                game_close = True

        draw_snake(snake_size,snake_pixels)
        print_score(snake_length-1)
        pygame.display.update()

        if(X == target_x and Y == target_y):
            snake_length += 1
            target_x = round(random.randrange(0,width-snake_size)/10)*10.0
            target_y = round(random.randint(0,height-snake_size)/10.0) * 10.0


        clock.tick(snake_speed)

    pygame.quit()
    quit()



if __name__=="__main__":
    # target_x = round(random.randrange(0,width-snake_size)/10.0) * 10.0
    # target_y = round(random.randint(0,height-snake_size)/10.0) * 10.0
    # print(target_x,target_y)
    print("Snake Game ")
    run_game()
    

