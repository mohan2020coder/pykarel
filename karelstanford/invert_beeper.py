from stanfordkarel import *

#load invert beeper world for this program

def main():
    """"karel code goes here"""
    while front_is_clear():
        invert_beeper()
        move()
    invert_beeper()

def invert_beeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()




if __name__ == "__main__":
    run_karel_program()
