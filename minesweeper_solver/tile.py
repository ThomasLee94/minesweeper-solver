class Tile:
    def __init__(self, coords):
        i, j = coords

        self.i = i
        self.j = j

    def coordinates(self):
        return self.i, self.j

    