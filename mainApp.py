# Matrix Guide
# By: Alan Gładyś, Martyna Hedeszyńska

import functions

print("Matrix dla opornych - program do wykonywania podstawowych działań na macierzach.")
input()

# Przykładowe macierze do działań
A = []
B = []
# A = [[2,1,0],[1,1,2],[3,0,1]]
# A = [[2,1],[1,1],[3,0]]
# B = [[3,1,2],[3,-2,1],[-3,5,9]]
# B = [[3,1],[3,-2],[-3,5]]

def pick_Matrix():
    print("Wybierz macierz do działania:")
    print("A - Macierz A")
    print("B - Macierz B")

    while True:
        choice = input("Wybór: ").strip().upper()
        if choice == 'A':
            return A
        elif choice == 'B':
            return B
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
while True:
    print("\n=== GŁÓWNE MENU ===")
    print("1 - Działania na macierzach")
    print("2 - Samouczek macierzy")
    print("3 - Porównanie czasu wykonywania działań na macierzach (numpy vs Alan & Martyna)")
    print("4 - Wyjście")

    main_choice = input("Wybór: ").strip()

    if main_choice == '1':
        while True:
            print("\nWybierz operację do wykonania:")
            print("1 - Wprowadź własne macierze")
            print("2 - Dodawanie macierzy")
            print("3 - Odejmowanie macierzy")
            print("4 - Mnożenie macierzy")
            print("5 - Dzielenie macierzy")
            print("6 - Transpozycja macierzy")
            print("7 - Wyznacznik macierzy")
            print("8 - Inwersja macierzy")
            print("9 - Powrót do głównego menu")

            choice = input("Wybór: ").strip()

            if choice == '1':
                A, B = functions.edit_matrix(A, B)

            elif choice == '2':
                functions.sum_matrices(A, B)

            elif choice == '3':
                functions.sub_matrices(A, B)

            elif choice == '4':
                functions.multiply_matrices(A, B)

            elif choice == '5':
                functions.divide_matrices(A, B)

            elif choice == '6':
                M = pick_Matrix()
                print("Macierz przed transpozycją:")
                functions.print_matrix(M)
                print("Macierz po transpozycji:")
                functions.print_matrix(functions.transpose_matrix(M))

            elif choice == '7':
                M = pick_Matrix()
                if(functions.determinant(M) is None):
                    continue
                else:
                    print("Wyznacznik macierzy wynosi:")
                    print(functions.determinant(M))

            elif choice == '8':
                M = pick_Matrix()
                if(functions.inverse_matrix(M) is None):
                    continue
                else:
                    print("\nMacierz przed inwersją:")
                    functions.print_matrix(M)
                    print("Macierz odwrotna (po inwersji):")
                    functions.print_matrix(functions.inverse_matrix(M))

            elif choice == '9':
                print("Powrót ")
                break

            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    elif main_choice == '2':
        print("\nSamouczek macierzy, work in progress...")
    elif main_choice == '3':
        print("\nPorównanie czasu wykonywania działań na macierzach - U GO GIRL ")
    elif main_choice == '4':
        print("Zamykanie programu. Do zobaczenia!")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")