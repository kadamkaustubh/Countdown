import turtle

folds = 10
stack = []
for i in range(folds):
    if i == 0:
        stack.append(1)
    else:
        temp_stack = list(map(lambda x: -1 * x, stack))
        temp_stack.reverse()
        stack.extend(temp_stack)
        stack.insert(int(len(stack) / 2), 1)


class ColorDragon(turtle.Turtle):
    def __init__(self, color, step_size, orientation):
        super().__init__()
        self.pencolor(color)
        self.speed(0)
        self.setheading(orientation)
        self.forward(step_size)
        self.forward_distance = step_size

    def right_turn(self):
        self.right(90)
        self.forward(self.forward_distance)

    def left_turn(self):
        self.left(90)
        self.forward(self.forward_distance)


screen = turtle.Screen()
screen.screensize(2000, 2000)
dist = 10
red_dragon = ColorDragon('red', dist, 0)
green_dragon = ColorDragon('green', dist, 90)
blue_dragon = ColorDragon('blue', dist, 180)
black_dragon = ColorDragon('black', dist, 270)

for i in stack:
    if i == 1:
        red_dragon.right_turn()
        green_dragon.right_turn()
        blue_dragon.right_turn()
        black_dragon.right_turn()
    else:
        red_dragon.left_turn()
        green_dragon.left_turn()
        blue_dragon.left_turn()
        black_dragon.left_turn()

screen.exitonclick()
