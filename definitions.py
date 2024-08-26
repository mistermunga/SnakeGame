from random import choice


class Apple:
    def __init__(self):
        self.position = None

    def popup(self, invalids: [tuple], dimensions: tuple) -> tuple:
        valids = [(x, y)
                  for x in range(dimensions[0])
                  for y in range(dimensions[1])
                  if (x, y) not in invalids]

        self.position = choice(valids)
        return self.position


class Snake:
    def __init__(self, initial_pos: tuple):
        self.head = initial_pos
        self.length = 1
        self.path = [initial_pos]

    def move(self, direction):

        self.path.append(self.head)

        x, y = self.head
        if direction == 'up':
            self.head = (x, y - 1)
        elif direction == 'down':
            self.head = (x, y + 1)
        elif direction == 'left':
            self.head = (x - 1, y)
        elif direction == 'right':
            self.head = (x + 1, y)

        if len(self.path) > self.length:
            self.path.pop(0)
