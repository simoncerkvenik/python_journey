# # KAREL THE ROBOT - COMMANDS AND CONDITIONS
# # -----------------------------------------
# # This is a list of basic Karel commands in Python.
# # Karel is used to learn programming logic.
# # Karel lives in a grid world, moves around, turns, picks up beepers, and puts them down.
#
#
# # BASIC COMMANDS
# # --------------
#
# # move()
# # Karel moves one square forward.
# # If there is a wall in front of Karel, the program gives an error.
#
# # turn_left()
# # Karel turns 90 degrees to the left.
#
# # pick_beeper()
# # Karel picks up a beeper from the current square.
# # If there is no beeper, the program gives an error.
#
# # put_beeper()
# # Karel puts a beeper on the current square.
# # If Karel has no beepers in the bag, the program gives an error.
#
#
# # PATH CONDITIONS
# # ---------------
#
# # front_is_clear()
# # Returns True if the path in front of Karel is clear.
#
# # front_is_blocked()
# # Returns True if there is a wall in front of Karel.
#
# # left_is_clear()
# # Returns True if the path on Karel's left side is clear.
#
# # left_is_blocked()
# # Returns True if there is a wall on Karel's left side.
#
# # right_is_clear()
# # Returns True if the path on Karel's right side is clear.
#
# # right_is_blocked()
# # Returns True if there is a wall on Karel's right side.
#
#
# # BEEPER CONDITIONS
# # -----------------
#
# # beepers_present()
# # Returns True if there is at least one beeper on the current square.
#
# # no_beepers_present()
# # Returns True if there is no beeper on the current square.
#
# # beepers_in_bag()
# # Returns True if Karel has at least one beeper in the bag.
#
# # no_beepers_in_bag()
# # Returns True if Karel has no beepers in the bag.
#
#
# # DIRECTION CONDITIONS
# # --------------------
#
# # facing_north()
# # Returns True if Karel is facing north.
#
# # facing_south()
# # Returns True if Karel is facing south.
#
# # facing_east()
# # Returns True if Karel is facing east.
#
# # facing_west()
# # Returns True if Karel is facing west.
#
# # not_facing_north()
# # Returns True if Karel is NOT facing north.
#
# # not_facing_south()
# # Returns True if Karel is NOT facing south.
#
# # not_facing_east()
# # Returns True if Karel is NOT facing east.
#
# # not_facing_west()
# # Returns True if Karel is NOT facing west.
#
#
# # CORNER COLORS - IF YOUR KAREL VERSION SUPPORTS THEM
# # ---------------------------------------------------
#
# # paint_corner(COLOR_NAME)
# # Paints the current square with the selected color.
#
# # corner_color_is(COLOR_NAME)
# # Returns True if the current square has the selected color.
#
#
# # PYTHON STRUCTURES USED WITH KAREL
# # ---------------------------------
#
# # def main():
# # The main function of the program.
# # This is where we write what Karel should do.
#
# # if condition:
# # Runs the code below only if the condition is True.
#
# # else:
# # Runs if the if condition is not True.
#
# # while condition:
# # Repeats the code while the condition is True.
#
# # for i in range(number):
# # Repeats the code a specific number of times.
#
#
# # EXAMPLES
# # --------
#
# # if front_is_clear():
# #     move()
#
# # if beepers_present():
# #     pick_beeper()
#
# # if no_beepers_present():
# #     put_beeper()
#
# # while front_is_clear():
# #     move()
#
# # for i in range(4):
# #     move()
#
#
# # COMMANDS WE CAN CREATE OURSELVES
# # --------------------------------
# # Karel does not always have turn_right().
# # So we can create it using three left turns.
#
# # def turn_right():
# #     turn_left()
# #     turn_left()
# #     turn_left()
#
# # def turn_around():
# #     turn_left()
# #     turn_left()
#
#
# # MAIN IDEA
# # ---------
#
# # Karel knows only a few commands.
# # But from small commands, we build bigger logic.
# # That is the point of programming:
# # small steps + clear order = solved problem.
# from stanfordkarel import *
#
# def  turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def two_pick():
#     move()
#     pick_beeper()
#     move()
#     pick_beeper()
#
# def three_pick():
#     move()
#     pick_beeper()
#     move()
#     pick_beeper()
#     move()
#     pick_beeper()
#
# def four_pick():
#     move()
#     pick_beeper()
#     move()
#     pick_beeper()
#     move()
#     pick_beeper()
#     move()
#     pick_beeper()
#
# # def main():
# #     turn_left()
# #     turn_left()
# #     two_pick()
# #     move()
# #     turn_right()
# #     three_pick()
# #     move()
# #     turn_right()
# #     two_pick()
# #     turn_left()
# #     three_pick()
# #     move()
# #     turn_right()
# #     three_pick()
# #     move()
# #     turn_right()
# #     three_pick()
# #     turn_left()
# #     four_pick()
# #     move()
# #     turn_right()
# #     three_pick()
# #     move()
# #     turn_right()
# #     four_pick()
#
# # def pick_many(amount):
# #     for i in range(amount):
# #         move()
# #         pick_beeper()
# #
# # def main():
# #     turn_left()
# #     turn_left()
# #     pick_many(2)
# #     move()
# #     turn_right()
# #     pick_many(3)
# #     move()
# #     turn_right()
# #     pick_many(2)
# #     turn_left()
# #     pick_many(3)
# #     move()
# #     turn_right()
# #     pick_many(3)
# #     move()
# #     turn_right()
# #     pick_many(3)
# #     turn_left()
# #     pick_many(4)
# #     move()
# #     turn_right()
# #     pick_many(3)
# #     move()
# #     turn_right()
# #     pick_many(4)
#
# def step_down_from_right():
#     turn_right()
#     move()
#     turn_right()
#
# def step_down_from_left():
#     turn_left()
#     move()
#     turn_left()
#
# def step_down():
#     if facing_east():
#         step_down_from_right()
#     elif facing_west():
#         step_down_from_left()
#
# def clean_line():
#     while front_is_clear():
#         if beepers_present():
#             pick_all_here()
#         move()
#     if beepers_present():
#         pick_all_here()
#
# def pick_all_here():
#     while beepers_present():
#         pick_beeper()
#
# def safe_step_down():
#     if front_is_clear() and right_is_clear():
#         step_down_from_right()
#     elif facing_west() and left_is_clear():
#         step_down_from_left()
#
# def main():
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#     safe_step_down()
#     clean_line()
#
#
#
#
#
# if __name__ == "__main__":
#     run_karel_program()


from stanfordkarel import *


# AUTO KAREL CLEANER
# This program explores the whole reachable world
# and picks up all beepers.


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = EAST
current_x = 0
current_y = 0

visited = set()


def set_start_direction():
    global direction

    if facing_north():
        direction = NORTH
    elif facing_east():
        direction = EAST
    elif facing_south():
        direction = SOUTH
    elif facing_west():
        direction = WEST


def turn_left_smart():
    global direction

    turn_left()

    direction = (direction - 1) % 4


def turn_right():
    turn_left_smart()
    turn_left_smart()
    turn_left_smart()


def turn_around():
    turn_left_smart()
    turn_left_smart()


def face_direction(target_direction):
    while direction != target_direction:
        turn_left_smart()


def move_smart():
    global current_x
    global current_y

    move()

    if direction == NORTH:
        current_y += 1
    elif direction == EAST:
        current_x += 1
    elif direction == SOUTH:
        current_y -= 1
    elif direction == WEST:
        current_x -= 1


def next_position():
    if direction == NORTH:
        return current_x, current_y + 1
    elif direction == EAST:
        return current_x + 1, current_y
    elif direction == SOUTH:
        return current_x, current_y - 1
    elif direction == WEST:
        return current_x - 1, current_y


def pick_all_here():
    while beepers_present():
        pick_beeper()


def explore():
    visited.add((current_x, current_y))

    pick_all_here()

    start_direction = direction

    for target_direction in [NORTH, EAST, SOUTH, WEST]:
        face_direction(target_direction)

        next_x, next_y = next_position()

        if front_is_clear() and (next_x, next_y) not in visited:
            move_smart()
            explore()

            turn_around()
            move_smart()
            turn_around()

    face_direction(start_direction)


def main():
    set_start_direction()
    explore()


if __name__ == "__main__":
    run_karel_program()