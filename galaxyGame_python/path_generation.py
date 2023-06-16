import random

def pre_fill_tiles_coordinates(self):
    for i in range(5):
        self.tiles_coordinates.append((0, i))

def generate_tiles_coordinates(self):
    min_tile_x = -int(self.number_of_vertical_lines / 2) + 1
    max_tile_x = (self.number_of_vertical_lines / 2) - 1
    last_y = 0
    last_x = 0
    for i in range(len(self.tiles_coordinates) - 1, -1, -1):
        if self.tiles_coordinates[i][1] < self.current_loop:
            del self.tiles_coordinates[i]

    if len(self.tiles_coordinates) > 0:
        last_y = self.tiles_coordinates[-1][1] + 1
        last_x = self.tiles_coordinates[-1][0]

    for i in range(len(self.tiles_coordinates), self.number_of_tiles):
        if last_x == min_tile_x:
            rnd = 2
        elif last_x == max_tile_x:
            rnd = 0
        else:
            rnd = random.randint(0, 2)

        self.tiles_coordinates.append((last_x, last_y))
        if rnd == 0:
            last_x -= 1
            self.tiles_coordinates.append((last_x, last_y))
            last_y += 1
            self.tiles_coordinates.append((last_x, last_y))
        if rnd == 2:
            last_x += 1
            self.tiles_coordinates.append((last_x, last_y))
            last_y += 1
            self.tiles_coordinates.append((last_x, last_y))
        last_y += 1