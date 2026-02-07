import random
from turtle import Turtle, colormode
colormode(255)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.2)
        self.penup()
        self.set_color(self.get_random_color())
        self.speed("fastest")
        self.refresh()


    def get_random_color(self):
        """Generates a random RGB color tuple."""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)
    def set_color(self, color):
        self.color(color)

    def refresh(self):
        self.set_color(self.get_random_color())
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)


