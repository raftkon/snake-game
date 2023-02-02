from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self) -> None:
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # def expand_snake(self):
    #     tail = self.segments[-1]
    #     almost_tail = self.segments[-2]
    #     new_segment = Turtle('square')
    #     new_segment.penup()
    #     new_segment.color('white')
    #     if tail.xcor() > almost_tail.xcor():
    #         new_segment.goto(x=tail.xcor()+20, y=tail.ycor())
    #     elif tail.xcor() < almost_tail.xcor():
    #         new_segment.goto(x=tail.xcor()-20, y=tail.ycor())

    #     elif tail.ycor() < almost_tail.ycor():
    #         new_segment.goto(x=tail.xcor(), y=tail.ycor()-20)

    #     elif tail.ycor() > almost_tail.ycor():
    #         new_segment.goto(x=tail.xcor()+20, y=tail.ycor()+20)
    #     self.segments.append(new_segment)
