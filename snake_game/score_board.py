from turtle import Turtle
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            data = file.read()
            data2 = data.strip().split()
            print(data2[0])
            print(int(data2[1]))
            self.player = data2[0]
            self.high_score_player = data2[0]
            self.high_score = int(data2[1])
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 270)
        self.write(f'Score: {self.score}', align="center", font=("Arial", 20, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.update_score()

    def write_data(self):
       if self.high_score<self.score:
          with open("data.txt", "w") as file:
             file.write(f'{self.player} {self.score}')



    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write(f'Game Over', align="center", font=("Arial", 20, "normal"))
        self.goto(0, -35)
        self.write(f'High Score :{self.high_score}',align='center',font=('Arial',20,'normal'))
        self.goto(0,-60)
        self.write(f'player :{self.high_score_player}',align='center',font=('Arial',20,'normal'))

        time.sleep(5)


        # self.write(f'TOP PLAYER {self.player}', align="center", font=("Arial", 20, "normal"))
        # self.update_score()


