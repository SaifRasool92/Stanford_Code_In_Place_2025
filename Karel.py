  """A cheat-sheet with the structure of the Karel programming language. See the Karel Reader for more details:

  

Base Karel commands

move()
turn_left()
put_beeper()
pick_beeper()



Karel program structures

This is the structure of a Karel program

from karel.stanfordkarel import *

# Comments can be included in any part
# of a program. They start with a #
# and include the rest of the line.
# the computer will ignore them, but they
# are very helpful for human readers!

def main():
    # code to execute

# declarations of other functions

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()



# example program to move, put_beeper, move
def main():
    move()
    put_beeper()
    move()

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()



Function Declaration:

def name():
    # body of the function.



# example: turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()



Conditions:

if condition:
    # code run if condition passes



if condition:
    # code block for "yes"
else:
    #code block for "no"



# example: a safe move
if front_is_clear():
    move()



For Loop:

for i in range(count):
    # code to repeat



# example: place 100 beepers
for i in range(100):
    put_beeper()



While Loop:

while condition:
    # code to repeat



# example: move karel to the next wall
while front_is_clear():
    move()



Names of the conditions

# karel conditions
front_is_clear()
beepers_present()
beepers_in_bag()
left_is_clear()
right_is_clear()
facing_north()
facing_south()
facing_east()
facing_west()



# opposites
front_is_blocked()
no_beepers_present()
no_beepers_in_bag()
left_is_blocked()
right_is_blocked()
not_facing_north()
not_facing_south()
not_facing_east()
not_facing_west()



Additional commands:

For advanced Karel programs you can use these two secret commands

random(p)
paint_corner(color)"""
from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    # move_and_put()
    # move_back_karel()
    # check_above_the_line()
    apply_all()


def apply_all():
    while left_is_clear():
        move_and_put()
        move_back_karel()
        check_above_the_line()
    move_and_put()


def turn_right_direct():
    turn_left()
    turn_left()
    turn_left()


def move_and_put():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def move_back_karel():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()


def check_above_the_line():
    if left_is_clear():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
