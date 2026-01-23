# Matrix Guide
# By: Alan Gładyś, Martyna Hedeszyńska

import functions
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    print("=" * 50)
    print("   MATRIX DLA OPORNYCH 🧮")
    print("   Prosty kalkulator macierzy")
    print("=" * 50)


def show_matrices(A, B):
    print("\nMacierz A:")
    functions.print_matrix(A)

    print("Macierz B:")
    functions.print_matrix(B)


def main_menu():
    print("\nWybierz operację:")
    print("1 - Dodawanie A + B")
    print("2 - Odejmowanie A - B")
    print("3 - Mnożenie A · B")
    print("4 - Dzielenie macierzy")
    print("5 - Transpozycja macierzy")
    print("6 - Wczytaj nowe macierze")
    print("0 - Wyjście")


def transpose_menu(A, B):
    print("\nTranspozycja:")
    print("1 - Transponuj A")
    print("2 - Transponuj B")
    print("0 - Powrót")

    choice = input("Wybór: ")

    if choice == "1":
        A = functions.transpose_matrix(A)
        print("\nMacierz A po transpozycji:")
        functions.print_matrix(A)

    elif choice == "2":
        B = functions.transpose_matrix(B)
        print("\nMacierz B po transpozycji:")
        functions.print_matrix(B)

    return A, B


def main():
    clear()
    print_header()

    # Wczytanie początkowych macierzy
    A = functions.get_matrix("A")
    B = functions.get_matrix("B")

    while True:
        clear()
        print_header()
        show_matrices(A, B)
        main_menu()

        choice = input("\nTwój wybór: ").strip()

        if choice == "1":
            functions.sum_matrices(A, B)
            input("\nENTER aby kontynuować...")

        elif choice == "2":
            functions.sub_matrices(A, B)
            input("\nENTER aby kontynuować...")

        elif choice == "3":
            functions.multiply_matrices(A, B)
            input("\nENTER aby kontynuować...")

        elif choice == "4":
            functions.divide_matrices(A, B)
            input("\nENTER aby kontynuować...")

        elif choice == "5":
            A, B = transpose_menu(A, B)
            input("\nENTER aby kontynuować...")

        elif choice == "6":
            A = functions.get_matrix("A")
            B = functions.get_matrix("B")

        elif choice == "0":
            print("\nDo zobaczenia! 👋")
            break

        else:
            print("\nNiepoprawny wybór.")
            input("ENTER aby spróbować ponownie...")


if __name__ == "__main__":
    main()
