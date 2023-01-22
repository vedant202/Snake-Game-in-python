import pygame
from random import randint
from numpy import sqrt

pygame.init()

done = False

# define colors
white = (255,255,255)
black = (0,0,0)
orange = (255,165,0)
red = (255,0,0)
blue = (0, 0, 255)

width,height = 600,500
cols = 25
rows = 25
wr = width/cols
hr = height/rows
direction = 1


game_display = pygame.display.set_mode([width,height])
pygame.display.set_caption("Vedant's A* Star Snake Game")

clock = pygame.time.Clock()

message_font = pygame.font.SysFont('ubuntu',30)
score_font = pygame.font.SysFont('ubuntu',25)

def get_path(food,snake):
    food.cameFrom = []

    for s in snake:
        s.cameFrom = []

    openSet = [snake[-1]]
    closedSet = []

    dir_arr1 = []

    while 1:
        current1 = min(openSet,key=lambda x:x.f)
        openSet = [openSet[i] for i in range(len(openSet)) if not openSet[i] == current1]
        closedSet.append(current1)

        for neighbor in current1.neighbors:
            if neighbor not in closedSet and neighbor not in snake:
                tempg = neighbor.g+1
                if neighbor in openSet:
                    if tempg < neighbor.g:
                        neighbor.g = tempg
                else:
                    neighbor.g = tempg
                    openSet.append(neighbor)

                neighbor.h = sqrt((neighbor.x - food.x) ** 2 + (neighbor.y - food.y)**2)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.cameFrom = current1


        if current1 == food:
            break
        
    while current1.cameFrom:

        if current1.x == current1.cameFrom.x and current1.y < current1.cameFrom.y:
            dir_arr1.append(2)
        elif current1.x == current1.cameFrom.x and current1.y > current1.cameFrom.y:
            dir_arr1.append(0)
        elif current1.x < current1.cameFrom.x and current1.y == current1.cameFrom.y:
            dir_arr1.append(3)
        elif current1.x > current1.cameFrom.x and current1.y == current1.cameFrom.y:
            dir_arr1.append(1)

        current1 = current1.cameFrom
    print(dir_arr1)
    for i in range(rows):
        for j in range(cols):
            grid[i][j].cameFrom = []
            grid[i][j].f = 0
            grid[i][j].h = 0
            grid[i][j].g = 0

    return dir_arr1

def print_score(score):
        text = score_font.render("Score "+str(score),True,orange)
        game_display.blit(text,[0,0])

class Spot:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.cameFrom = []
        
    

    def draw_snake(self,color):
        pygame.draw.rect(game_display,color,[self.x*hr+2,self.y*wr+2,hr-4,wr-4])

    def add_neighbors(self):
        if self.x>0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y>0:
            self.neighbors.append(grid[self.x][self.y-1])
        if self.x < rows-1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.y <cols-1:
            self.neighbors.append(grid[self.x][self.y+1])

grid = [[Spot(row,col) for col in range(cols)] for row in range(rows)]

#Adding neighbors
for i in range(rows):
    for j in range(cols):
        grid[i][j].add_neighbors()

# printing neighbors
# print([(i.x,i.y) for i in grid[0][0].neighbors])

snake = [grid[round(rows/2)][round(cols/2)]]
food = grid[randint(0,rows-1)][randint(0,cols-1)]

print(snake[0].x,snake[0].y)
print("food ",food.x,food.y)

current = snake[-1]
dir_arr = get_path(food,snake)

food_array = [food]
score = 0


while not done:

    clock.tick(12)
    game_display.fill(black)
    print_score(score)

    direction = dir_arr.pop(-1)

    if direction == 0:    # right
        snake.append(grid[current.x][current.y + 1])
    elif direction == 1:  # down
        snake.append(grid[current.x + 1][current.y])
    elif direction == 2:  # left
        snake.append(grid[current.x][current.y - 1])
    elif direction == 3:  # up
        snake.append(grid[current.x - 1][current.y])

    current = snake[-1]

    if current.x == food.x and current.y == food.y:
        while 1:
            food = grid[randint(0, rows - 1)][randint(0, cols - 1)]
            if not food in snake:
                break
        score += 1
        print_score(score)
        food_array.append(food)
        dir_arr = get_path(food, snake)

    else:
        snake.pop(0)
    
    for spot in snake:
        spot.draw_snake(white)

    food.draw_snake(orange)
    snake[-1].draw_snake(blue)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not direction == 0:
                direction = 2
            elif event.key == pygame.K_a and not direction == 1:
                direction = 3
            elif event.key == pygame.K_s and not direction == 2:
                direction = 0
            elif event.key == pygame.K_d and not direction == 3:
                direction = 1
