# AI-belief_system

run main.py and make sure to use the following syntax for symbols:

~   = NOT <br />
&   = AND <br />
|   = OR <br />
==> = Implication <br />
<== = Reversed implication <br />
<=> = Equivalence <br />

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
