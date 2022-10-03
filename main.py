from Scripts.drawner import Drawner
from Scripts.system import System


def main():
    drawner = Drawner()

    system = System(game=drawner)
    system.update()

    drawner.run()


if __name__ == '__main__':
    main()
