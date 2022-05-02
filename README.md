# AI-belief_system

run main.py and you will be prompted with 4 options: 

1: Attempt to add a new belief to the belief base if it passes logical entailment. <br />
2: Check if a belief would pass logical entailment in the current knowledge base. <br />
3: Remove a belief from the knowledge base. <br />
4: Remove the entire knowledge base. <br />
5: Exit program.

When entering beliefs make sure to follow the syntax as shown below:

| Function | Book notation | Python input notation |
| :---: | :---: | :---: |
| NOT | ¬A | ~A |
| AND | A∧B | A&B |
| OR | A∨B | A&#124;B |
| XOR | A≠B | A^B |
| IMPLICATION | A→B | A==>B |
| REVERSE IMPLICATION | A←B | A<==B |
| EQUIVILANCE | A↔B | A<=>B |

Code for handling symbols, conversions and symbol arithmatic can be found in the following 2 files: <br />
https://github.com/aimacode/aima-python/blob/master/utils.py <br />
https://github.com/aimacode/aima-python/blob/master/logic.py
