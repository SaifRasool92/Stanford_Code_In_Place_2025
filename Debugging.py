"""Karel Debugging
(1) Identify the problems in the code below and (2) Write 3 sentences of advice to the student who wrote this code. Rather than point out the bugs, consider how to guide the student toward diagnosing and correcting the problems on their own.

"""
Assumes that Karel starts in the bottom of a world filled with beepers
Picks up all the beepers in the first two rows
"""
def pick_up_all_beepers():
    pick_row()
    change_rows()
    pick_row()

def change_rows():
    turn_left()
    move()

def pick_row():
    while front_is_clear():
        pick_beeper()
        move()"""
"""Solution:



"""
