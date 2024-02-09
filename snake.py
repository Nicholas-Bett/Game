from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.b_segments = []
        self.c_snake()
        self.head = self.b_segments[0]

    def c_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.b_segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.b_segments[-1].position())

    def move(self):

        for segment_index in range(len(self.b_segments) - 1, 0, -1):
            new_x = self.b_segments[segment_index - 1].xcor()
            new_y = self.b_segments[segment_index - 1].ycor()
            self.b_segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.b_segments[0].heading() != 270:
            self.b_segments[0].setheading(90)

    def down(self):
        if self.b_segments[0].heading() != 90:
            self.b_segments[0].setheading(270)

    def left(self):
        if self.b_segments[0].heading() != 0:
            self.b_segments[0].setheading(180)

    def right(self):
        if self.b_segments[0].heading() != 180:
            self.b_segments[0].setheading(0)

    def x_boundary(self):
        self.b_segments[0].goto(self.b_segments[0].xcor()*-1, self.b_segments[0].ycor())

    def y_boundary(self):
        self.b_segments[0].goto(self.b_segments[0].xcor(), self.b_segments[0].ycor()*-1)
