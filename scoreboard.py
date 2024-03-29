from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(arg=f"Score : {self.score}", move=False, align="left", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align="left", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_board()
