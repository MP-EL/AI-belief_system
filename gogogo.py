from utils import *
from logic import *
from time import sleep


class KB:
    def __init__(self):
        self.clauses = ""
        self.done = False
        # self.ques = to_cnf("A & B & C")
        # self.ques2 = to_cnf("B")
        self.done = False
        self.start()
    def clear_terminal(self):
        # pass
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        self.clear_terminal()
        print(self.clauses)
        if self.clauses != "":
            temp = self.clauses.replace(" , ", " & ")
            print(to_cnf(temp))
        print("\nPossible actions:")
        print('"1" to add a belief to the belief base without LE')
        print('"2" to add a belief to the belief base with LE')
        print('"3" check if belief is valid')
        print('"4" remove a belief from the belief base')

    def start(self):
        while not self.done:
            self.main_menu()
            self.get_input()

    def check_base(self,kb, model={}):
        print(kb)
        symbols = list(prop_symbols(kb))
        return self.check_base2(kb,symbols,model)

    def check_base2(self, kb, symbols, model={}):
        if not symbols:
            if pl_true(kb, model):
                result = pl_true(True, model)
                assert result in (True, False)
                return result
            else:
                return True
        else:
            P, rest = symbols[0], symbols[1:]
            return (self.check_base2(kb, rest, extend(model, P, True)) and self.check_base2(kb, rest, extend(model, P, False)))

    def get_input(self):
        text = input("\nEnter a command: ")
        if text == "1":
            new_belief = str(to_cnf(str.upper(input("Enter a belief: "))))
            if self.clauses != "":
                self.clauses = "".join(self.clauses + " , " + new_belief)
            else:
                self.clauses = new_belief
        elif text == "2":
            new_belief = str(to_cnf(str.upper(input("Enter a belief: "))))
            if self.clauses != "":
                temp = self.clauses.replace(" , ", " & ")
                print(temp)
                if tt_entails(to_cnf(temp), to_cnf(new_belief)):
                    self.clauses = "".join(self.clauses + " , " + new_belief)
                    print("successfully added new belief")
                else:
                    print("could not solve LE belief was not added ")
                    sleep(2)
            else:
                self.clauses = new_belief
        elif text == "3":
            temp = self.clauses.replace(" , ", " & ")
            validity = self.check_base(to_cnf(temp), {})
            print(validity)
            print(f"Belief base is {'valid' if validity else 'invalid'}")
            sleep(2)
        elif text == "4":
            new_belief = str(to_cnf(str.upper(input("Enter a belief to remove: "))))
            if new_belief in self.clauses:
                self.clauses = self.clauses.replace(", " + new_belief, "")
                print("Belief removed")

    def check_if_solveable(self):
        temp = self.clauses.replace(" , ", " & ")
        print(temp)
        # print(tt_entails(temp, ))

    def print_cnf(self):
        print(self.clauses)


k_b = KB()

