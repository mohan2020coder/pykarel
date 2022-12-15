from stanfordkarel import *

def main():
    """"karel code goes here"""
    move()
    drop_beeper_two_compact()
    drop_beeper_two()
    turn_left()
    drop_beeper_two_compact()
    drop_beeper_two()
    turn_left()
    drop_beeper_two_compact()
    drop_beeper_two()
    turn_left()
    drop_beeper_two_compact()
    drop_beeper_two()
    turn_around()
    turn_right()
    move_two()
    move()
    turn_left()
    move_two()
    move()
    turn_right()


def drop_beeper_two():
    for i in range(2):
        put_beeper()

def move_two():
    move()
    move()


def drop_beeper_two_compact():
    drop_beeper_two()
    move_two()
    drop_beeper_two()
    move_two()
    drop_beeper_two()
    move_two()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
