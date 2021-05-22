from turtle import Turtle
POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
IS_GAME = True
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.draw()
        self.head = self.segments[0]

    def draw(self):
        for ran in POSTIONS:
          self.add_segment(ran)

    def add_segment(self,postions):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(postions)
            self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        # POSTIONS.append(self.segments[-1].position)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
