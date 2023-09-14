
class Rover:
    #initialize rover
    def __init__(self, x, y, direction):

        self.all_directions = ['N', 'E', 'S', 'W']

        self.x_pos = x
        self.y_pos = y
        self.current_pointer = self.all_directions.index(direction)
            
    #If the direction pointer is less than 0 (lower bound), set pointer to back of list, and vice versa upper bound
    def checkDirection(self):
        if self.current_pointer < 0:
            self.current_pointer = len(self.all_directions)-1
        if self.current_pointer == len(self.all_directions):
            self.current_pointer = 0
    
    #navigate function to move/rotate the rover
    def navigate(self, command, x_boundry, y_boundry):
        if command == 'M':
            self.move(x_boundry, y_boundry)
        else:
            self.rotate(command)

    #rotate function to change the POINTER
    def rotate(self, direction):
        try:
            if direction == 'L':
                self.current_pointer -=1
                self.checkDirection()
            if direction == 'R':
                self.current_pointer +=1
                self.checkDirection()
            return 'Rotation complete'
        except:
            print('Invalid Input')
    
    #returns the current facing direction of the rover
    def getCurrentDirection(self):
        return self.all_directions[self.current_pointer]   
    
    #returns the current coordinates of the rover
    def getCurrentCoordinates(self):
        return [self.x_pos, self.y_pos]

    #returns the position and direction of the rover
    def getCurrentPosition(self):
        return '' + str(self.x_pos) + ' ' + str(self.y_pos) + ' ' + str(self.getCurrentDirection())

    #primary function to initiate a move on the rover, if move is invalid (out of bounds) it will not move
    def move(self, x_boundry, y_boundry):
        if self.isMoveValid(x_boundry, y_boundry):
            directionToMove = self.getCurrentDirection()
            if directionToMove == 'N':
                self.y_pos += 1
            elif directionToMove == 'E':
                self.x_pos += 1
            elif directionToMove == 'S':
                self.y_pos -= 1
            elif directionToMove == 'W':
                self.x_pos -= 1
            return 'Rover moved to ' + str([self.x_pos, self.y_pos])
        else:
            return 'Move is out of bounds, skipping command'
    
    #checks if the next move is valid
    #something to think about here: when to check if the move is valid...should we predetermine when the rotation happens or only check when the move happens
    #depending on the metrics and frequency of move vs rotate to limit checks
    def isMoveValid(self, x_boundry, y_boundry):
        directionToMove = self.getCurrentDirection()
         
        #if rover is facing N/E/S/W and next move will put us out of bounds
        if directionToMove == 'N' and (self.y_pos + 1 > y_boundry):
             return False
        elif directionToMove == 'E' and (self.x_pos + 1 > x_boundry):
             return False
        elif directionToMove == 'S' and (self.y_pos - 1 < 0):
             return False
        elif directionToMove == 'W' and (self.x_pos - 1 < 0):
             return False
        return True

    def __str__(self):
        return 'The rover is currently at ' + str(self.getCurrentCoordinates()) + ' facing ' + str(self.getCurrentDirection())


#run script
plateau = input('Enter plateau dimensions: ')
plateau_x = int(plateau.split()[0])
plateau_y = int(plateau.split()[1])
rover_starting = input('Enter rover starting coordinates: ')
rover_x = int(rover_starting.split()[0]) 
rover_y = int(rover_starting.split()[1])
rover_direction = rover_starting.split()[2]
navigation = input('Enter navigation sequence: ')

r = Rover(rover_x,rover_y, rover_direction)
for i in navigation:
    r.navigate(i, plateau_x, plateau_y)
    print(r)
print(r.getCurrentPosition())