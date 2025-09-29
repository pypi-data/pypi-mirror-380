"""
A module that contains several implementations of various scroll art.

Individual functions implement scroll art, and make use of the WIDTH and DELAY global variables.

The *_simple() functions are variations whose code is more understandable to beginners and has a fixed configuration.
"""

import os, sys, random, shutil, time, argparse

WIDTH = shutil.get_terminal_size()[0]
DELAY = 0.02

# TODO add max_rows parameter so we can make text files of the output.

def main():
    parser = argparse.ArgumentParser(description="ScrollArt - Various animated scroll art displays")
    parser.add_argument('command', nargs='?', choices=['starfield', 'stripeout'], 
                       help='The scroll art command to run')
    
    args = parser.parse_args()
    
    credit = ''
    try:
        if args.command == 'starfield':
            credit = 'Starfield by Al Sweigart al@inventwithpython.com 2024'
            starfield()
        elif args.command == 'stripeout':
            credit = 'Stripe Out by Al Sweigart al@inventwithpython.com 2024'
            stripeout()
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print(credit)

def update_width(new_width=None):
    """Updates the global WIDTH variable to new_width. If new_width is None, WIDTH is based on the terminal size."""
    global WIDTH

    if new_width is None:
        WIDTH = shutil.get_terminal_size()[0]
    else:
        WIDTH = new_width

def update_delay(new_delay=None):
    """Updates the global DELAY variable to new_delay, if it's not None."""
    global DELAY

    if new_delay is not None:
        DELAY = new_delay


def starfield(change_amount=0.005, delay=0.02, star_char='*', empty_char=' '):
    update_delay(delay)
    density = 0.0

    while True:
        update_width()

        if density < 0 or density > 1.0:
            change_amount *= -1
        density = density + change_amount

        line = []
        for i in range(WIDTH):
            if random.random() < density:
                line.append(star_char)
            else:
                line.append(empty_char)

        print(''.join(line))
        time.sleep(DELAY)


def starfield_simple():
    change_amount = 0.005
    density = 0.0
    width = 80
    while True:
        if density < 0 or density > 1.0:
            change_amount *= -1
        density = density + change_amount

        line = ''
        for i in range(width):
            if random.random() < density:
                line = line + '*'
            else:
                line = line + ' '

        print(line)
        time.sleep(0.02)


def stripeout(fill_chars='#@O.:!', empty_chars=' ', delay=0.004, height=40, max_wipes=99):
    """Creates an animated stripe-out effect that alternates between filling and emptying the screen."""
    update_delay(delay)
    update_width()
    
    # Use the global WIDTH but subtract 1 like in the original
    simultaneous_stripes = WIDTH // 10
    block_mode = False
    
    def get_contiguous_columns_of_length(columns_left, length):
        contiguous_columns = set()
        for i in range(WIDTH):
            if all([i + x in columns_left for x in range(length)]):
                contiguous_columns.add(i)
        return contiguous_columns

    columns = [random.choice(empty_chars)] * WIDTH
    make_empty = False
    iteration = 0

    while True:
        columns_left = set(range(WIDTH))
        if make_empty:
            new_char = random.choice(empty_chars)
        else:
            new_char = random.choice(fill_chars)

        current_wipe_num = 1
        while len(columns_left):
            if current_wipe_num >= max_wipes:
                # change ALL of the remaining columns
                columns = [new_char] * WIDTH
                columns_left = set()
                current_wipe_num = 1
            else:
                if block_mode:
                    # Find contiguous columns (at least simultaneous_stripes in length)
                    for desired_length in range(simultaneous_stripes, 0, -1):
                        contiguous_columns = get_contiguous_columns_of_length(columns_left, desired_length)
                        if len(contiguous_columns) != 0:
                            break
                    col = random.choice(list(contiguous_columns))

                    # Remove several contiguous columns:
                    for i in range(simultaneous_stripes):
                        if col + i in columns_left:
                            columns_left.remove(col + i)
                            columns[col + i] = new_char
                else:
                    # Remove several random columns:
                    for i in range(simultaneous_stripes):
                        if len(columns_left) == 0: 
                            break
                        col = random.choice(list(columns_left))
                        columns_left.remove(col)
                        columns[col] = new_char

            # Print columns with the new_char
            for i in range(height):
                print(''.join(columns))
                time.sleep(DELAY)

            current_wipe_num += 1
        make_empty = not make_empty
        iteration += 1
        if iteration % 2 == 0:
            block_mode = not block_mode


