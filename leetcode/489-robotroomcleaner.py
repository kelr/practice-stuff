# Use DFS to visit every empty room. Keep track of rooms visited. DFS
# in order of Up, Left, Right, Down. Do not recurse if you can't visit
# the room or the room has been visited already. If no further rooms
# can be visited, return and the uper level will handle the robot returning.
# O(N), all viable rooms are visited once
# O(N), space, where N is the number of visitable rooms.
class Solution:
    def __init__(self):
        self.cleanList = set()
        self.direction = 0
        self.directions = ("up", "left", "down", "right")
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.rec(robot, 0, 0)
            
    def rec(self, robot, x, y):
        """
        :type robot: Robot
        :rtype: None
        """
        robot.clean()
        self.cleanList.add((x, y))
        
        self.orient("up", robot)
        if (x, y+1) not in self.cleanList and robot.move():
            self.rec(robot, x, y+1)
            self.orient("down", robot)
            robot.move()
        
        self.orient("left", robot)
        if (x-1, y) not in self.cleanList and robot.move():
            self.rec(robot, x-1, y)
            self.orient("right", robot)
            robot.move()
            
        self.orient("down", robot)
        if (x, y-1) not in self.cleanList and robot.move():
            self.rec(robot, x, y-1)
            self.orient("up", robot)
            robot.move()
            
        self.orient("right", robot)
        if (x+1, y) not in self.cleanList and robot.move():
            self.rec(robot, x+1, y)
            self.orient("left", robot)
            robot.move()

    # Iterate through the directions array in a circular manner and left turn until you get the
    # orientation you want.
    def orient(self, newDirection, robot):
        while newDirection != self.directions[self.direction]:
            self.direction = (self.direction + 1) % len(self.directions)
            robot.turnLeft()