
class Rover:
    
    
    def __init__(self, x, y, direction):

        self.all_directions = ['N', 'E', 'S', 'W']

        self.x_pos = x
        self.y_pos = y
        self.current_pointer = self.all_directions.index(direction)
        print('Created rover at '+ str([self.x_pos, self.y_pos]) + ' and is facing ' + str(self.all_directions[self.current_pointer]))
            
    def checkDirection(self):
        if self.current_pointer < 0:
            self.current_pointer = len(self.all_directions)-1
        if self.current_pointer == len(self.all_directions):
            self.current_pointer = 0
    
    def navigate(self, command, x_boundry, y_boundry):
        if command == 'M':
            self.move(x_boundry, y_boundry)
        else:
            self.rotate(command)

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
    
    def getCurrentDirection(self):
        return self.all_directions[self.current_pointer]   
        
    def getCurrentCoordinates(self):
        return [self.x_pos, self.y_pos]

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
                self.y_pos -= 1
            return 'Rover moved to ' + str([self.x_pos, self.y_pos])
        else:
            return 'Move is out of bounds'
    
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



plateau = input('Enter plateau dimensions: ')
plateau_x = int(plateau.split()[0])
plateau_y = int(plateau.split()[1])
print([plateau_x, plateau_y])
rover_starting = input('Enter rover starting coordinates: ')
rover_x = int(rover_starting.split()[0])
rover_y = int(rover_starting.split()[1])
rover_direction = rover_starting.split()[2]
navigation = input('Enter navigation sequence: ')

r = Rover(rover_x,rover_y, rover_direction)
for i in navigation:
    r.navigate(i, plateau_x, plateau_y)
    print(r)