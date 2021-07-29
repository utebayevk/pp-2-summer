import pygame
import random
import sys
# Initialize pygame program
pygame.init()

# Surface
SCREEN_WIDTH, SCREEN_HEIGHT = 950, 950
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Snake")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
BROWN =(150,75,0)

clock = pygame.time.Clock()
# Frames Per Second


color = GREEN
block = 15
dx, dy = block, 0
radius = 10

food_location = random.randint(50, SCREEN_WIDTH), random.randint(50, SCREEN_HEIGHT)

body = [[70, 100], [85, 100], [100, 100]]
# Init
# 1) [70, 100], [85, 100], [100, 100]

# Moving to the right
# 2) [85, 100], [100, 100], [115, 100]

# Moving to the right
# 2) [100, 100], [115, 100], [130, 100]


# Moving to the down
# 3) [100, 100], [115, 100], [115, 115]
running1 =False
start = True
print("Press 1 to play level 1, Press 2 to play level 2\n")
a1= int(input())
# Main loop
while a1==1:
  # Event loop
  FPS = 10
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      a1 = 0
      sys.exit()
    if event.type == pygame.KEYDOWN:
    #   if event.key == pygame.K_SPACE:
    #     body.append([0, 0])
    #     food_location = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
        
      if event.key == pygame.K_RIGHT:
        dx, dy = block, 0
      if event.key == pygame.K_LEFT:
        dx, dy = -block, 0
      if event.key == pygame.K_UP:
        dx, dy = 0, -block
      if event.key == pygame.K_DOWN:
        dx, dy = 0, block
  # Тут можно рисовать
    
  # Move our snake
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0] # x - point
    body[i][1] = body[i - 1][1] # y - point

  body[0][0] += dx
  body[0][1] += dy
  if ((body[0][0]-food_location[0])**2+(body[0][1]-food_location[1])**2)<400:
    body.append([0, 0])
    food_location = random.randint(50, SCREEN_WIDTH), random.randint(50, SCREEN_HEIGHT)
  if body[0][0]<40:
    a1 =0
    sys.exit()
  if body[0][0]>960:
    a1 =0
    sys.exit()
  if body[0][1]<40:
    a1 =0
    sys.exit()
  if body[0][1]>960:
    a1 =0
    sys.exit()
  # if body[0][0] >= SCREEN_WIDTH:
  #   body[0][0] = 0
  # if body[0][0] <= 0:
  #   body[0][0] = SCREEN_WIDTH

  # if body[0][1] >= SCREEN_HEIGHT:
  #   body[0][1] = 0
  # if body[0][1] <= 0:
  #   body[0][1] = SCREEN_HEIGHT

  # Check for collision head of the snake with food location

  screen.fill(GREEN)
  pygame.draw.rect(screen,BROWN,(0,0,1000,1000),50)

  # Draw food
  pygame.draw.circle(screen, WHITE, food_location, radius)


  # Draw snake
  for i, point in enumerate(body):
    color = RED if i == 0 else BLUE
    pygame.draw.circle(screen, color, point, radius)
  # if running1 == False:
  #   fontObj = pygame.font.Font('freesansbold.ttf', 20)
  #   textSurfaceObj = fontObj.render('Press -C to play game,press -Q to quit', True, BLUE)
  #   textSurfaceObj1 = fontObj.render('Press -1 to play level 1,press -2 play level 2', True, BLUE)
  #   textSurfaceObj2 = fontObj.render('Press -R to play saved game', True, BLUE)
  #   textRectObj = textSurfaceObj.get_rect()
  #   textRectObj.center = (250, 100)
  #   textRectObj1 = textSurfaceObj1.get_rect()
  #   textRectObj1.center = (250, 200)
  #   textRectObj2 = textSurfaceObj2.get_rect()
  #   textRectObj2.center = (250, 300)

  #   screen.fill(BROWN)
  #   screen.blit(textSurfaceObj, textRectObj)
  #   screen.blit(textSurfaceObj1, textRectObj1)
  #   screen.blit(textSurfaceObj2, textRectObj2)
  #   pygame.display.flip()
  #   for event in pygame.event.get():
  #     if event.type == pygame.KEYDOWN:
  #       if event.key == pygame.K_q:
  #         running = False
  #       if event.key == pygame.K_1:
  #         a1 = 1
  #       if event.key == pygame.K_2:
  #         a1 = 2
        
  #   running1 = True

  pygame.display.flip()

  clock.tick(FPS)
while a1==2:
  # Event loop
  FPS = 20
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      a1 = 0
      sys.exit()
    if event.type == pygame.KEYDOWN:
    #   if event.key == pygame.K_SPACE:
    #     body.append([0, 0])
    #     food_location = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
        
      if event.key == pygame.K_RIGHT:
        dx, dy = block, 0
      if event.key == pygame.K_LEFT:
        dx, dy = -block, 0
      if event.key == pygame.K_UP:
        dx, dy = 0, -block
      if event.key == pygame.K_DOWN:
        dx, dy = 0, block
  # Тут можно рисовать
    
  # Move our snake
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0] # x - point
    body[i][1] = body[i - 1][1] # y - point

  body[0][0] += dx
  body[0][1] += dy
  if ((body[0][0]-food_location[0])**2+(body[0][1]-food_location[1])**2)<400:
    body.append([0, 0])
    a = random.randint(0,2)
    if a == 1:
      food_location = random.randint(250, 750), random.randint(50, SCREEN_HEIGHT)
    if a == 0:
      food_location = random.randint(50, 150), random.randint(50, SCREEN_HEIGHT)
    if a==2:
      food_location = random.randint(850, 950), random.randint(50, SCREEN_HEIGHT)
  if body[0][0]<40:
    a1 =0
    sys.exit()
  if body[0][0]>960:
    a1 =0
    sys.exit()
  if body[0][1]<40:
    a1 =0
    sys.exit()
  if body[0][1]>960:
    a1 =0
    sys.exit()
  if ((body[0][0]>=200) and (body[0][0]<=250)) and ((body[0][1]>=200) and (body[0][1]<=800)):
    a1 =0
    sys.exit()
  if ((body[0][0]>=800) and (body[0][0]<=850)) and ((body[0][1]>=200) and (body[0][1]<=800)):
    a1 =0
    sys.exit()
  # if body[0][0] >= SCREEN_WIDTH:
  #   body[0][0] = 0
  # if body[0][0] <= 0:
  #   body[0][0] = SCREEN_WIDTH

  # if body[0][1] >= SCREEN_HEIGHT:
  #   body[0][1] = 0
  # if body[0][1] <= 0:
  #   body[0][1] = SCREEN_HEIGHT

  # Check for collision head of the snake with food location

  screen.fill(GREEN)
  pygame.draw.rect(screen,BROWN,(0,0,1000,1000),50)
  pygame.draw.rect(screen,BROWN,(200,200,50,600))
  pygame.draw.rect(screen,BROWN,(800,200,50,600))

  # Draw food
  pygame.draw.circle(screen, WHITE, food_location, radius)


  # Draw snake
  for i, point in enumerate(body):
    color = RED if i == 0 else BLUE
    pygame.draw.circle(screen, color, point, radius)
  pygame.display.flip()

  clock.tick(FPS)

pygame.quit()