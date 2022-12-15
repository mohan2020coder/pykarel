from stanfordkarel import *


def main():
    """ Karel code goes here! """
    turn_left()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def fill_pothole():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()

if __name__ == "__main__":
    run_karel_program()
