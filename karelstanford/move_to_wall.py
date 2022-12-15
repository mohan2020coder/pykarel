from stanfordkarel import *

def main():
    """"karel code goes here"""
    move_to_wall()

def move_to_wall():
    while front_is_clear():
        move()



if __name__ == "__main__":
    run_karel_program()
