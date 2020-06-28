import random

TARGET_BLOCKS_FROM_HOME = 5


# simulate random walk of n blocks
def random_walk(n):
    # coordinates start at (0, 0)
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    # return coordinates
    return (x, y)


def test_random_walk():
    NUM_OF_TESTS = 25
    NUM_OF_BLOCKS = 10

    for i in range(NUM_OF_TESTS):
        walk = random_walk(NUM_OF_BLOCKS)
        print(f'{walk} Distance from home = {abs(walk[0]) + abs(walk[1])}')


def compute_short_walk_percentage():
    NUM_OF_WALKS = 20000
    MAX_WALK_SIZE = 50

    longest_walk = 0
    for walk_length in range(1, MAX_WALK_SIZE + 1):
        short_walk = 0

        # iterate through a large number of trials
        for i in range(NUM_OF_WALKS):
            (x, y) = random_walk(walk_length)
            distance = abs(x) + abs(y)
            if distance <= TARGET_BLOCKS_FROM_HOME:
                short_walk += 1

        # find percentage of short walks
        short_walk_percentage = float(short_walk) / NUM_OF_WALKS

        # display trials
        print(f'Walk length = {walk_length} \t'
              f'percentage of short walks = {100*short_walk_percentage}')

        if short_walk_percentage >= 0.5:
            longest_walk = walk_length
    return longest_walk


if __name__ == "__main__":

    longest_walk = compute_short_walk_percentage()

    # display answer
    print(f'\nLongest walk: {longest_walk}')
