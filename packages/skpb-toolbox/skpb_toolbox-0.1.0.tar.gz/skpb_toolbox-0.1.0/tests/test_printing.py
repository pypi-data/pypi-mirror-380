import numpy as np
import sympy as sp
from skpb_toolbox.printing import (
    get_significant_digits,
    vec_get_significant_digits,
)


class Test_get_significant_digits:
    def test_TestCase1(self):
        x = 1162
        x_expected = sp.Symbol("1.2e+03")

        assert vec_get_significant_digits(x, 2) == x_expected

    def test_TestCase2(self):
        x = 0.0001
        x_expected = sp.Symbol("1.00e-04")

        assert get_significant_digits(x, 3) == x_expected

    def test_TestCase3(self):
        x = -0.0001
        x_expected = sp.Symbol("-1.00e-04")

        assert get_significant_digits(x, 3) == x_expected

    def test_TestCase4(self):
        x = np.array([1162, 0.001])
        x_expected = np.array(sp.symbols("1.2e+03 1.0e-03"))
        x_result = vec_get_significant_digits(x, 2)
        assert np.array_equal(x_result, x_expected)

    def test_TestCase5(self):
        x = np.array([[1162, 0.001], [1342, 0.005]])
        x_expected = np.array(
            [sp.symbols("1.2e+03 1.0e-03"), sp.symbols("1.3e+03 5.0e-03")]
        )
        x_result = vec_get_significant_digits(x, 2)
        assert np.array_equal(x_result, x_expected)

    def test_TestCase6(self):
        x = sp.Matrix([[1162, 0.001], [1342, 0.005]])
        x_expected = sp.Matrix(
            [
                [sp.Symbol("1.2e+03"), sp.Symbol("1.0e-03")],
                [sp.Symbol("1.3e+03"), sp.Symbol("5.0e-03")],
            ],
        )
        result = vec_get_significant_digits(x, 2)
        x_result = sp.Matrix(result, evaluate=False)
        assert x_result == x_expected

    def test_TestCase7(self):
        x = 0.00772968
        x_expected = sp.Symbol("7.73e-03")
        x_result = get_significant_digits(x, 3)
        assert x_result == x_expected