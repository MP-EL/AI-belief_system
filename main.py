from utils import *
from logic import *
from time import sleep
import os.path


class KB:
    def __init__(self):
        self.clauses = ""
        self.done = False

        self.start()
    def clear_terminal(self):
        # pass
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        self.clear_terminal()
        if self.clauses != "":
            print("Knowledge base:",self.clauses)
        else: 
            print("No knowledge base")
        print("\nPossible actions:")
        print('"1" Add a belief to the knowledge base with checking for logical entailment')
        print('"2" Check new belief for logical entailment with knowledge base')
        print('"3" Remove a belief from the knowledge base')
        print('"4" Remove entire knowledge base')
        print('"5" Exit program')

    def start(self):
        while not self.done:
            self.main_menu()
            self.get_input()

    def get_input(self):
        text = input("\nEnter a command: ")
        if text == "1":
            new_belief = str(to_cnf(str.upper(input("Enter a belief: "))))
            if self.clauses != "":
                temp = self.clauses.replace(" , ", " & ")
                # print(temp)
                if tt_entails(to_cnf(temp), to_cnf(new_belief)):
                    self.clauses = "".join(self.clauses + " , " + new_belief)
                    print("Successfully added new belief")
                    sleep(2)
                else:
                    print("Belief is logically entailed in belief base. Therefore not added.")
                    sleep(2)
            else:
                self.clauses = new_belief

        elif text == "2":
            new_belief = str(to_cnf(str.upper(input("Enter a belief: "))))
            if self.clauses != "":
                temp = self.clauses.replace(" , ", " & ")
                # print(temp)
                if tt_entails(to_cnf(temp), to_cnf(new_belief)):
                    print("Belief is logically entailed in belief base")
                    sleep(2)
                else:
                    print("Belief is not logically entailed in belief base ")
                    sleep(2)
            else:
                print("Belief base is empty")

        elif text == "3":
            new_belief = str(to_cnf(str.upper(input("Enter a belief to remove: "))))
            if new_belief in self.clauses:
                sep = " , "
                self.clauses = sep.join([ i for i in self.clauses.split(sep) if i != new_belief ])
                print("Belief removed")
                sleep(2)
            else:
                print("Entered belief not found in belief base")
                sleep(2)
        elif text == "4":
            self.clauses = ""
            print("Belief base removed")
            sleep(2)
        elif text == "5":
            print("Exiting program")
            self.done = True


k_b = KB()

