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
        
        # Always go right at the beginning
        elif self.dirs == []:
            dir = 'Right'
            self.log(dir, 'None', 'Straight')
            return dir
        
        # Stop moving after 300 steps
        elif self.step >= 400:
            return 'NoOp'
        
        # Every 10 steps, go in a random direction
        elif self.step % 10 == 0:
            dir = random.choice(['Left', 'Right', 'Up', 'Down'])
            self.log(dir, percept[1], 'Random')
            return dir
        
        elif percept[1] == 'Bump':
            
            # Turn left at a bump
            dir = self.turnLeft(self.dirs[-1])
            self.log(dir, 'Bump', 'Left')
            return dir


        
        elif percept[1] == 'None':

            # If just turned left, turn right
            if self.turns[-1] == 'Left':
                dir = self.turnRight(self.dirs[-1])
                self.log(dir, 'None', 'Right')
                return dir
            
            else:

                # Keep going in the same direction
                dir = self.dirs[-1]
                self.log(dir, 'None', 'Straight')
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
     

    # Keep a log of past directions, bumps, and turns
    def log(self, dir, bump, turn):
        self.dirs.append(dir)
        self.bumps.append(bump)
        self.turns.append(turn)


    
