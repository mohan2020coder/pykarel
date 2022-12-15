from stanfordkarel import *

def main():
    """"karel code goes here"""
    while front_is_clear():
            # place a beeper
        put_beeper()

            #move to next square

        move()




if __name__ == "__main__":
    run_karel_program()
