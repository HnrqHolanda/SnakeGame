from snake import Snake
from score import Score
from turtle import Screen, Turtle
from scoreboard import ScoreBoard
import time


tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.tracer(0)

pedro = Snake()

tela.listen()

tela.onkey(pedro.up, "Up")
tela.onkey(pedro.down, "Down")
tela.onkey(pedro.left, "Left")
tela.onkey(pedro.right, "Right")

game_is_on = True


newScore = Score()
ScoreBoard = ScoreBoard()


while game_is_on:
    tela.update()
    time.sleep(0.1)
    pedro.snake_move()
    if(pedro.head.distance(newScore.ball) < 15):
        newScore.spawnScore()
        pedro.snake_update()
        ScoreBoard.plusCounter()
    
    if(pedro.head.xcor() > 290 or pedro.head.xcor() < -290 or pedro.head.ycor() > 290 or pedro.head.ycor() < - 290 ):
        game_is_on = False

    for i in  range(1, len(pedro.segments)):
        if(pedro.head.distance(pedro.segments[i]) < 15):
            game_is_on = False

gameOver = Turtle()
gameOver.color("white")
gameOver.hideturtle()
gameOver.write("Game Over", align="center", font=('Arial', 20, 'normal'))

tela.exitonclick()