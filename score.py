from turtle import Turtle
from random import randint

class Score:

    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.ball = Turtle("circle")
        self.ball.color("blue")
        self.ball.penup()
        self.ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.spawnScore()

    def spawnScore(self):
        self.xc = randint(-280, 280)
        self.yc = randint(-280, 280)
        self.ball.goto((self.xc, self.yc))
        
