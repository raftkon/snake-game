from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
SMALL_FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(f"Your score is: {self.score}",
                   align=ALIGNMENT, font=SMALL_FONT)
