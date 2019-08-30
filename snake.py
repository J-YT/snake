import pygame
import random


class Fruit:
    def __init__(self):
        self.color = (255, 0, 0)
        crash = True
        while crash:
            self.x = random.randrange(0, scr_width, scale)
            self.y = random.randrange(0, scr_height, scale)
            crash = False
            for j in snake.location:
                if j[0]==self.x and j[1]==self.y:
                    crash = True

    def ate(self):
        crash = True
        while crash:
            self.x = random.randrange(0, scr_width, scale)
            self.y = random.randrange(0, scr_height, scale)
            crash = False
            for j in snake.location:
                if j[0]==self.x and j[1]==self.y:
                    crash = True


class Snake:
    def __init__(self):
        self.x = scale
        self.y = scale
        self.speedx = speed
        self.speedy = 0
        self.location=[]
        self.location.append([self.x, self.y])
        self.ate = False
        self.color = (255,255,255)
        self.die = False

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        # constrain x and y
        if self.x > scr_width - scale:
            # self.x = scr_width - scale
            self.die = True
        if self.y > scr_height - scale:
            # self.y = scr_height - scale
            self.die = True
        if self.x < 0:
            # self.x = 0
            self.die = True
        if self.y < 0:
            # self.y = 0
            self.die = True
        for loc in self.location:
            if self.x == loc[0] and self.y == loc[1]:
                self.die = True

        self.location.append([self.x, self.y])
        if not self.ate:
            self.location = self.location[1:]
        else:
            fruit.ate()
            self.ate = False

    def eat(self):
        self.ate = True


scale = 30
speed = 1*scale
scr_width = scale*scale
scr_height = scale*scale
dt = pygame.time.Clock()
done = False
pygame.init()
screen = pygame.display.set_mode((scr_width, scr_height))
snake = Snake()
fruit = Fruit()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if snake.speedy == 0:
                snake.speedx = 0
                snake.speedy = -speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if snake.speedy == 0:
                snake.speedx = 0
                snake.speedy = speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if snake.speedx == 0:
                snake.speedx = speed
                snake.speedy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if snake.speedx == 0:
                snake.speedx = -speed
                snake.speedy = 0

    # eat fruit
    if snake.x == fruit.x and snake.y == fruit.y:
        snake.eat()

    snake.update()
    done = snake.die
    # draw rect
    screen.fill((0,0,0))
    for i in snake.location:
        pygame.draw.rect(screen, snake.color, pygame.Rect(i[0], i[1], scale, scale))
    pygame.draw.rect(screen, fruit.color, pygame.Rect(fruit.x, fruit.y, scale, scale))

    pygame.display.flip()

    dt.tick(10)
