class Rover(object):

    x = 0
    y = 0
    orientation = 'N'
    orientation_list = ["N","E","S","W"]

    def __init__(self, start_x, start_y, orientation):
        self.x = start_x
        self.y = start_y
        self.orientation = orientation

    def move(self, movs):
        for m in movs:
            if self.orientation == "N":
                if m == "f":
                    self.y = self.y + 1
                else:
                    self.y = self.y - 1
            elif self.orientation == "S":
                if m == "f":
                    self.y = self.y - 1
                else:
                    self.y = self.y + 1
            elif self.orientation == "E":
                if m == "f":
                    self.x = self.x + 1
                else:
                    self.x = self.x - 1
            elif self.orientation == "W":
                if m == "f":
                    self.x = self.x - 1
                else:
                    self.x = self.x + 1

    def rotate(self, turns):
        for turn in turns:
            if(turn == "r"):
                self.orientation = self.orientation_list[(self.orientation_list.index(self.orientation)+1)%4]
            elif (turn =="l"):
                self.orientation = self.orientation_list[(self.orientation_list.index(self.orientation)-1)%4]
