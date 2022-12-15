from stanfordkarel import *

def main():
    """"karel code goes here"""
    for i in range(4):
        put_five_beepers()
        move_to_next_corner()

def move_to_next_corner():
    move()
    move()
    move()
    turn_left()


def put_five_beepers():
    for i in range(5):
        put_beeper()

if __name__ == "__main__":
    run_karel_program()
