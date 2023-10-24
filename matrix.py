import pygame
import sys
from collections import deque

# Define the Square class
class Square:
    def __init__(self, color, x, y, click):
        self.color = color
        self.x = x
        self.y = y
        self.click = click
        self.visited = False

    def set_color(self, color):
        self.color = color

class Bot:
    def __init__(self, x, y):
        self.image = CHARACTER
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def get_center(self):
        self.center = [self.x + 3*SQUARE_SIZE//2, self.y + SQUARE_SIZE // 2]
    def move_down(self):
        self.y +=1
    def move_up(self):
        self.y -=1
    def move_r(self):
        self.x += 1
    def move_l(self):
        self.x -= 1

def check_all_directions(maze, square):
    possible = []
    if square.x > 0 and maze[square.x - 1][square.y].color == RED:
        # possible.append(f"Upwards path was found at {square.x - 1}, {square.y}")
        # possible.append((square.x - 1,square.y))
        possible.append((square.x-1,square.y))
    if square.x < GRID_WIDTH - 1 and maze[square.x + 1][square.y].color == RED:
        # possible.append(f"Downwards path was found at {square.x+ 1} {square.y}")
        # possible.append((square.x+ 1,square.y))
        possible.append((square.x+1, square.y))
    if square.y > 0 and maze[square.x][square.y - 1].color == RED:
        # possible.append(f"Leftwards path was found at {square.x},{square.y-1}")
        # possible.append((square.x,square.y-1))
        possible.append((square.x,square.y-1))
    if square.y < GRID_HEIGHT - 1 and maze[square.x][square.y + 1].color == RED:
        # possible.append(f"Rightwards path was found at {square.x}, {square.y + 1}")
        # possible.append((square.x,square.y + 1))
        possible.append((square.x,square.y+1))
    print(possible)
    return possible
def move(maze,square):
    paths = []

    t = (check_all_directions(maze,square))
    paths.append(t)
    pointer = 0
    if len(paths) > 0:
        temp = (check_all_directions(maze,paths[pointer]))
        pointer+=1
        paths.append(temp)
        if len(temp) > 0:
            return paths
    else:
        return paths





# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 10
SQUARE_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10
SCREEN_WIDTH = GRID_WIDTH * SQUARE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * SQUARE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CHARACTER = pygame.image.load("Bot.jpg")
# CHARACTER = pygame.transform.scale(character, (3 * SQUARE_SIZE, SQUARE_SIZE))
# character_rect = character.get_rect()
bot = Bot(-1250, -1250)
# character_rect.center = (-25, -25)
speed = 2
clock = pygame.time.Clock()
# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid of Squares")
search_for_truth = []
# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, SQUARE_SIZE):
        for y in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)


# Create a 2D list of squares and initialize them with default color
grid = [[Square(WHITE, x, y, 0) for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]
running = True
bot_x = 0
bot_y = 0
clock = pygame.time.Clock()
green = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x = x // SQUARE_SIZE
            grid_y = y // SQUARE_SIZE
            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                square = grid[grid_y][grid_x]
                square.click += 1
                for row in grid:
                    for obj in row:
                        if obj.x != grid_x or obj.y != grid_y:
                            obj.click = 0
                if square.click == 1:
                    square.color = RED
                if square.click == 3 and square.color == RED and bot_x == 0 and bot_y == 0:
                    square.set_color(GREEN)
                    tempx = square.x * 50 - 50
                    tempy = square.y * 50
                    bot.draw(screen)
                if square.click == 5:
                    square.color = BLACK
    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_RETURN]:
        bot.x = tempx
        bot.y = tempy
    
    # print(len(grid),len(grid[0]))
    for y, rown in enumerate(grid):
        for x, square in enumerate(rown):
           if square == GREEN:
                coordinates = check_all_directions(grid, square)
                print(coordinates )
        
                if coordinates:
                    adj_x, adj_y = coordinates[0]  # Get the coordinates of the adjacent square

                    if bot.x + 25 < adj_x * 50 + 25:
                        bot.move_r()
                    elif bot.x + 25 > adj_x * 50 + 25:
                        bot.move_l()
                    elif bot.y + 25 < adj_y * 50 + 25:
                        bot.move_down()
                    elif bot.y + 25 > adj_y * 50 + 25:
                        bot.move_up()

                    square.color = BLACK
                    grid[adj_y][adj_x].color = GREEN
            
    


    bot.draw(screen)
    screen.fill(BLACK)
    draw_grid()

    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            pygame.draw.rect(screen, BLACK, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, square.color, (x * SQUARE_SIZE + 1, y * SQUARE_SIZE + 1, SQUARE_SIZE - 2, SQUARE_SIZE - 2))
    bot.draw(screen)
    pygame.draw.circle(screen, BLACK, (bot.x+25, bot.y+25),5)
    pygame.draw.circle(screen, BLACK, (bot.x+75, bot.y+25),5)
    pygame.draw.circle(screen, BLACK, (bot.x+125, bot.y+25),5)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

