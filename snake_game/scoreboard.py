from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        self.BASE_DIR = os.path.dirname(__file__)
        self.data_path = os.path.join(self.BASE_DIR, "data.txt")
        try:
            with open(self.data_path) as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            with open(self.data_path, "w") as data:
                data.write("0")
        
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.data_path, "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

