class Grid(object):
    size_x = 0
    size_y = 0
    obstacles = []
    name = ""

    def __init__(self, size_x, size_y, name="Mars", obstacles=[]):
        self.name = name
        self.size_x = size_x
        self.size_y = size_y
        self.obstacles = obstacles