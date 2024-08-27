from definitions import Apple, Snake
import time
import threading
import keyboard
import sys


class Game:
    def __init__(self, grid_size: tuple):
        self.grid_size = grid_size
        self.apple = Apple()
        self.snake = Snake(initial_pos=(grid_size[0] // 2, grid_size[1] // 2))
        self.apple.popup(invalids=self.snake.path, dimensions=self.grid_size)
        self.game_over = False
        self.score = 0
        self.direction = 'right'

    def update(self):
        if self.game_over:
            return

        self.snake.move(self.direction)

        # Check for collisions with walls
        if (self.snake.head[0] < 0 or self.snake.head[0] >= self.grid_size[0] or
            self.snake.head[1] < 0 or self.snake.head[1] >= self.grid_size[1]):
            self.game_over = True
            print("Game Over: You hit a wall.")

        # Check for collisions with itself
        if self.snake.head in self.snake.path[:-1]:
            self.game_over = True
            print("Game Over: You ran into yourself.")

        # Check if the snake eats the apple
        if self.snake.head == self.apple.position:
            self.score += 1
            self.snake.length += 1
            self.apple.popup(invalids=self.snake.path, dimensions=self.grid_size)

    def render(self):
        grid = [['_' for _ in range(self.grid_size[0])] for _ in range(self.grid_size[1])]

        ax, ay = self.apple.position
        grid[ay][ax] = 'A'

        for (sx, sy) in self.snake.path[1:]:
            grid[sy][sx] = 'S'

        # Place the snake's head
        sx, sy = self.snake.head
        grid[sy][sx] = 'H'

        for row in grid:
            print(' '.join(row))

        print(f"Score: {self.score}\n")

    def game_loop(self, speed: float):
        while not self.game_over:

            self.update()
            self.render()
            time.sleep(speed)

        sys.exit()

    def start(self, speed: str):
        input_thread = threading.Thread(target=self.get_input)
        input_thread.start()
        speed = float(speed)
        if speed < 0.1:
            print("Speed value too low, set it higher")
            return
        if speed >= 2:
            print("Game will be exceptionally slow.")
            confirm = input("are you sure you wish to proceed? (y/n) ")
            if confirm != 'y':
                return
        self.game_loop(speed)

    def get_input(self):
        while not self.game_over:
            if keyboard.is_pressed('up') and self.direction != 'down':
                self.direction = 'up'
            elif keyboard.is_pressed('down') and self.direction != 'up':
                self.direction = 'down'
            elif keyboard.is_pressed('left') and self.direction != 'right':
                self.direction = 'left'
            elif keyboard.is_pressed('right') and self.direction != 'left':
                self.direction = 'right'
            time.sleep(0.1)  # To prevent excessive CPU usage



