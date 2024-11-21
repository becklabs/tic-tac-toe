from z3 import Solver, Not, Implies, unsat


def is_tautology(expr):
    """
    Determines if the logical expression is a tautology (true under all possible variable assignments).

    Args:
        expr: A Z3 Boolean expression to check

    Returns:
        bool: True if the expression is a tautology, False otherwise
    """
    s = Solver()
    s.add(Not(expr))

    return s.check() == unsat


def implies(antecedent, consequent):
    """
    Checks if a logical implication between two expressions (antecedent → consequent) holds for all assignments.

    Args:
        antecedent: A Z3 Boolean expression representing the antecedent: The left side of the implication
        consequent: A Z3 Boolean expression representing the consequent: The right side of the implication

    Returns:
        bool: True if the implication is a tautology, False otherwise
    """
    return is_tautology(Implies(antecedent, consequent))
