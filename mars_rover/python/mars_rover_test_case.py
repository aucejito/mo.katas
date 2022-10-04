import unittest

from rover import Rover


"""
Mars rover moves through


                       N
        --------------------------------
        |   0,2   |   1,2   |   2,2    |
        -------------------------------- 
    W   |   0,1   |   1,1   |   2,1    |    E
        -------------------------------- 
        |   0,0   |   1,0   |   2,0    |
        --------------------------------
                       S
                   
"""


class MarsRoverTestCase(unittest.TestCase):
    def test_rover_move_forward(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='N'
        )

        movements = ['f']
        expected_position = (1, 2)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)
       
    def test_rover_rotate(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='W'
        )
        turns = ["r","r"]
        rover.rotate(turns)
        expected_orientation = "E"
        self.assert_rover_orientation(expected_orientation, rover)

    def assert_rover_position(self, expected_position, rover):
        self.assertEqual(expected_position[0], rover.x)
        self.assertEqual(expected_position[1], rover.y)

    def assert_rover_orientation(self, expected_orientation, rover):
        self.assertEqual(expected_orientation, rover.orientation)
