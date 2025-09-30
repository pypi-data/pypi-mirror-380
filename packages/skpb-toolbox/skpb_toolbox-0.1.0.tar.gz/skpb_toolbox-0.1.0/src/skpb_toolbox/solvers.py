from sympy import Symbol, solve, lambdify
from typing import List, Union

from .symbolic import string_to_symbolic_equation


def solve_string_equations(
    str_equations: Union[str, List[str]],
    symbols: Union[str, List[str]],
    lambdify_solutions: bool = True,
    verbose: bool = True,
):
    if isinstance(str_equations, str):
        str_equations = [str_equations]

    if isinstance(symbols, str):
        symbols = [symbols]

    sym_equations = [string_to_symbolic_equation(eq) for eq in str_equations]
    solutions = solve(sym_equations, symbols)

    if isinstance(solutions, dict):
        solutions = [solutions]

    for i, solution in enumerate(solutions):
        symbol_solutions = {}

        for j, symbol in enumerate(symbols):
            symbol_solution = (
                solution[Symbol(symbol)] if isinstance(
                    solution, dict) else solution[j]
            )
            symbol_solution = symbol_solution.simplify()
            variables = [str(var) for var in symbol_solution.free_symbols]
            variables.sort()

            if verbose:
                print(
                    f"Solution {i}: {symbol}({', '.join(variables)}) = {symbol_solution}"
                )

            if lambdify_solutions:
                lambda_solution = lambdify(variables, symbol_solution)
                lambda_solution.expression = symbol_solution
                symbol_solutions[symbol] = lambda_solution
            else:
                symbol_solutions[symbol] = symbol_solution

        solutions[i] = (
            symbol_solutions if len(symbol_solutions) > 1 else lambda_solution
        )

    return solutions if len(solutions) > 1 else solutions[0]
