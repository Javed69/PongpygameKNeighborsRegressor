'''
Created on Wed Sept 9 05:23 2020
@author: Khan Javed Hakim
'''

import pygame


# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 15
FRAMERATE = 35
paddle
newx
newy

# define my classes


class Ball:
    RADIUS = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour, (self.x, self.y), Ball.RADIUS)

    def update(self):
        global bgcolor, fgcolor

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER + Ball.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + Ball.RADIUS or newy > HEIGHT - BORDER - Ball.RADIUS:
            self.vy = -self.vy
        elif newx + Ball.RADIUS > WIDTH - Paddle.WIDTH and abs(newy - paddle.y) < Paddle.HEIGHT // 2:
            self.vx = - self.vx
        else:
            self.show(bgcolor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgcolor)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        global screen
        pygame.draw.rect(screen, colour, pygame.Rect
                         (WIDTH - self.WIDTH, self.y - self.HEIGHT // 2, self.WIDTH, self.HEIGHT))

    def update(self):
        self.y = pygame.mouse.get_pos()[1]
        if newy - self.HEIGHT // 2 > BORDER and newy + self.HEIGHT // 2 < HEIGHT - BORDER:
            self.show(bgcolor)
            self.y = newy
            self.show(fgcolor)


# create objects:


ballplay = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)

# Draw the scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgcolor = pygame.Color("black")
fgcolor = pygame.Color("White")

# Filling the background
screen.fill(bgcolor)

pygame.draw.rect(screen, fgcolor, pygame.Rect((0, 0, WIDTH, BORDER)))
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))

# draw the ball and the paddle

ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH,
            HEIGHT // 2, -VELOCITY, -VELOCITY)
ball.show(fgcolor)

Clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)
    # visualise the changes you just made
    pygame.display.flip()
    paddle.update()
    ball.update()

pygame.quit()
