import pygame
import sys



class GreenFlag:
    def __init__(self,x, y):
        self.image = IMAGE
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))
    def move(self):
        self.x += 1
        self.draw(screen)
    





pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
WHITE = (255, 255, 255)

GRID_SIZE = 50  # Adjust the size of the grid squares as needed
GRID_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Image")


IMAGE = pygame.image.load("bot.jpg")
# image_rect = image.get_rect()


# x = 0
# y = SCREEN_HEIGHT // 2 - image_rect.height // 2

# Speed of movement
speed = 2

running = True
clock = pygame.time.Clock()

while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    screen.fill(WHITE)
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))
    user = pygame.key.get_pressed()
    if user[pygame.K_UP]:
        flag = GreenFlag(50,50)
    try:
        flag.draw(screen)
        if flag.x < 150:
            flag.move()
            flag.draw(screen)
    except:
        pass

        
    pygame.display.flip()



pygame.quit()
sys.exit()
