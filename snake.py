from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color('white')
        turtle.shapesize(stretch_wid=1, stretch_len=1)
        turtle.penup()
        turtle.goto(position)
        self.snake_segment.append(turtle)

    def snake_reset(self):
        for seg in self.snake_segment:
            seg.goto(1000,1000)
        self.snake_segment.clear()
        self.create_snake()
        self.head = self.snake_segment[0]

    def extend(self):
        self.add_segment(self.snake_segment[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
