# =========================
# Matrix Guide
# By: Alan Gładyś, Martyna Hedeszyńska
#
# Logika matematyczna (bez interakcji konsolowej)
# =========================

import time
import numpy as np


# =========================
# FUNKCJE POMOCNICZE
# =========================

def transpose_matrix(matrix):
    """Zwraca transpozycję macierzy."""
    return [
        [matrix[i][j] for i in range(len(matrix))]
        for j in range(len(matrix[0]))
    ]


def can_add(A, B):
    """Sprawdza czy macierze mają takie same wymiary."""
    return len(A) == len(B) and len(A[0]) == len(B[0])


def can_multiply(A, B):
    """Sprawdza warunek mnożenia macierzy A · B."""
    return len(A[0]) == len(B)


# =========================
# OPERACJE PODSTAWOWE
# =========================

def add_matrices(A, B):
    if not can_add(A, B):
        return None

    return [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def sub_matrices(A, B):
    if not can_add(A, B):
        return None

    return [
        [A[i][j] - B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def multiply_matrices(A, B):
    if not can_multiply(A, B):
        return None

    return [
        [
            round(sum(A[i][k] * B[k][j] for k in range(len(B))), 2)
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


# =========================
# WYZNACZNIK
# =========================

def determinant(matrix):
    n = len(matrix)

    if any(len(row) != n for row in matrix):
        return None

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        sub = [
            matrix[i][:col] + matrix[i][col+1:]
            for i in range(1, n)
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det


def cofactor_matrix(matrix):
    n = len(matrix)
    cofactors = []

    for i in range(n):
        row = []
        for j in range(n):
            sub = [
                matrix[r][:j] + matrix[r][j+1:]
                for r in range(n) if r != i
            ]
            row.append(((-1) ** (i + j)) * determinant(sub))
        cofactors.append(row)

    return cofactors


def inverse_matrix(matrix):
    n = len(matrix)

    if any(len(row) != n for row in matrix):
        return None

    det = determinant(matrix)
    if det == 0 or det is None:
        return None

    adj = transpose_matrix(cofactor_matrix(matrix))

    return [
        [round(adj[i][j] / det, 2) for j in range(n)]
        for i in range(n)
    ]


# =========================
# BENCHMARK
# =========================

def benchmark(operation, A, B, repeats=1000):
    """
    operation:
    'add', 'sub', 'mul', 'a_div_b', 'b_div_a'
    """

    start_manual = time.perf_counter()

    for _ in range(repeats):
        if operation == "add":
            result_manual = [
                [A[i][j] + B[i][j] for j in range(len(A[0]))]
                for i in range(len(A))
            ]

        elif operation == "sub":
            result_manual = [
                [A[i][j] - B[i][j] for j in range(len(A[0]))]
                for i in range(len(A))
            ]

        elif operation == "mul":
            result_manual = [
                [
                    sum(A[i][k] * B[k][j] for k in range(len(B)))
                    for j in range(len(B[0]))
                ]
                for i in range(len(A))
            ]

        elif operation == "a_div_b":
            B_inv = inverse_matrix(B)
            if B_inv is None:
                return None
            result_manual = multiply_matrices(A, B_inv)

        elif operation == "b_div_a":
            A_inv = inverse_matrix(A)
            if A_inv is None:
                return None
            result_manual = multiply_matrices(A_inv, B)

    end_manual = time.perf_counter()

    np_A = np.array(A)
    np_B = np.array(B)

    start_numpy = time.perf_counter()

    for _ in range(repeats):
        if operation == "add":
            result_numpy = np_A + np_B
        elif operation == "sub":
            result_numpy = np_A - np_B
        elif operation == "mul":
            result_numpy = np_A @ np_B
        elif operation == "a_div_b":
            result_numpy = np_A @ np.linalg.inv(np_B)
        elif operation == "b_div_a":
            result_numpy = np.linalg.inv(np_A) @ np_B

    end_numpy = time.perf_counter()

    return {
        "manual_result": result_manual,
        "numpy_result": result_numpy.tolist(),
        "manual_time": (end_manual - start_manual) / repeats,
        "numpy_time": (end_numpy - start_numpy) / repeats
    }
