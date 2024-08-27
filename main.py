from game import Game


def main():
    print("Welcome to Snake!")
    print("Enter game speed: ")
    speed = input()
    x = int(input("Width of grid: "))
    y = int(input("Height of grid: "))
    game = Game(grid_size=(x, y))
    game.start(speed)


if __name__ == '__main__':
    main()