from math import copysign, log10

from IPython.display import display
from numpy import floor, ndarray, vectorize
from sympy import Expr, Matrix, Rel, Symbol, SympifyError


def display_matrix(matrix: ndarray) -> None:
    display(Matrix(matrix))


def display_variable_equation(
    variable: str | Expr,
    value: Expr | Matrix,
    n_significant_digits: int | None = None,
    relation_operator: str = "==",
) -> None:
    if n_significant_digits is not None:
        value = vec_get_significant_digits(value, n_significant_digits)

    if isinstance(variable, str):
        variable = Symbol(variable)

    try:
        display(Rel(variable, value, relation_operator, evaluate=False))
    except SympifyError:
        display(Rel(variable, Matrix(value), relation_operator, evaluate=False))


def get_significant_digits(x: float, digits: int = 1) -> str:
    """Return the number of significant digits in x."""
    sign = copysign(1, x)
    x = abs(x)
    factor = floor(log10(abs(x)))
    offset = 10.0 ** (factor - digits + 1)
    x_new = x / offset

    if x_new % 1 > 0.5:
        x_new += 1

    x_new = str(int(x_new))
    x_new = int(x_new) * offset * sign
    return Symbol(f"{x_new:.{abs(digits) - 1}e}")


vec_get_significant_digits = vectorize(get_significant_digits)