from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
SMALL_FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = self.read_highscore()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(
            f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def read_highscore(self):
        with open('highscore.txt', mode='r') as my_file:
            try:
                return int(my_file.read())
            except Exception:
                return 0

    def write_highscore(self):
        with open("highscore.txt", mode="w") as my_file:
            my_file.write(str(self.high_score))

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    #     self.goto(0, -20)
    #     self.write(f"Your score is: {self.score}",
    #                align=ALIGNMENT, font=SMALL_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = -1
        self.update_score()
        self.write_highscore()
