from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)
        self.go_up()

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)



