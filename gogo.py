import sympy
from time import sleep
import os


class Belief:
    def __init__(self):
        self.belief_base = []
        self.done = False
        self.start()

    def reset(self):
        sleep(2)
        self.belief_base.clear()
        self.belief_system = ""
        self.done = False
        self.start()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        self.clear_terminal()

        print("Current belief base:", self.belief_base)
        print("Current belief system:", str.upper(self.belief_system))
        print("\nPossible actions:")
        print("Type a belief to add the belief to the belief base. Otherwise use 1 of the following codewords:")
        # print('"Display" the current belief base')
        print('"clear" the belief base')
        print('"quit" stop the agent')
        print('"solve" the current belief system')

    def get_belief_system(self):
        self.clear_terminal()
        print("Choose a belief system: \nPL  (Propositional logic), \nRES (Resolution),\nCNF (CNF-form),\nAGM (AGM revision),\nPAR (Partial meet contraction)\n")
        while True:
            belief_options = ['pl', 'res', 'cnf', 'agm', 'par']
            belief_system = str.lower(input())
            if belief_system in belief_options:
                return belief_system
            else:
                print('Invalid belief system.')

    def get_input(self):
        new_belief = str.lower(input())
        #Fjern alle tal i string.. Skal man det?
        new_belief = ''.join([i for i in new_belief if not i.isdigit()])

        #rens inputtet somehow:
        # Hvordan skal inputtet også se ud? Jeg forstår faktisk ikke rigtigt hvad der foregår tbh..

        if new_belief == "clear":
            self.belief_base.clear()
        elif new_belief == "quit":
            self.done = True
        elif new_belief == "solve":
            if len(self.belief_base) != 0:
                self.solve_belief_system()
                self.done = True
                self.reset()
            else:
                print("Belief base is empty.")
                sleep(2)
        else:
            if new_belief != '':
                self.belief_base.append(new_belief)
            else:
                print("Input is empty.")
                

    #Solve funktioner.. Ved ikke om det skal fungere sådan her tbh
    def solve_PL(self):
        print("PL")
    
    def solve_RES(self):
        print("RES")
    
    def solve_CNF(self):
        print("CNF")
    
    def solve_AGM(self):
        print("AGM")

    def solve_PAR(self):
        print("PAR")

    def solve_belief_system(self):
        if self.belief_system == "pl":
            self.solve_PL()
        elif self.belief_system == "res":
            self.solve_RES()
        elif self.belief_system == "cnf":
            self.solve_CNF()
        elif self.belief_system == "agm":
            self.solve_AGM()
        elif self.belief_system == "par":
            self.solve_PAR()

    def start(self):
        self.belief_system = self.get_belief_system()
        while(not self.done):
            self.main_menu()

            self.get_input()

if __name__ == '__main__':
    belief = Belief()
