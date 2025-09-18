
from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()

    pass

def build_hospital():
    pick_beeper()
    one_column()
    move()
    one_column()
def one_column():
    turn_left()
    put_3beepers()
    return_to_base()
    turn_left()


def return_to_base():
    """
    Karel turns around and goes to the wall.
    Pre-condition: Karel is at the end of the column
        it just built, facing north.
    Post-condition: Karel has returned to 1st Street,
        below the column is just built, facing south.
    """
    turn_around()
    move_to_wall()


def move_to_wall():
    while front_is_clear():
        move()

def safe_move():
    if front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def put_3beepers():
    
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        
        pass

    
    

if __name__ == '__main__':
    main()
