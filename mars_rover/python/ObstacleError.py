class ObstacleError(Exception):
    """Raised when rover detects an obstacle"""
    position = (-1,-1)

    def _init__(self, position, *args):
        self.position = position
        super().__init__(args)
        
    def __str__(self):
        return f'Rover has detected an obstacle at {self.position}'