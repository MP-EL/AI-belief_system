from sympy import *
from time import sleep
import os


class Belief:
    def __init__(self):
        self.belief_base = []
        self.done = False

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        self.clear_terminal()

        print("Current belief base:", self.belief_base)
        print("Current belief system:", self.belief_system)
        print("\nPossible actions:")
        print("Type a belief to add the belief to the belief base. Otherwise use 1 of the following codewords:")
        # print('"Display" the current belief base')
        print('"Clear" the belief base')
        print('"Quit" stop the agent')
        print('"Solve" the current belief system')

    def get_belief_system(self):
        self.clear_terminal()
        belief_options = ['PL', 'RES', 'CNF', 'AGM', 'PAR']
        belief_system = input("""Choose a belief system: \nPL  (Propositional logic), \nRES (Resolution),\nCNF (CNF-form),\nAGM (AGM revision),\nPAR (Partial meet contraction)\n""")
        if belief_system in belief_options:
            return belief_system
        else:
            print('Invalid belief system.')

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
        if self.belief_system == "PL":
            self.solve_PL()
        elif self.belief_system == "RES":
            self.solve_RES()
        elif self.belief_system == "CNF":
            self.solve_CNF()
        elif self.belief_system == "AGM":
            self.solve_AGM()
        elif self.belief_system == "PAR":
            self.solve_PAR()

    def user_action(self):
        self.belief_system = self.get_belief_system()
        while(not self.done):
            self.main_menu()
            new_belief = input()
            
            #rens inputtet somehow:
            # Hvordan skal inputtet også se ud? Jeg forstår faktisk ikke rigtigt hvad der foregår tbh..

            if new_belief == "Clear":
                self.belief_base = []
            elif new_belief == "Quit":
                self.done = True
            elif new_belief == "Solve":
                if len(self.belief_base) != 0:
                    self.solve_belief_system()
                    self.done = True
                else:
                    print("Belief base is empty.")
                    sleep(2)
            else:
                self.belief_base.append(new_belief)

if __name__ == '__main__':
    belief = Belief()
    belief.user_action()
