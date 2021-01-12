from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
  def __init__(self):
    self.all_cars = []
    self.place_holder = STARTING_MOVE_DISTANCE

  def create_cars(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      new_cars = Turtle("square")
      new_cars.penup()
      new_cars.shapesize(stretch_wid=1.0,stretch_len = 2.0)
      new_cars.color(random.choice(COLORS))
      random_y = random.randint(-250,250)
      new_cars.goto(x=290,y=random_y)
      self.all_cars.append(new_cars)

  def move_cars(self):
    for cars in self.all_cars:
      cars.backward(self.place_holder)

  def increment_speed(self):
    self.place_holder +=  MOVE_INCREMENT

  
    

  


 



    

  

      
    
    
