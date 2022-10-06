import unittest

from rover import Rover
from grid import Grid


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
"""He organizado cada test en 3 fases (Arrange, Act, Assert)
    1. Arrange: se crean las dependencias y el estado inicial para el test
    2. Act: se llama al método o propiedad que se testea
    3. Assert: se comprueban que los resultados observados son correctos
"""
class MarsRoverTestCase(unittest.TestCase):
    def test_rover_move_forward(self):
        #Arrange
        rover = Rover(
            start_x=0,
            start_y=2,
            orientation='N',
            grid=Grid(3,3)
        )
        movements = ['f']
        expected_position = (0, 0)

        #Act
        rover.move(movements)
        
        #Assert
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backward(self):
        rover = Rover(
            start_x=0,
            start_y=2,
            orientation='N',
            grid=Grid(3,3)
        )
        movements = ['b']
        expected_position = (0, 1)

        rover.move(movements)

        self.assert_rover_position(expected_position, rover)   

    def test_rover_rotate_right(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='W',
            grid=Grid(3,3)
        )
        turns = ["r"]
        expected_orientation = "N"

        rover.move(turns)

        self.assert_rover_orientation(expected_orientation, rover)

    def test_rover_rotate_left(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='N',
            grid=Grid(3,3)
        )
        turns = ["l"]
        expected_orientation = "W"

        rover.move(turns)

        self.assert_rover_orientation(expected_orientation, rover)


    def test_spheric_planets_N_to_S(self):
        rover = Rover(
            start_x=0,
            start_y=2,
            orientation='N',
            grid=Grid(3,3)
        )
        movements = ['f']
        expected_position = (0, 0)

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)

    def test_spheric_planets_S_to_N(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='N',
            grid=Grid(3,3)
        )
        movements = ['b']
        expected_position = (0,2)

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)

    def test_spheric_planets_E_to_W(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='W',
            grid=Grid(3,3)
        )
        movements = ['f']
        expected_position = (2,0)

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)

    def test_spheric_planets_W_to_E(self):
        rover = Rover(
            start_x=2,
            start_y=0,
            orientation='E',
            grid=Grid(3,3)
        )
        movements = ['f']
        expected_position = (0,0)

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)

    def test_detect_obstacle(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='N',
            grid=Grid(3,3, "Mars", [(0,1)]) #Un obstáculo en la coordenada (1,1)
        )
        movements = ["f","r","f"]
        expected_position = (0, 0)
        expected_orientation = "N"

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover) #Comprobamos que vuelve a la posición anterior posible
        self.assert_rover_orientation(expected_orientation, rover)

    def test_detect_initial_obstacle(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='N',
            grid=Grid(3,3, "Mars", [(0,0)]) #Un obstáculo en la coordenada (0,0)
        )
        movements = ["f"]
        expected_position = (0, 0) #Al haber un obstáculo en la pos. inicial se queda donde está
        expected_orientation = "N"

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)
        self.assert_rover_orientation(expected_orientation, rover)

    def test_array_of_commands(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='N',
            grid=Grid(3,3)
        )
        movements = ["f","r","f","f", "l", "f"]
        expected_position = (2,2) 
        expected_orientation = "N"

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)
        self.assert_rover_orientation(expected_orientation, rover)

    def test_unknown_command(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='N',
            grid=Grid(3,3)
        )
        movements = ["j", "f"]
        expected_position = (0,0) 
        expected_orientation = "N"

        rover.move(movements)
        
        self.assert_rover_position(expected_position, rover)
        self.assert_rover_orientation(expected_orientation, rover)

    def assert_rover_position(self, expected_position, rover):
        self.assertEqual(expected_position[0], rover.x)
        self.assertEqual(expected_position[1], rover.y)

    def assert_rover_orientation(self, expected_orientation, rover):
        self.assertEqual(expected_orientation, rover.orientation)