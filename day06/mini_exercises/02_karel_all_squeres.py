from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def step_up_from_right_side():
    turn_left()

    if front_is_clear():
        move()
        turn_left()
        return True

    turn_right()
    return False


def step_up_from_left_side():
    turn_right()

    if front_is_clear():
        move()
        turn_right()
        return True

    turn_left()
    return False

def go_around():
    while front_is_clear():
        move()
        if front_is_blocked():
            turn_left()

def cover_all_squares():
    while True:
        move_to_wall()

        if facing_east():
            if not step_up_from_right_side():
                break
        elif facing_west():
            if not step_up_from_left_side():
                break


def step_down_from_left():
    if left_is_blocked():
        turn_left()
        move()
        turn_left()

def step_down_from_right():
    if right_is_blocked():
        turn_right()
        move()
        turn_right()

def beeper_take():
    if beepers_present():
        pick_beeper()

def main():
    cover_all_squares()





if __name__ == "__main__":
    run_karel_program()