# Matrix Guide
# By: Alan Gładyś, Martyna Hedeszyńska
#
# Operacje na macierzach z walidacją danych
# oraz świadomą transpozycją wybieraną przez użytkownika


# =========================
# FUNKCJE POMOCNICZE
# =========================

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()
    print()


def transpose_matrix(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        transposed.append([])
        for i in range(len(matrix)):
            transposed[j].append(matrix[i][j])
    return transposed


def can_add(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0])


def can_multiply(A, B):
    return len(A[0]) == len(B)


# =========================
# INTERAKCJA Z UŻYTKOWNIKIEM
# =========================

def ask_for_transpose():
    print("\nKtórą macierz chcesz przetransponować?")
    print("A - transponuj macierz A")
    print("B - transponuj macierz B")
    print("N - nie transponuj żadnej")

    while True:
        choice = input("Wybór (A/B/N): ").strip().upper()
        if choice in ["A", "B", "N"]:
            return choice
        print("Niepoprawny wybór. Wpisz A, B lub N.")


def inform_about_dimensions(A, B, operation):
    print(f"\nNie można wykonać operacji {operation}.")
    print(f"Wymiary A: {len(A)} x {len(A[0])}")
    print(f"Wymiary B: {len(B)} x {len(B[0])}")
    print("Możesz spróbować transpozycji jednej z macierzy.")


def get_matrix(name):
    print(f"\nPodaj wymiary macierzy {name}")

    while True:
        try:
            rows = int(input("Liczba wierszy: "))
            cols = int(input("Liczba kolumn: "))

            if rows <= 0 or cols <= 0:
                print("Wymiary muszą być dodatnie.")
                continue
            break
        except ValueError:
            print("Błąd: wymiary muszą być liczbami całkowitymi.")

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
                    print("Błąd: wpisz liczbę.")
        matrix.append(row)

    return matrix


# =========================
# DODAWANIE 
# =========================

def sum_matrices(A, B):
    if not can_add(A, B):
        inform_about_dimensions(A, B, "dodawania")
        choice = ask_for_transpose()

        if choice == "A":
            A = transpose_matrix(A)
        elif choice == "B":
            B = transpose_matrix(B)
        else:
            print("Operacja przerwana.")
            return

    if not can_add(A, B):
        print("Błąd: nie można dodać macierzy.")
        return

    result = []
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
    if not can_add(A, B):
        inform_about_dimensions(A, B, "odejmowania")
        choice = ask_for_transpose()

        if choice == "A":
            A = transpose_matrix(A)
        elif choice == "B":
            B = transpose_matrix(B)
        else:
            print("Operacja przerwana.")
            return

    if not can_add(A, B):
        print("Błąd: nie można odjąć macierzy.")
        return

    result = []
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
    # Sprawdzamy, czy mnożenie A · B jest możliwe
    if not can_multiply(A, B):
        inform_about_dimensions(A, B, "mnożenia (A · B)")
        print("Uwaga: kolejność mnożenia ma znaczenie!")
        choice = ask_for_transpose()

        # Transpozycja wybranej macierzy
        if choice == "A":
            A = transpose_matrix(A)
        elif choice == "B":
            B = transpose_matrix(B)
        else:
            print("Operacja przerwana.")
            return

    # Ponowne sprawdzenie po ewentualnej transpozycji (W przypadku gdy transpozycja nie pomogła)
    if not can_multiply(A, B):
        print("Błąd: nie można wykonać mnożenia.")
        return

    result = []

    # Iterujemy po wierszach macierzy A
    for i in range(len(A)):
        result.append([])

        # Iterujemy po kolumnach macierzy B
        for j in range(len(B[0])):
            s = 0

            # Obliczamy iloczyn wiersza i kolumny
            for k in range(len(B)):
                s += A[i][k] * B[k][j]

            # Zaokrąglamy wynik do 2 miejsc po przecinku
            result[i].append(round(s, 2))

    print("\nWynik mnożenia A · B:")
    print_matrix(result)



# =========================
# DZIELENIE (A · B⁻¹)
# =========================

def identity_matrix(n):
    I = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        I.append(row)
    return I


def inverse_matrix(matrix):
    n = len(matrix)

    for row in matrix:
        if len(row) != n:
            print("Błąd: macierz nie jest kwadratowa.")
            return None

    A = [row.copy() for row in matrix]
    I = identity_matrix(n)

    for i in range(n):
        if A[i][i] == 0:
            print("Błąd: macierz nie ma odwrotności.")
            return None

        d = A[i][i]
        for j in range(n):
            A[i][j] /= d
            I[i][j] /= d

        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    I[k][j] -= factor * I[i][j]

    return I


def divide_matrices(A, B):
    print("\nDzielenie macierzy:")

    print("1 - A · B⁻¹")
    print("2 - B⁻¹ · A")

    # Pobieramy wybór użytkownika
    while True:
        choice = input("Wybierz sposób dzielenia (1/2): ").strip()
        if choice in ["1", "2"]:
            break
        print("Niepoprawny wybór.")

    # Obliczamy macierz odwrotną B
    B_inv = inverse_matrix(B)
    if B_inv is None:
        print("Nie można wykonać dzielenia.")
        return

    # Wariant 1: A · B⁻¹
    if choice == "1":
        left = A
        right = B_inv
        opis = "A · B⁻¹"

    # Wariant 2: B⁻¹ · A
    else:
        left = B_inv
        right = A
        opis = "B⁻¹ · A"

    # Sprawdzamy, czy wybrane mnożenie jest możliwe
    if not can_multiply(left, right):
        inform_about_dimensions(left, right, "dzielenia")
        trans_choice = ask_for_transpose()

        # Transpozycja wybranej macierzy
        if trans_choice == "A":
            left = transpose_matrix(left)
        elif trans_choice == "B":
            right = transpose_matrix(right)
        else:
            print("Operacja przerwana.")
            return

    # Ostateczna walidacja
    if not can_multiply(left, right):
        print("Błąd: nie można wykonać dzielenia.")
        return

    result = []

    # Mnożenie macierzy
    for i in range(len(left)):
        result.append([])
        for j in range(len(right[0])):
            s = 0
            for k in range(len(right)):
                s += left[i][k] * right[k][j]

            # Zaokrąglanie wyniku
            result[i].append(round(s, 2))

    print(f"\nWynik dzielenia ({opis}):")
    print_matrix(result)



