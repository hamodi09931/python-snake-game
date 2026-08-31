from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 36, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#ffff00")  # Bright yellow for score text
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.color("#ff0000")  # Bright red for game over
        self.write("GAME OVER", align=ALIGN, font=GAME_OVER_FONT)
        self.goto(0, -30)
        self.color("#ffff00")  # Yellow for final score
        self.write(f"Final Score: {self.score}", align=ALIGN, font=FONT)
        
    def score_point(self):
        self.score += 1
        self.clear()
        self.update_score()