from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def add_tail(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.squares.append(new_square)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_tail(position)

    def move(self):
        for seg_number in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[seg_number - 1].xcor()
            new_y = self.squares[seg_number - 1].ycor()
            self.squares[seg_number].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)
        # self.squares[0].left(90)

    def extend(self):
        self.add_tail(self.squares[-1].position())

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
