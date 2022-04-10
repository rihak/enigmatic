import random
import itertools
import sys
import math


class Enigmatic:
    # Operations terms indexes
    OPERATIONS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
    ]

    def __init__(self, enigma="xxxaxxbcxddbxdefxxxbxxecxgcaxxhfxxda*//**-"):
        self.enigma = enigma.lower()
        self.operators = [self.select_operator(self.enigma[operator + 36]) for operator in range(6)]

    # Quantifies how much an assignment is far from goal
    def distance(self, assignment):
        numbers = [sum([10**(3-i)*(assignment[ord(self.enigma[number*4+i]) - 97] if self.enigma[number*4+i] != 'x' else 0) for i in range(4)]) for number in range(9)]
        try:
            return sum([abs(self.operators[i](numbers[a], numbers[b]) - numbers[result]) for i, (a, b, result) in enumerate(self.OPERATIONS)])
        except ZeroDivisionError:
            return 119988

    # Formats a solution to a readable and printable string
    def format_solution(self, solution):
        self.variables = max([ord(self.enigma[i]) - 96 if self.enigma[i] != 'x' else 0 for i in range(36)])
        return "\n".join([f'{chr(variable + 97)} = {solution[variable]}' for variable in range(self.variables)])

    # Search goal through all possible assignment. Slow, but if a solution exists, it's guaranteed it will hit that
    def search_brute_force(self):
        for assignment in itertools.permutations(range(10)):
            if self.distance(assignment) == 0:
                return self.format_solution(assignment)
        return False

    # Search goal with Simulated Annealing algorithm. Fast, but could sometimes stuck looping around local minimums
    def search_simulated_annealing(self, shake_initial=250, shake_reduction=0.001, shake_limit=50):
        assignment = list(range(10))
        random.shuffle(assignment)
        step = -1
        while step < sys.maxsize:
            step += 1
            shake_amount = shake_initial * math.exp(-shake_reduction * step)
            if shake_amount < shake_limit:
                step = 0
            index_a, index_b = random.choice([(a, b) for a in range(10) for b in range(10) if a != b])
            assignment_next = list(assignment)
            assignment_next[index_a], assignment_next[index_b] = assignment_next[index_b], assignment_next[index_a]

            delta_e = self.distance(assignment) - self.distance(assignment_next)
            if delta_e > 0 or math.exp(delta_e / shake_amount) > random.uniform(0.0, 1.0):
                assignment = assignment_next

            if self.distance(assignment) == 0:
                return self.format_solution(assignment)

    # Return an operation function based on symbol
    def select_operator(self, symbol):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }[symbol]


#print(Enigmatic(input("Enter String:\n")).search_brute_force())
print(Enigmatic(input("Enter String:\n")).search_simulated_annealing())
