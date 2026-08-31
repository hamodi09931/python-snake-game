from turtle import Turtle

# Border corner positions for visual wall representation
CORNER_LIST = [(-260, 260), (260, 260), (-260, -260), (260, -260), (-260, 220), (260, 260), (-260, -260), (260, -260)]

class Deat(Turtle):
    def __init__(self):
        super().__init__()
        self.ALL_LIST = [CORNER_LIST]
        
    def goin_posiuon(self):
        for direction_list in self.ALL_LIST:
            for pos in direction_list:
                self.criet_turtle(pos)

    def criet_turtle(self, posuton):
        new_turtle = Turtle("square")
        new_turtle.color("#00ffff")  # Bright cyan for border/walls
        new_turtle.penup()
        new_turtle.goto(posuton)
        