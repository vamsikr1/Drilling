from turtle import Turtle,Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Processing():
    def __init__(self):
        self.dots=[]
        self.create_dot()
        self.move_dots()
    def create_dot(self):
        for position in STARTING_POSITIONS:
            new_dot=Turtle()
            new_dot.shape("circle")
            new_dot.color("white")
            new_dot.penup()
            new_dot.goto(position)
            self.dots.append(new_dot)
    def move_dots(self):
        for dot_num in range(len(self.dots)-1,0,-1):
            new_x = self.dots[dot_num - 1].xcor()
            new_y = self.dots[dot_num - 1].ycor()
            self.dots[dot_num].goto(new_x, new_y)
        self.dots[0].setheading(45)
        self.dots[0].forward(MOVE_DISTANCE)
