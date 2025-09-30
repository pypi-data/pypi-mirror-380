from sympy import Eq
from sympy.parsing.sympy_parser import parse_expr


def string_to_symbolic_equation(equation: str):
    equation_parts = equation.split("=")
    if not len(equation_parts) == 2:
        return
    rhs, lhs = equation_parts
    return Eq(parse_expr(rhs), parse_expr(lhs))