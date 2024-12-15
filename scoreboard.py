from turtle import Turtle

def incrementar():
        caminho = "data/high_score.txt"

        with open(caminho, 'r') as arquivo:
            high_score = arquivo.read().strip()

        try:
            hs = int(high_score)

        except ValueError:
            print("Conteúdo não válido")

        hs = hs + 1

        with open(caminho, 'w') as arquivo:
            arquivo.write(str(hs))

def read():
        caminho = "data/high_score.txt"
        with open(caminho, 'r') as arquivo:
            high_score = arquivo.read().strip()

        try:
            hs = int(high_score)

        except ValueError:
            print("Conteúdo não válido")

        return hs

class ScoreBoard:
    def __init__(self):
        self.counter = 0
        self.highscore = read()
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(0, 270)
        self.turtle.write(f"Score: {self.counter}       HighScore: {self.highscore}", align="center", font=('Arial', 20, 'normal'))
        self.turtle.hideturtle()
        

    

    def plusCounter(self):
        self.counter += 1
        if(self.counter > read()):
             incrementar()
        self.highscore = read()
        self.turtle.clear()
        self.turtle.write(f"Score: {self.counter}       HighScore: {self.highscore}", align="center", font=('Arial', 20, 'normal'))