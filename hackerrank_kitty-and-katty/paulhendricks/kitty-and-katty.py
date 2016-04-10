#!/bin/python3


def main():
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        if n == 1:
            print("Kitty")
        elif n > 1:
            if n % 2 == 0:
                print("Kitty")
            else:
                print("Katty")
        else:
            print("Error!")


if __name__ == '__main__':
    main()
