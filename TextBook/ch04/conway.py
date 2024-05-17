import random, time, copy
WIDTH, HEIGHT = 60, 20
next_cells = [['#' if random.randint(0, 1) == 0 else ' ' for _ in range(HEIGHT)] for _ in range(WIDTH)]

while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        print(''.join(current_cells[x][y] for x in range(WIDTH)))

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left, right = (x - 1) % WIDTH, (x + 1) % WIDTH
            above, below = (y - 1) % HEIGHT, (y + 1) % HEIGHT
            neighbors = sum(current_cells[i][j] == '#' for i in [left, x, right] for j in [above, y, below]) - (current_cells[x][y] == '#')
            next_cells[x][y] = '#' if (current_cells[x][y] == '#' and neighbors in [2, 3]) or (current_cells[x][y] == ' ' and neighbors == 3) else ' '
    time.sleep(1)
