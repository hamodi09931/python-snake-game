from turtle import Turtle
# قائمة تحتوي على نقاط في الزوايا الأربعة فقط
CORNER_LIST = [(-260, 260), (260, 260), (-260, -260), (260, -260), (-260, 220), (260, 260), (-260, -260), (260, -260)]
GOOIG = 20

class Deat(Turtle):
    def __init__(self):
        super().__init__()
        self.ALL_LIST = [CORNER_LIST]
        
    def goin_posiuon(self):
        for direction_list in self.ALL_LIST:
            for pos in direction_list:
                self.criet_turtle(pos)
            
                
                
            
        
        
    def criet_turtle (self, posuton):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(posuton)
        