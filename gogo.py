import sympy
from time import sleep
import os
import numpy as np
from utils import *
from logic import *
from sympy.abc import _clash




class KB():
    """A KB for propositional logic. Inefficient, with no indexing."""

    def __init__(self):
        self.done = False
        self.clauses = []
        self.start()

    def add_sentence(self, sentence):
        """Add the sentence's clauses to the KB."""
        self.clauses.extend(conjuncts(to_cnf(sentence)))

    def ask_generator(self, query):
        """Yield the empty substitution {} if KB entails query; else no results."""
        if tt_entails(Expr('&', *self.clauses), query):
            yield {}

    def ask_if_true(self, query):
        """Return True if the KB entails query, else return False."""
        for _ in self.ask_generator(query):
            return True
        return False

    def retract(self, sentence):
        """Remove the sentence's clauses from the KB."""
        for c in conjuncts(to_cnf(sentence)):
            if c in self.clauses:
                self.clauses.remove(c)

    def get_input(self):
        input()
        # new_belief = str.lower(input())

        # #Fjern alle tal i string.. Skal man det?
        # new_belief = ''.join([i for i in new_belief if not i.isdigit()])

        # if new_belief == "quit":
        #     self.done = True
        # elif new_belief == "solve":
        #     if len(self.clauses) != 0:
        #         self.solve()
        #     else:
        #         print("Belief base is empty.")
        #         sleep(2)
        # elif new_belief == "ask":
        #     question = input()
        #     print(self.ask_if_true(question))
        # else:
        #     if new_belief != '':
        #         self.add_sentence(new_belief)
        #     else:
        #         print("Input is empty.")

        # self.add_sentence(a & b & c)
        # print(self.ask_if_true(b))



    def clear_terminal(self):
        pass
        # os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        self.clear_terminal()
        print("\nPossible actions:")
        print("Type a belief to add the belief to the belief base. Otherwise use 1 of the following codewords:")
        # print('"Display" the current belief base')
        print('"clear" the belief base')
        print('"quit" stop the agent')
        print('"solve" the current belief system')
    
    def solve(self):
        print(pl_true(self.clauses))

    def start(self):
        while not self.done:
            self.main_menu()
            self.get_input()


if __name__ == '__main__':
    k_b= KB()




























# class Belief:
#     def __init__(self):
#         self.belief_base = np.zeros(shape=(100,100), dtype=object)
#         self.belief_base_len = 0
#         self.done = False
#         self.start()

#     def reset(self):
#         sleep(2)
#         self.belief_base.clear()
#         self.belief_system = ""
#         self.done = False
#         self.start()

#     def clear_terminal(self):
#         pass
#         # os.system('cls' if os.name == 'nt' else 'clear')

#     def main_menu(self):
#         self.clear_terminal()

#         # print("Current belief base:", self.belief_base[self.belief_base != 0])

#         print("Current belief base:")
#         for i in self.belief_base:
#             if i[0] != 0:
#                 print(i[i != 0])
#         #     for j in range(y):
#         #         if self.belief_base[i][j] != 0:
#         #             print(self.belief_base[i][j])
        
            
#         print("Current belief system:", str.upper(self.belief_system))
#         print("\nPossible actions:")
#         print("Type a belief to add the belief to the belief base. Otherwise use 1 of the following codewords:")
#         # print('"Display" the current belief base')
#         print('"clear" the belief base')
#         print('"quit" stop the agent')
#         print('"solve" the current belief system')

#     def get_belief_system(self):
#         self.clear_terminal()

#         print("Choose a belief system: \nPL  (Propositional logic), \nRES (Resolution),\nCNF (CNF-form),\nAGM (AGM revision),\nPAR (Partial meet contraction)\n")
#         while True:
#             belief_options = ['pl', 'res', 'cnf', 'agm', 'par']
#             belief_system = str.lower(input())
#             if belief_system in belief_options:
#                 return belief_system
#             else:
#                 print('Invalid belief system.')

#     def get_input(self):
#         new_belief = str.lower(input())
#         #Fjern alle tal i string.. Skal man det?
#         new_belief = ''.join([i for i in new_belief if not i.isdigit()])

#         #rens inputtet somehow:
#         # Hvordan skal inputtet også se ud? Jeg forstår faktisk ikke rigtigt hvad der foregår tbh..

#         if new_belief == "clear":
#             self.belief_base.clear()
#         elif new_belief == "quit":
#             self.done = True
#         elif new_belief == "solve":
#             if len(self.belief_base) != 0:
#                 self.solve_belief_system()
#                 self.done = True
#                 self.reset()
#             else:
#                 print("Belief base is empty.")
#                 sleep(2)
#         else:
#             if new_belief != '':
#                 temp_base = np.array([],dtype=object)
#                 for i in new_belief:
#                     if i.isalpha():
#                         temp_base = np.append(temp_base, sympy.symbols(i))
#                     elif i == ("&" or "|" or "~" or "<" or ">" or "=" or "(" or ")"):
#                         temp_base = np.append(temp_base, i)
#                     else:
#                         print("invalid input")

#                 missing = 100 - len(temp_base)   
#                 for i in range(missing):
#                     temp_base = np.append(temp_base, 0)  
                    
#                 self.belief_base[self.belief_base_len] = temp_base
#                 self.belief_base_len += 1
#             else:
#                 print("Input is empty.")
                
                
#     #Solve funktioner.. Ved ikke om det skal fungere sådan her tbh
#     def solve_PL(self):
#         print("PL")
    
#     def solve_RES(self):
#         print("RES")
    
#     def solve_CNF(self):
#         print("CNF")
    
#     def solve_AGM(self):
#         print("AGM")

#     def solve_PAR(self):
#         print("PAR")

#     def solve_belief_system(self):
#         if self.belief_system == "pl":
#             self.solve_PL()
#         elif self.belief_system == "res":
#             self.solve_RES()
#         elif self.belief_system == "cnf":
#             self.solve_CNF()
#         elif self.belief_system == "agm":
#             self.solve_AGM()
#         elif self.belief_system == "par":
#             self.solve_PAR()

#     def is_valid(self):
        
#         for x in self.belief_base:
#             start_paran = 0
#             slut_paran = 0
#             print(x)
#             for j in range(len(x)):
#                 print(j)
#                 if x[j] == "(":
#                     start_paran += 1
#                     if x[j+1] == sympy.core.symbol.Symbol:
#                         pass
#                     else:
#                         print("invalid  1")
#                         return 1
#                 elif x[j] == ")":
#                     slut_paran += 1
#                 elif x[j] == ("&" or "|" or "~" or "<" or ">" or "="):
#                     if x[j+1] == sympy.core.symbol.Symbol:
#                         pass
#                     else:
#                         print("invalid  2")
#                         return 1
#                 elif x[j] == sympy.symbols:
#                     if x[j+1] == ("&" or "|" or "~" or "<" or ">" or "="):
#                         pass
#                     else:
#                         print("invalid  3")
#                         return 1
#             if start_paran != slut_paran:
#                 print("parentheses error")
#         return 0

#     def start(self):
#         self.belief_system = self.get_belief_system()
#         while(not self.done):
#             self.main_menu()

#             self.get_input()

#             if self.is_valid() == 1:
#                 print("is not good")
#                 sleep(3)

# if __name__ == '__main__':
#     belief = Belief()


