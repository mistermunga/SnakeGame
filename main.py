from game import Game


def main():
    print("Welcome to Snake!")
    print("Enter game speed: ")
    speed = input()
    game = Game(grid_size=(30, 15))
    game.start(speed)


if __name__ == '__main__':
    main()