from game import Game

def main():
    game = Game()
    while game.running():
        game.tick()

if __name__ == '__main__':
    main()