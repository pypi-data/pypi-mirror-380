import numpy as np


def preprocess_input(s: str) -> str:
    s = s.strip().replace("−", "-")  # Replace LaTex minus with correct minus

    return s


def string_to_matrix(s: str) -> np.ndarray:
    s = preprocess_input(s)

    # Matrix creation
    rows = s.split("\n")

    n = len(rows)  # Number of rows
    m = len(rows[0].split())  # Number of cols

    A = np.zeros((n, m))
    for i, row in enumerate(rows):
        A[i] = np.array(list(map(float, row.split())))

    return A


def string_to_vector(s: str) -> np.ndarray:
    s = preprocess_input(s)
    separator = "\n" if "\n" in s else " "

    return np.array(list(map(float, s.split(separator))))