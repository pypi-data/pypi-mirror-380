from decimal import Decimal, ROUND_HALF_UP

import numpy as np
import sympy as sp


def round_scientific(x: float, ndigits=0):
    return float(
        Decimal(str(x)).quantize(
            Decimal("1e-%d" % ndigits), rounding=ROUND_HALF_UP
        )
    )