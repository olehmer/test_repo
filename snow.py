#!/usr/bin/env python3
"""A simple terminal snow animation."""

import random
import time
import sys
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_terminal_size():
    """Get terminal dimensions."""
    size = os.get_terminal_size()
    return size.columns, size.lines

def snow_animation(duration=60):
    """Generate snow animation in the terminal.

    Args:
        duration: How long to run the animation in seconds.
    """
    width, height = get_terminal_size()
    snowflakes = []

    # Initialize snowflakes at random positions
    for _ in range(width // 4):
        snowflakes.append({
            'x': random.randint(0, width - 1),
            'y': random.randint(0, height - 1),
        })

    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            clear_screen()

            # Create a grid to place snowflakes
            grid = [[' ' for _ in range(width)] for _ in range(height)]

            # Update snowflake positions
            for flake in snowflakes:
                flake['y'] += random.randint(0, 2)
                flake['x'] += random.randint(-1, 1)

                # Wrap around edges
                if flake['x'] < 0:
                    flake['x'] = width - 1
                elif flake['x'] >= width:
                    flake['x'] = 0

                # Reset to top if falls off bottom
                if flake['y'] >= height:
                    flake['y'] = 0
                    flake['x'] = random.randint(0, width - 1)

                # Place snowflake in grid
                if 0 <= flake['y'] < height and 0 <= flake['x'] < width:
                    grid[int(flake['y'])][int(flake['x'])] = '*'

            # Print the grid
            for row in grid:
                print(''.join(row))

            time.sleep(0.1)

    except KeyboardInterrupt:
        clear_screen()
        print("Snow animation stopped!")
        sys.exit(0)

if __name__ == '__main__':
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    snow_animation(duration)
