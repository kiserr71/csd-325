#Randy Easton, Rob Kiser, and Daniel Preller, 02 July 2025, Assignment 6.2

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
LAKE = 'L'

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.
LAKE_CHANCE = 75  # Chance a blank space turns into a lake. Used to create a randomized
#lake on startup.
lake_start_x = 20
lake_start_y = 10

MAX_LAKE_SIZE = 450 # Maximum size of the lake, approximately 25% of the whole space

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    lake_spaces = 0

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if x == lake_start_x and y == lake_start_y:
                forest[(x, y)] = LAKE
                #This is our "lake seed".
                lake_spaces += 1

            elif forest.get(((x-1), y)) == LAKE and (random.random() * 100 <= LAKE_CHANCE) and lake_spaces <= MAX_LAKE_SIZE:
                forest[(x, y)] = LAKE
                lake_spaces +=1
            #Randomly determines if the next space will be a lake. NOTE: LAKE_CHANCE is
            #set to 75% as a result of my playing with the code. Too low and we only have
            #a puddle. Too high and it becomes a square. - RWK
                
            elif forest.get((x, (y-1))) == LAKE and (random.random() * 100 <= LAKE_CHANCE) and lake_spaces <= MAX_LAKE_SIZE:
                forest[(x, y)] = LAKE
                lake_spaces += 1
            #Randomly determines if the next space will be a lake based on the space
            #above it. Due to the random generation of lake spaces, the lakes that form
            #will often have "islands" in them but natural lakes have those too so I
            #left it as is. - RWK


    for x in range(WIDTH):
        for y in range(HEIGHT):
            if forest.get((x, y)) == LAKE:
                continue
            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
          	
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')

            elif forest[(x, y)] == LAKE:
                bext.fg('blue')
                print(LAKE, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
