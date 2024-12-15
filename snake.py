STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0



from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            newSegment = Turtle("square")
            newSegment.color("white")
            newSegment.penup()
            newSegment.goto(position)
            self.segments.append(newSegment)

    def snake_move(self):
        for i in range(len(self.segments) -1, -1, -1):
            if(i == 0):
                self.segments[i].penup()
                self.segments[i].forward(20)
            else:
                self.segments[i].penup()
                self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
                self.segments[i].setheading(self.segments[i-1].heading())

    def snake_update(self):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto((self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor()))
        self.segments.append(newSegment)


    def up(self):
        if(self.head.heading() != DOWN):
            self.segments[0].setheading(90)

    def down(self):
        if(self.head.heading() != UP):
            self.segments[0].setheading(270)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.segments[0].setheading(180)
    
    def right(self):
        if(self.head.heading() != LEFT):
            self.segments[0].setheading(0)



