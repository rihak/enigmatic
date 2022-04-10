# Enigmatic
A tool for solving "Calcolo Enigmatico" puzzle from the weekly "[La Settimana Enigmistica](https://en.wikipedia.org/wiki/La_Settimana_Enigmistica)" italian magazine.

# The Mission
Solving "Calcolo Enigmatico" from "[La Settimana Enigmistica](https://en.wikipedia.org/wiki/La_Settimana_Enigmistica)" is not far from solving a system of equations: you only need to play smarter and find a solution while exploiting some basic math operation rules.

You're presented with symbols (which we're going to replace with letters for simplicity) that hide digits from 0 to 9 behind them and a set of twisted operations like follows:

```
   a *   bc =  ddb
   *      *      -
 def /    b =   ec
------------------
 gca /   hf =   da
```

The same symbol, the same digit.

There are 6 operations between numbers composed by digits: three multiplications, two divisions and one subtraction for this one.

e.g.: first row satisfies: `(a) * (10b+c) = (100d+10d+b)`, third column satisfies: `(100d+10d+b) - (10e+c) = (10d+a)`

# Assumptions
- There are always 6 operations and they are always disposed in the way they are in the example
- Each operand of each operation is never going to be greater than 9999, so 4 is the maximum number of digits an operand can have: `0 < operand < 1000`
# Usage
After launching

```python
python3 enigmatic.py
```
you will be asked for a string. This string represent the enigma itself.

There are 9 operand in total, so each number is going to have a maximum of 4 hiddend digits, plus 6 operands which take string lenght to 42 characters.

Operand are red by rows and from left to right. Operators are red from top to down, for row operations first, and then from left to right for columns operations next. If one or two or three digits of any number are missing, just replace them with 'x's.

For example, the above enigma is represented by the following string:
```
xxxaxxbcxddbxdefxxxbxxecxgcaxxhfxxda*//**-
```
Once the enigma string is inserted, just press Enter and wait for a solution to be printed.


