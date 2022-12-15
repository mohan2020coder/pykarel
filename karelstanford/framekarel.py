# This is an editor! An editor is where you write code.
# Make karel: move, turn_left, move

from stanfordkarel import *


def main():
   move()
   turn_left()
   move()
   # add your code here
   for i in range(5):
      put_beepers()

   turn_right()

   for i in range(4):
      put_beepers()

   turn_right()

   for i in range(5):
      put_beepers()

   turn_right()

   for i in range(4):
      put_beepers()

   turn_right()

def line_beepers():
   pass

def put_beepers():
   put_beeper()
   move()

def turn_right():
   turn_left()
   turn_left()
   turn_left()

if __name__ == "__main__":
    run_karel_program()
