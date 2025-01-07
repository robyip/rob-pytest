import os

import modules.clock as cl


def main():
    filename = os.path.basename(__file__)
    print(f'Hello from src ')

    cl.main()

if __name__ == "__main__":
    main()