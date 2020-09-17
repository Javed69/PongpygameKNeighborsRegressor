'''
Created on Wed Sept 9 05:23 2020
@author: Khan Javed Hakim
'''

import pygame
import pandas as pd

#global Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 15
FRAMERATE = 35

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
        pygame.draw.circle(screen, colour, (self.x,self.y),Ball.RADIUS)

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
            self.x = newx
            self.y = newy
            self.show(fgcolor)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        pygame.draw.rect(screen, colour, pygame.Rect
                         (WIDTH - self.WIDTH, self.y - self.HEIGHT // 2, self.WIDTH, self.HEIGHT))

    def update(self):
        newy = pygame.mouse.get_pos()[1]
        if newy - self.HEIGHT // 2 > BORDER  and newy + self.HEIGHT // 2 < HEIGHT - BORDER:
            self.show(bgcolor)
            self.y = newy
            self.show(fgcolor)



# Draw the scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgcolor = pygame.Color("black")
fgcolor = pygame.Color("White")

# Filling the background
screen.fill(bgcolor)

# drawing the walls
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgcolor, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))

# draw the ball and the paddle

ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH,HEIGHT // 2, -VELOCITY, -VELOCITY)
ball.show(fgcolor)

paddle = Paddle(HEIGHT//2)
paddle.show(fgcolor)
 
Clock = pygame.time.Clock()

#sample = open("game.csv","w")

#print("x,y,vx,vy,Paddle.y" , file=sample)

#pong = pd.read_csv('game.csv')
#pong = pong.drop_duplicates()

#X = pong.drop(columns='Paddle.y')
#y = pong['Paddle.y']

#from sklearn.neighbors import KNeighborsRegressor

#clf = KNeighborsRegressor(n_neighbors=3)
#clf = clf.fit(X, y)

#df = pd.DataFrame(columns=['x','y','vx','vy'])

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    Clock.tick(FRAMERATE)
    # visualise the changes you just made
    pygame.display.flip()
    #toPredict = df.append({'x':ball.x,'y':ball.y,'vx':ball.vx,'vy':ball.y},ignore_index=True)
    #shouldMove = clf.predict(toPredict)
    paddle.update()

    ball.update()

pygame.quit()
