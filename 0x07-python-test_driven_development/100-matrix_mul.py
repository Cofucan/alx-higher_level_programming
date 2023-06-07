#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        matrix_a (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.

    Returns:
        list of lists of ints/floats: A new matrix representing the
        multiplication of matrix_a by matrix_b.

    Raises:
        ValueError: If matrix_a or matrix_b is empty.
        TypeError: If m_a or m_b is not a list or they are not lists of lists.
                   If m_a or m_b contains elements other than ints or floats.
                   If the rows of m_a or m_b are not of the same size.
        ValueError: If the number of columns in matrix_a is not equal to the
                    number of rows in matrix_b.
    """

    if not m_a or m_a == [[]]:
        raise ValueError("matrix_a cannot be empty")
    if not m_b or m_b == [[]]:
        raise ValueError("matrix_b cannot be empty")

    if not isinstance(m_a, list):
        raise TypeError("matrix_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("matrix_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("matrix_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("matrix_b must be a list of lists")

    if not all(
        isinstance(el, (int, float))
        for el in [num for row in m_a for num in row]
    ):
        raise TypeError("matrix_a should contain only integers or floats")
    if not all(
        isinstance(el, (int, float))
        for el in [num for row in m_b for num in row]
    ):
        raise TypeError("matrix_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of matrix_a must have the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of matrix_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("matrix_a and matrix_b cannot be multiplied")

    inverted_b = [
        [m_b[c][r] for c in range(len(m_b))] for r in range(len(m_b[0]))
    ]

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = sum(row[i] * col[i] for i in range(len(col)))
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
