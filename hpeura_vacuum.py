from vacuum import VacuumAgent
import random

class HpeuraVacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.step = 0
        self.dirs = []
        self.bumps = []
        self.turns = []

    def program(self, percept):

        self.step += 1

        if percept[0] == 'Dirty':
            return 'Suck'
        
        elif self.dirs == []:
            dir = 'Right'
            self.log(dir, 'None', 'Straight')
            return dir
        
        
        elif percept[1] == 'Bump':
            
            # If this is the first time encountering a bump, turn left

            dir = self.turnLeft(self.dirs[-1])
            self.log(dir, 'Bump', 'Left')
            return dir


        
        elif percept[1] == 'None':

            if self.turns[-1] == 'Left':
                dir = self.turnRight(self.dirs[-1])
                self.log(dir, 'None', 'Right')
                return dir
            
            else:
                dir = self.dirs[-1]
                self.log(dir, 'None', 'Right')
                return dir

        
    def turnLeft(self, lastdir):
        if lastdir == 'Left':
            return 'Down'       
        elif lastdir == 'Right':
            return 'Up'
        elif lastdir == 'Up':
            return 'Left'
        else:
            return 'Right'
            
    def turnRight(self, lastdir):
        if lastdir == 'Left':
            return 'Up'       
        elif lastdir == 'Right':
            return 'Down'
        elif lastdir == 'Up':
            return 'Right'
        else:
            return 'Left'
     
    def log(self, dir, bump, turn):
        self.dirs.append(dir)
        self.bumps.append(bump)
        self.turns.append(turn)


    
