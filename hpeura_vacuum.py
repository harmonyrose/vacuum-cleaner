from vacuum import VacuumAgent
import random

class HpeuraVacuumAgent(VacuumAgent):

    def __init__(self, step = 0, curr_dir = "Right"):
        super().__init__()
        # any initialization you want to do here
        self.step = step
        self.curr_dir = curr_dir

    def program(self, percept):
        # your amazing AI vacuum cleaner code goes here
        self.step += 1
        if percept[0] == 'Dirty':
            return 'Suck'


        dirs = ['Up', 'Down', 'Right', 'Left']
        self.curr_dir = random.choice(dirs)
        return self.curr_dir        

    
