from graphics import *

grid_size = 28
pos = 20
rad = 10
grid = []

win = GraphWin("Natural Digit Reader", (grid_size + 1)*pos, (grid_size + 3)*pos)
submitted = False


def main():
    global submitted, grid, win

    win.bind('<B1-Motion>', drag)

    submit_button = Rectangle(Point(0.375*(grid_size + 1)*pos, (grid_size + 1)*pos), Point(0.625*(grid_size + 1)*pos, (grid_size+2.5)*pos))
    submit_text = Text(Point(0.5*(grid_size + 1)*pos, (grid_size + 1.75)*pos), "Submit")
    submit_button.draw(win)
    submit_text.draw(win)

    refresh_button = Rectangle(Point(pos, (grid_size + 1)*pos), Point(0.225*(grid_size + 1)*pos, (grid_size+2.5)*pos))
    refresh_text = Text(Point(0.125*(grid_size + 1)*pos, (grid_size + 1.75)*pos), "Refresh")
    refresh_button.draw(win)
    refresh_text.draw(win)
    
    for i in range(grid_size):
        grid.append([])
        for j in range(grid_size):
            grid[i].append(Node((i+1)*pos, (j+1)*pos, rad))


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].draw(win)


    while True:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()

        if((x >= submit_button.getP1().getX() and x <= submit_button.getP2().getX()) and (y >= submit_button.getP1().getY() and y <= submit_button.getP2().getY())):
            print(submit(grid))
            submitted = True
        
        elif((x >= refresh_button.getP1().getX() and x <= refresh_button.getP2().getX()) and (y >= refresh_button.getP1().getY() and y <= refresh_button.getP2().getY())):
            clear(grid)
            submitted = False

        elif(not submitted):
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if(grid[i][j].inside(x,y)):
                        grid[i][j].changeColour()
                

class Node(Circle):

    def __init__(self, x, y, radius, filled = False):
        Circle.__init__(self, Point(x, y), radius)
        self.x = x
        self.y = y
        self.filled = filled
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def changeColour(self):
        if(self.filled):
            self.setFill(color="white")
        else:
            self.setFill(color="black")
        
        self.filled = not self.filled

    def fill(self):
        if(not self.filled):
            self.setFill(color="black")
            self.filled = not self.filled

    def clear(self):
        if(self.filled):
            self.setFill(color="white")
            self.filled = not self.filled

    def isFilled(self):
        return self.filled

    def inside(self, x, y):
        return (x >= (self.getX() - self.getRadius()) and x <= (self.getX() + self.getRadius())) and (y >= (self.getY() - self.getRadius()) and y <= (self.getY() + self.getRadius()))
        

def submit(grid):
    values = ""

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j].isFilled()):
                values += '1'
            else:
                values += '0'
    
    return values


def clear(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].clear()
    
    print('Grid Cleared')


def drag(event):
    global submitted, grid

    if(not submitted):
        x = event.x
        y = event.y
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j].inside(x,y)):
                    grid[i][j].fill()

if __name__ == '__main__':
    main()