from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Colors for enhanced UI
HEAD_COLOR = "#00ff00"  # Bright green for snake head
BODY_COLOR = "#00cc00"  # Darker green for snake body

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.High_Score = 0
        self.Score = 0
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        # Head is bright green, body segments are darker green
        if len(self.segments) == 0:
            new_segment.color(HEAD_COLOR)  # Head color
        else:
            new_segment.color(BODY_COLOR)  # Body color
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.head = self.segments[0]
        
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def Move(self):
        for seg_num in range (len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        

    
    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
       