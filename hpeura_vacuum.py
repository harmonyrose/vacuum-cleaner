from vacuum import VacuumAgent

class HpeuraVacuumAgent(VacuumAgent):

    def __init__(self, step = 0):
        super().__init__()
        # any initialization you want to do here
        self.step = step

    def program(self, percept):
        # your amazing AI vacuum cleaner code goes here
        self.step += 1
        if percept[0] == 'Dirty':
            return 'Suck'
        
        if percept[1] == 'None':
            return 'Left'
        if percept[1] == 'Bump':
            return 'Right'
        return 'NoOp'
    
