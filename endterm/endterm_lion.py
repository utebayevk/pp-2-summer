import pygame 
import random
from pygame.locals import *
import sys


white = (255, 255, 255)
black = (0,   0,   0  )
red   = (255, 0,   0  )
green = (0,   255, 0  )
blue  = (0,   0,   255) 

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hungry lion")

FPS = 60
clock = pygame.time.Clock()

x, y = 100, 100
dx, dy = 5, 5

class Food:
    def __init__(self, where1):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.y2 = 620
        self.x2 = random.randint(0, 800)
        self.dy = 1
        self.color = green
        self.width = 28
        self.height = 20
        self.where = where1
        self.rect = Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        if self.where == True:
            self.rect = Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, self.rect)
        if self.where == False:
            self.rect = Rect(self.x2, self.y2, self.width, self.height)
            pygame.draw.rect(screen, self.color, self.rect)
    def move(self):
        self.y -= self.dy
        if self.y < -20:
            self.y = random.randint(620, 640)
            self.x = random.randint(0, 770)
        self.y2 -= self.dy
        if self.y2 < -20:
            self.y2 = random.randint(620, 640)
            self.x2 = random.randint(0, 770)
    
class gamer:
    def __init__(self):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = blue
    def draw(self):
        self.rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
    def move(self):
        pass
    
class Enemy:
    def __init__(self, where2):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.y2 = -20
        self.x2 = random.randint(0, 800)
        self.dy = 1.5
        self.width = 28
        self.height = 20
        self.color = red
        self.where = where2
        self.rect = Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        if self.where == True:
            self.rect = Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, (self.rect))
        elif self.where == False:
            self.rect = Rect(self.x2, self.y2, self.width, self.height)
            pygame.draw.rect(screen, self.color, (self.rect))
    def move(self):
        self.y += self.dy
        if self.y > 600: 
            self.y = random.randint(-40, -20)
            self.x = random.randint(0, 770)
        self.y2 += self.dy
        if self.y2 > 600:
            self.y2 = random.randint(-40, -20)
            self.x2 = random.randint(0, 770)
    


enemies = []
foods = []
player = gamer()

for i in range(10):
    food = Food(True)
    foods.append(food)
for i in range(30):
    enemy = Enemy(True)
    enemies.append(enemy)


running = True

score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
    where1 = True
    where2 = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]: player.x += dx 
    if pressed[pygame.K_LEFT]: player.x -= dx
    if pressed[pygame.K_DOWN]: player.y += dy 
    if pressed[pygame.K_UP]: player.y -= dy

    for food in foods:
        food.move()
    for enemy in enemies:
        enemy.move()

    screen.fill(white)

    player.move()
    player.draw()

    for enemy in enemies:
        if pygame.Rect.colliderect(player.rect, enemy.rect):
            score -= 1
            enemies.remove(enemy)
            x = Enemy(False)
            enemies.append(x)
    for food in foods:
        if pygame.Rect.colliderect(player.rect, food.rect):
            score += 1
            foods.remove(food)
            x = Food(False)
            y = Enemy(False)
            foods.append(x)
            enemies.append(y)
            
            
    for food in foods:
        food.draw()
    for enemy in enemies:
        enemy.draw()
    s_score = 'Score: ' + str(score)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(s_score, True, black)
    textRect = text.get_rect()
    textRect.topleft = (10, 10) 
    screen.blit(text, textRect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()