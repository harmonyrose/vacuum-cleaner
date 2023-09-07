from vacuum import VacuumAgent

class HpeuraVacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        # any initialization you want to do here

    def program(self, percept):
        # your amazing AI vacuum cleaner code goes here
        return 'NoOp'