# =========================
# Matrix Guide
# By: Alan Gładyś, Martyna Hedeszyńska
#
# =========================


# =========================
# FUNKCJE POMOCNICZE
# =========================

# Funkcja do czytelnego wyświetlania macierzy
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()
    print()
    input("Naciśnij Enter, aby kontynuować...")


# Transpozycja macierzy (zamiana wierszy na kolumny)
def transpose_matrix(matrix):
    transposed = []

    # Iteracja po kolumnach macierzy wejściowej
    for j in range(len(matrix[0])):
        transposed.append([])

        # Iteracja po wierszach macierzy wejściowej
        for i in range(len(matrix)):
            transposed[j].append(matrix[i][j])

    return transposed


# Sprawdzenie czy macierze mają takie same wymiary
# (warunek dodawania i odejmowania)
def can_add(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0])


# Sprawdzenie warunku mnożenia macierzy
# liczba kolumn A = liczba wierszy B
def can_multiply(A, B):
    return len(A[0]) == len(B)


# =========================
# INTERAKCJA Z UŻYTKOWNIKIEM
# =========================

# Pytanie o transpozycję macierzy
def ask_for_transpose():
    print("\nKtórą macierz chcesz przetransponować?")
    print("A - transponuj macierz A")
    print("B - transponuj macierz B")
    print("N - nie transponuj żadnej")

    while True:
        choice = input("Wybór (A/B/N): ").strip().upper()
        if choice in ["A", "B", "N"]:
            return choice
        print("Niepoprawny wybór.")


# Informacja o błędnych wymiarach macierzy (w razie błędu)
def inform_about_dimensions(A, B, operation):
    print(f"\nNie można wykonać operacji {operation}.")
    print(f"Wymiary A: {len(A)} x {len(A[0])}")
    print(f"Wymiary B: {len(B)} x {len(B[0])}")
    print("Możesz spróbować transpozycji jednej z macierzy.")

# Wybór macierzy do edycji przez użytkownika
def edit_matrix(A, B):

    # Sprawdzenie, czy macierze są puste
    if not A and not B:
        print("\nNie zdefiniowano macierzy A ani B. Musisz wprowadzić obie macierze.")
        A = get_matrix("A")
        B = get_matrix("B")
        return A, B

    # Jeśli przynajmniej jedna macierz nie jest pusta, użytkownik wybiera którą edytować
    print("\nKtórą macierz chcesz edytować?")
    print("A - edytuj macierz A")
    print("B - edytuj macierz B")

    while True:
        choice = input("Wybór (A/B): ").strip().upper()
        if choice in ["A", "B"]:
            break
        print("Niepoprawny wybór. Wpisz A lub B.")

    if choice == "A":
        A = get_matrix("A")
    else:
        B = get_matrix("B")

    return A, B



# Pobieranie macierzy od użytkownika
def get_matrix(name):
    print(f"\nPodaj wymiary macierzy {name}")

    while True:
        try:
            rows = int(input("Liczba wierszy: "))
            cols = int(input("Liczba kolumn: "))
            if rows > 0 and cols > 0:
                break
            print("Wymiary muszą być dodatnie.")
        except ValueError:
            print("Wpisz liczbę całkowitą.")

    matrix = []
    print(f"\nWprowadzaj dane do macierzy {name}:")

    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = float(input(f"{name}[{i}][{j}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Wpisz liczbę.")
        matrix.append(row)

    return matrix

# =========================
# DODAWANIE
# =========================

def sum_matrices(A, B):

    # Sprawdzenie możliwości dodawania
    if not can_add(A, B):
        print(f"Błąd: nie można dodać macierzy. Wymiary A: {len(A)}x{len(A[0])}, B: {len(B)}x{len(B[0])}")
        print("Macierze muszą mieć takie same wymiary.")
        return

    result = []

    # Dodawanie element po elemencie
    for i in range(len(A)):
        result.append([])
        for j in range(len(A[0])):
            result[i].append(A[i][j] + B[i][j])

    print("\nSuma A + B:")
    print_matrix(result)


# =========================
# ODEJMOWANIE
# =========================

def sub_matrices(A, B):

    # Sprawdzenie możliwości odejmowania
    if not can_add(A, B):
        print(f"Błąd: nie można odjąć macierzy. Wymiary A: {len(A)}x{len(A[0])}, B: {len(B)}x{len(B[0])}")
        print("Macierze muszą mieć takie same wymiary.")
        return

    result = []

    # Odejmowanie element po elemencie
    for i in range(len(A)):
        result.append([])
        for j in range(len(A[0])):
            result[i].append(A[i][j] - B[i][j])

    print("\nRóżnica A - B:")
    print_matrix(result)


# =========================
# MNOŻENIE
# =========================

def multiply_matrices(A, B):

    if not can_multiply(A, B):
        inform_about_dimensions(A, B, "mnożenia")
        choice = ask_for_transpose()

        if choice == "A":
            A = transpose_matrix(A)
        elif choice == "B":
            B = transpose_matrix(B)
        else:
            return

    if not can_multiply(A, B):
        print("Błąd: nie można wykonać mnożenia.")
        return

    result = []

    # Mnożenie macierzy
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            result[i].append(round(s, 2))

    print("\nWynik mnożenia A · B:")
    print_matrix(result)


# =========================
# MACIERZ ODWROTNA – METODA Z WYZNACZNIKA
# =========================

# Obliczanie wyznacznika macierzy (rekurencyjnie)
def determinant(matrix):
    n = len(matrix)

    # Sprawdzenie, czy macierz jest kwadratowa
    for row in matrix:
        if len(row) != n:
            print("Nie da się obliczyć wyznacznika – macierz nie jest kwadratowa.")
            return None

    # Przypadek 1x1
    if n == 1:
        return matrix[0][0]

    # Przypadek 2x2
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0

    # Dalszy podział macierzy na mniejsze podmacierze 
    for col in range(n):
        sub = []
        for i in range(1, n):
            sub.append(matrix[i][:col] + matrix[i][col+1:])

        det += ((-1) ** col) * matrix[0][col] * determinant(sub)

    return det

# Tworzenie podmacierzy z głównej macierzy (dopełnienia algebraiczne)
def cofactor_matrix(matrix):
    n = len(matrix)
    cofactors = []

    for i in range(n):
        row = []
        for j in range(n):
            sub = []
            for r in range(n):
                if r != i:
                    sub.append(matrix[r][:j] + matrix[r][j+1:])

            value = ((-1) ** (i + j)) * determinant(sub)
            row.append(value)
        cofactors.append(row)

    return cofactors


# Obliczanie macierzy odwrotnej z wyznacznika
def inverse_matrix(matrix):

    n = len(matrix)

    # Sprawdzenie czy macierz jest kwadratowa
    for row in matrix:
        if len(row) != n:
            print("Błąd: macierz nie jest kwadratowa.")
            return None

    det = determinant(matrix)

    # Macierz nieodwracalna
    if det == 0:
        print("Błąd: wyznacznik = 0, brak macierzy odwrotnej.")
        return None

    # Macierz dopełnień algebraicznych
    cof = cofactor_matrix(matrix)

    # Transpozycja macierzy kofaktorów → adjugata,
    # zgodnie ze wzorem: A⁻¹ = (1 / det(A)) · adj(A)
    adj = transpose_matrix(cof)

    inverse = []

    # Dzielenie przez wyznacznik
    for i in range(n):
        inverse.append([])
        for j in range(n):
            inverse[i].append(round(adj[i][j] / det, 2))

    return inverse


# =========================
# DZIELENIE MACIERZY
# =========================

def divide_matrices(A, B):

    # Sprawdzenie czy B jest macierzą kwadratową
    n = len(B)
    for row in B:
        if len(row) != n:
            print("Błąd: macierz B nie jest kwadratowa – nie można wykonać dzielenia.")
            return

    # Obliczanie macierzy odwrotnej B
    B_inv = inverse_matrix(B)
    if B_inv is None:
        print("Nie można wykonać dzielenia.")
        return
    

    print("\nDzielenie macierzy:")
    print("1 - A · B⁻¹")
    print("2 - B⁻¹ · A")

    choice = input("Wybór (1/2): ").strip()

    # Wybór kolejności mnożenia
    if choice == "1":
        left = A
        right = B_inv
        opis = "A · B⁻¹"
    elif choice == "2":
        left = B_inv
        right = A
        opis = "B⁻¹ · A"
    else:
        print("Niepoprawny wybór.")
        return

    if not can_multiply(left, right):
        print("Błąd: nieprawidłowe wymiary.")
        return

    result = []

    # Mnożenie macierzy
    for i in range(len(left)):
        result.append([])
        for j in range(len(right[0])):
            s = 0
            for k in range(len(right)):
                s += left[i][k] * right[k][j]
            result[i].append(round(s, 2))

    print(f"\nWynik dzielenia ({opis}):")
    print_matrix(result)