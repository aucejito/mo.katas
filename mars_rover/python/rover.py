class Grid(object):
    size_x = 0
    size_y = 0
    obstacles = [(1,1)]

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y




class Rover(object):

    x = 0
    y = 0
    grid = Grid(3,3)
    orientation = 'N'
    orientation_list = ["N","E","S","W"]

    def __init__(self, start_x, start_y, orientation, grid):
        self.x = start_x
        self.y = start_y
        self.orientation = orientation
        self.grid = grid

    def move(self, movs):
        for m in movs:
            if self.orientation == "N":
                if m == "f":
                    self.y = (self.y + 1)%self.grid.size_y
                else:
                    self.y = (self.y - 1)%self.grid.size_y
            elif self.orientation == "S":
                if m == "f":
                    self.y = (self.y - 1)%self.grid.size_y
                else:
                    self.y = (self.y + 1)%self.grid.size_y
            elif self.orientation == "E":
                if m == "f":
                    self.x = (self.x + 1)%self.grid.size_x
                else:
                    self.x = (self.x - 1)%self.grid.size_x
            elif self.orientation == "W":
                if m == "f":
                    self.x = (self.x - 1)%self.grid.size_x
                else:
                    self.x = (self.x + 1)%self.grid.size_x

    def rotate(self, turns):
        for turn in turns:
            if(turn == "r"):
                self.orientation = self.orientation_list[(self.orientation_list.index(self.orientation)+1)%4]
            elif (turn =="l"):
                self.orientation = self.orientation_list[(self.orientation_list.index(self.orientation)-1)%4]
