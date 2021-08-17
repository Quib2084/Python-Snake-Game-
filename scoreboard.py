from turtle import Turtle


class Scoreboard(Turtle):
    FONT_FAMILY = "Courier"
    FONT_SIZE = 20

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write("Score: {}".format(self.score), align="center", font=(self.FONT_FAMILY, self.FONT_SIZE, 'normal'))

    def update(self):
        self.score = self.score + 1
        self.clear()
        self.write("Score: {}".format(self.score), align="center", font=(self.FONT_FAMILY, self.FONT_SIZE, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(self.FONT_FAMILY, self.FONT_SIZE, 'normal'))
