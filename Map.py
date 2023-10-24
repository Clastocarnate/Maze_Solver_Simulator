import pygame
import sys
from collections import deque
import cv2

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
    def __init__(self, image, x,y):
        self.rect = image.get_rect()
        self.rect.center = (x,y)

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
character = pygame.image.load("Bot.jpg")
character = pygame.transform.scale(character, (3*SQUARE_SIZE, SQUARE_SIZE))
character_rect = character.get_rect()

character_rect.center = (-25,-25)
speed = 2
clock = pygame.time.Clock()
# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid of Squares")

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, SQUARE_SIZE):
        for y in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE), 1)

def get_colour(maze):
    for row in maze:
        for square in row:
            print(f"Square at {square.x},{square.y} is {square.color}")

def check_all_directions(maze, square):
    possible = []
    if square.x > 0 and maze[square.x - 1][square.y].color == RED:
        # possible.append(f"Upwards path was found at {square.x - 1}, {square.y}")
        possible.append((square.x - 1,square.y))
    if square.x < GRID_WIDTH - 1 and maze[square.x + 1][square.y].color == RED:
        # possible.append(f"Downwards path was found at {square.x+ 1} {square.y}")
        possible.append((square.x+ 1,square.y))
    if square.y > 0 and maze[square.x][square.y - 1].color == RED:
        # possible.append(f"Leftwards path was found at {square.x},{square.y-1}")
        possible.append((square.x,square.y-1))
    if square.y < GRID_HEIGHT - 1 and maze[square.x][square.y + 1].color == RED:
        # possible.append(f"Rightwards path was found at {square.x}, {square.y + 1}")
        possible.append((square.x,square.y + 1))
    print(possible)
    return possible

def move_green_square(maze, start_x, start_y, end_x, end_y):
    visited = [[False for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        # Check if we reached the destination
        if x == end_x and y == end_y:
            return

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            # Check if the neighbor is a valid grid cell and not visited
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and not visited[nx][ny] and maze[nx][ny].color == RED:
                queue.append((nx, ny))
                visited[nx][ny] = True
                maze[nx][ny].set_color(GREEN)
                pygame.display.flip()
                pygame.time.delay(200)  # Delay for smoother animation (adjust as needed)

# Create a 2D list of squares and initialize them with default color
grid = [[Square(WHITE, x, y, 0) for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]
running = True
bot_x = 0
bot_y = 0
reached_end = False
DFS_start = False
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
                    tx = square.x
                    ty = square.y
                    bot_x, bot_y = grid_x, grid_y
                if square.click == 5:
                    square.color = BLACK
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            for i in grid:
                for j in i:
                    if j.color == GREEN:
                        starting_square = j
                        print(f"Green Found at {j.x},{j.y}")
                        Green_Flag = True
            print("Enter was pressed")
            paths= check_all_directions(grid,starting_square)
            if x > 50:
                the_x += 2
                x+=2
    
            for row in grid:
                for square in row:
                    if square.color == RED:
                        end_x, end_y = square.x, square.y
                        break
           # move_green_square(grid, starting_square.x, starting_square.y, end_x, end_y)



    screen.fill(BLACK)
    draw_grid()

    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            pygame.draw.rect(screen, BLACK, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, square.color, (x * SQUARE_SIZE + 1, y * SQUARE_SIZE + 1, SQUARE_SIZE - 2, SQUARE_SIZE - 2))
            screen.blit(character, character_rect)
            if square.color == GREEN:
                the_x, the_y = (SQUARE_SIZE*square.x+SQUARE_SIZE//2,SQUARE_SIZE*square.y+SQUARE_SIZE//2)
                character_rect.center = (the_x,the_y)
                thy_bot = Bot(character,the_x, the_y)
                while character_rect[0] > 500:
                    character_rect[0] += 2
                    screen.blit(character, character_rect)
                    pygame.draw.rect(screen,GREEN, character_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# get_colour(grid)
print(paths)
sys.exit()

