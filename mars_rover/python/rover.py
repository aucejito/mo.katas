from pickletools import read_decimalnl_long
from collections import deque
from tabnanny import check
from ObstacleError import ObstacleError
from grid import Grid

class Rover(object):

    x = 0
    y = 0
    grid = Grid(3,3)
    orientation = 'N'
    orient_list = ["N","E","S","W"]

    def __init__(self, start_x, start_y, orientation, grid):
        self.x = start_x
        self.y = start_y
        self.orientation = orientation
        self.grid = grid
        if(self.checkObstacle()):
            try:
                raise ObstacleError((self.x,self.y))
            except ObstacleError as err:
                print(err)

    def move(self, movs):
        last_position = (self.x, self.y)
        
        for m in movs:
            if m == "l" or m == "r":
                self.rotate(m)
            else:    
                if self.orientation == "N":
                    if m == "f":
                        self.y = (self.y + 1)%self.grid.size_y
                    else: #'b' backwards
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
            
                if(self.checkObstacle()):
                    obstacle_pos = (self.x, self.y)
                    self.x = last_position[0]
                    self.y = last_position[1]
                    
                    try:
                        raise ObstacleError()
                    except ObstacleError as err:
                        err.position = obstacle_pos
                        print(err)
                        break #Abort the sequence
                    
                else:
                    last_position = (self.x, self.y)

    def checkObstacle(self):
        curr_pos = (self.x, self.y)
        return curr_pos in self.grid.obstacles
            
    def rotate(self, turn):
        if(turn == "r"):
            self.orientation = self.orient_list[(self.orient_list.index(self.orientation)+1)%4]
        elif (turn =="l"):
            self.orientation = self.orient_list[(self.orient_list.index(self.orientation)-1)%4]


if __name__ == '__main__':
    rover = Rover(0,0,"N",Grid(3,3, "Mars",[(0,1)]))
    rover.move(['f'])

