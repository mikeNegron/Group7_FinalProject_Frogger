from graphics import*

#HitBox class
class HitBox:
    """Creates a square Hit-Box for obstacles."""

    def __init__(self, x1, y1, x2, y2):
        """Creates the Hit-Box for 2 given coordinates pairs in oposite corners."""

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.box = Rectangle(Point(x1, y1), Point(x2, y2))

        self.corner_coords = self.get_coords()

        self.side_coords = self.map_sides() #Might not need this
    
    def get_coords(self):
        """Returns the 4 coordinates of the Hit-Box (square)."""

        p1 = (self.x1, self.y1) # p1-------p2
        p2 = (self.x2, self.y1) # |         |
        p3 = (self.x1, self.y2) # |         |
        p4 = (self.x2, self.y2) # p3-------p4

        self.corner_coords = [p1, p2, p3, p4]

        return self.corner_coords

    def map_sides(self):
        """Gets coordinates for all the sides of the box"""

        x_values = [range(self.x1, self.x2)] #One at y1 and one at y2
        y_values = [range(self.y1, self.y2)] #One at x1 and one at x2

        self.side_coords = [x_values, y_values]

        return self.side_coords

    def move_box(self, dx):
        """Moves box to the left by a given amount."""
        self.box.move(-dx, 0)

        self.corner_coords = self.get_coords()
        self.side_coords = self.map_sides()

class Display:
    def __init__(self, width, height, window):
        self.width = width
        self.height = height

        self.window = window

        self.starts = {}
        self.river = {}
        self.road_lines = {}

    def generate_starts(self, start_amount):
        self.starts[0] = Rectangle(Point(0, 550), Point(self.width, self.height))
        self.starts[0].setFill('Green')
        self.starts[0].setOutline('Green')
        self.starts[0].draw(self.window)

        for i in range(1, start_amount):
            self.starts[i] = self.starts[i - 1].clone()
            
            self.starts[i].move(0, -250)
            
            self.starts[i].draw(self.window)

    def generate_river(self, goal_amount):
        self.river[0] = Rectangle(Point(0, -25), Point(100, 75))
        self.river[0].setFill('Green')
        self.river[0].setOutline('Green')
        self.river[0].draw(self.window)

        for i in range(1, goal_amount):
            self.river[i] = self.river[i - 1].clone()
            self.river[i].move(100, 0)

            if not(i%2 == 0):
                self.river[i].setFill('Blue')
                self.river[i].setOutline('Blue')

            else:
                self.river[i].setFill('Green')
                self.river[i].setOutline('Green')

            self.river[i].draw(self.window)

        water_body = Rectangle(Point(0, 75), Point(self.width, self.height/2))
        water_body.setFill('Blue')
        water_body.setOutline('Blue')
        water_body.draw(self.window)
        
    def generate_lines(self):
        self.road_lines[0] = Rectangle(Point(0, 435), Point(50, 455))
        self.road_lines[0].setFill('Yellow')
        self.road_lines[0].draw(self.window)

        for j in range(1, 9):
            self.road_lines[j] = self.road_lines[j - 1].clone()
            self.road_lines[j].move(125, 0)
            self.road_lines[j].draw(self.window)

    def generate_field(self):
        self.generate_starts(2)
        self.generate_river(11)
        self.generate_lines()
        

def main():
    win = GraphWin('Frogger', 900, 600, autoflush=False)
    win.setBackground('Black')

    ui = Display(900, 600, win)
    ui.generate_field()

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

#Car class to inherit HitBox class (bool expression to determine if it'll kill or not)
    #4 types of cars
        #Could be implemented on a list

#Snake class to inherit HitBox class

#Turtle class to control their behavior (sink and float) inherits HitBox too

#Frog class

#Reward class

#Game class to run frogger