from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.goto(x=-70,y=260)
    self.number = 0
    self.hideturtle()
    self.write(f"Score:{self.number}",False, font=FONT)
    
  def add_score(self):
    self.number += 1
    self.clear()
    self.write(f"Score:{self.number}",False, font=FONT)

  def you_lose_screen(self):
    self.clear()
    self.goto(x=-70,y=0)
    self.write("You lose",False, font=FONT)

    
