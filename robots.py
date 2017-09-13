class Robot:
    def __init__(self, row, column, colour):
        self.row = row
        self.column = column
        self.colour = colour
    def move(self):
        pass

def make_robots():
    return 8, 8, [
        Robot(3, 2, "teal"),
        Robot(1, 7, "green"),
        Robot(2, 4, "pink"),
    ]
    
