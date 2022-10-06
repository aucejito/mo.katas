from pickletools import read_decimalnl_long
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
       

    def move(self, movs):
        try:
            if(self.checkObstacle()): #Initial obstacle check
                    obstacle_pos = (self.x, self.y)
                    raise ObstacleError()
                
            else:        
                last_position = (self.x, self.y)
                
                for m in movs:
                    if m == "l" or m == "r":
                        self.rotate(m)
                    else:    
                        if(m=="f"):
                            self.move_forward()
                        elif(m=="b"):
                            self.move_backwards()
                        else:
                            print(f"\'{m}\' is an unknown command")
                            break
                    
                        if(self.checkObstacle()):
                            obstacle_pos = (self.x, self.y)
                            self.x = last_position[0]
                            self.y = last_position[1]
                            
                            raise ObstacleError()
                            # except ObstacleError as err:
                            #     err.position = obstacle_pos
                            #     print(err)
                            #     break #Abort the sequence
                        else:
                            last_position = (self.x, self.y)

        except ObstacleError as err:
                    err.position = obstacle_pos
                    if((self.x, self.y) == err.position):
                        print(str(err) + ", the initial position")
                    else:
                        print(err)

    def checkObstacle(self):
        curr_pos = (self.x, self.y)
        return curr_pos in self.grid.obstacles

    def move_forward(self):
        if self.orientation == "N":
                self.y = (self.y + 1)%self.grid.size_y
        elif self.orientation == "S":
                self.y = (self.y - 1)%self.grid.size_y
        elif self.orientation == "E":
                self.x = (self.x + 1)%self.grid.size_x
        elif self.orientation == "W":
                self.x = (self.x - 1)%self.grid.size_x

    def move_backwards(self):
        if self.orientation == "N":
                self.y = (self.y - 1)%self.grid.size_y
        elif self.orientation == "S":
                self.y = (self.y + 1)%self.grid.size_y
        elif self.orientation == "E":
                self.x = (self.x - 1)%self.grid.size_x
        elif self.orientation == "W":
                self.x = (self.x + 1)%self.grid.size_x

    def rotate(self, turn):
        if(turn == "r"):
            self.orientation = self.orient_list[(self.orient_list.index(self.orientation)+1)%4]
        elif (turn =="l"):
            self.orientation = self.orient_list[(self.orient_list.index(self.orientation)-1)%4]


if __name__ == '__main__':
    rover = Rover(0,0,"N",Grid(3,3, "Mars",[(0,1)]))
    rover.move(["f","r","f"])
    pass

