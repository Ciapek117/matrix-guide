# Samouczek macierzy – OPERACJE NA MACIERZACH
# Aplikacja edukacyjna: teoria + przykłady krok po kroku

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Matrix Guide – operacje na macierzach")
root.geometry("1000x720")


def show_text(title, content):
    text_title.config(text=title)
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, content)
    text_box.config(state="disabled")


# =========================
# TREŚCI EDUKACYJNE
# =========================

ADD_TEXT = """
DODAWANIE MACIERZY (A + B)

CO TO JEST?
Dodawanie macierzy polega na dodawaniu odpowiadających sobie elementów.

WARUNEK:
Macierze MUSZĄ mieć takie same wymiary.

JAK TO ZROBIĆ KROK PO KROKU?
1. Sprawdź wymiary macierzy
2. Dodaj elementy o tych samych pozycjach
3. Zapisz wynik w nowej macierzy

PRZYKŁAD:
A = [ 4  -1 ]
       [ 7   3 ]

B = [ -2  5 ]
       [  6 -4 ]

OBLICZENIA:
[4 + (-2)        -1 + 5]
[7 + 6            3 + (-4)]

WYNIK:
[ 2   4 ]
[13  -1 ]

UWAGI:
• A + B = B + A
• Jeśli wymiary są różne → NIE DA SIĘ dodać
"""

SUB_TEXT = """
ODEJMOWANIE MACIERZY (A - B)

CO TO JEST?
Odejmowanie polega na odejmowaniu elementów macierzy B od macierzy A.

WARUNEK:
Macierze muszą mieć takie same wymiary.

PRZYKŁAD:
A = [ 8  -3 ]
       [ 1   6 ]

B = [ 5   2 ]
       [ -4  1 ]

OBLICZENIA:
[8 - 5            -3 - 2]
[1 - (-4)        6 - 1]

WYNIK:
[ 3  -5 ]
[ 5   5 ]

UWAGI:
• A - B ≠ B - A
• Kolejność ma znaczenie
"""

MUL_TEXT = """
MNOŻENIE MACIERZY (A · B)

CO TO JEST?
Mnożenie macierzy polega na:
wiersz (A) × kolumna (B) → suma iloczynów
czyli: A[i,1] · B[1,j] + A[i,2] · B[2,j] + ... + A[i,n] · B[n,j]

WARUNEK:
Liczba kolumn A = liczba wierszy B

================================
PRZYKŁAD (2x2)
================================
A = [ 2  -1 ]
       [ 4   3 ]

B = [ 5   2 ]
       [ -3  1 ]

OBLICZENIA:
[2·5 + (-1)·(-3)    2·2 + (-1)·1]
[4·5 + 3·(-3)       4·2 + 3·1]

WYNIK:
[13   3]
[11  11]

================================
PRZYKŁAD (3x3) 
================================
A = [ 1   2   0 ]
       [ -1  3   4 ]
       [ 2   1  -2 ]

B = [ 2   1   3 ]
       [ 0  -1   4 ]
       [ 5   2   1 ]

OBLICZENIA:
(1,1): 1·2 + 2·0 + 0·5 = 2
(1,2): 1·1 + 2·(-1) + 0·2 = -1
(1,3): 1·3 + 2·4 + 0·1 = 11

(2,1): -1·2 + 3·0 + 4·5 = 18
(2,2): -1·1 + 3·(-1) + 4·2 = 4
(2,3): -1·3 + 3·4 + 4·1 = 13

(3,1): 2·2 + 1·0 + (-2)·5 = -6
(3,2): 2·1 + 1·(-1) + (-2)·2 = -3
(3,3): 2·3 + 1·4 + (-2)·1 = 8

WYNIK:
[  2  -1  11 ]
[ 18   4  13 ]
[ -6  -3   8 ]

UWAGI:
• A·B ≠ B·A
• Wymiary MUSZĄ się zgadzać ( kolumny A = wiersze B )
"""

TRANSPOSE_TEXT = """
TRANSPOZYCJA MACIERZY (Aᵀ)

CO TO JEST?
Transpozycja polega na zamianie:
wiersze ↔ kolumny

JAK TO ZROBIĆ?
• Element (i, j) przechodzi na (j, i)

PRZYKŁAD:
A = [ 3  -1  4 ]
       [ 2   5  0 ]

Aᵀ = [ 3  2 ]
         [ -1 5 ]
         [ 4  0 ]

UWAGI:
• Każdą macierz da się transponować
• Pomaga przy mnożeniu
"""

DET_TEXT = """
WYZNACZNIK MACIERZY – METODA ROZWINIĘCIA LAPLACE’A

Wyznacznik macierzy kwadratowej można obliczyć rozwijając ją względem dowolnego wiersza lub kolumny.

W tym procesie wykorzystujemy:
• MINI MACIERZE (MINORY) – macierze powstałe po usunięciu wiersza i kolumny danego elementu
• DOPEŁNIENIA ALGEBRAICZNE – znak (-1)^(i+j) pomnożony przez wyznacznik minora
• COFACTOR = DOPEŁNIENIE ALGEBRAICZNE

WZÓR OGÓLNY (rozwinięcie względem wiersza i):
det(A) = Σ aᵢⱼ · (-1)^(i+j) · det(Mᵢⱼ)

gdzie:
• aᵢⱼ – element macierzy w i-tym wierszu i j-tej kolumnie
• Mᵢⱼ – mini macierz powstała po usunięciu i-tego wiersza i j-tej kolumny

================================================
PRZYKŁAD 2x2
================================================
A = [ 3   5 ]
       [ 2  -1 ]


------------------------------------------------
WZÓR NA WYZNACZNIK MACIERZY 2x2
------------------------------------------------
det(A) = a11·a22 − a12·a21

------------------------------------------------
KROK 1: WYZNACZNIK MACIERZY 2x2
------------------------------------------------
det(A) = a11·a22 − a12·a21
det(A) = 3·(-1) − 5·2
det(A) = -3 − 10
det(A) = -13

------------------------------------------------
UWAGI:
• Dla macierzy 2x2 nie trzeba tworzyć dopełnień algebraicznych – to jest najprostsza forma.

================================================
PRZYKŁAD 3x3
================================================
A = [ 3  -1   2 ]
       [ 4   0  -3 ]
       [ -2  5   1 ]

------------------------------------------------
KROK 1: WYBÓR WIERSZA DO ROZWINIĘCIA
------------------------------------------------
Rozwijamy względem pierwszego wiersza (i = 1)
Znaki dopełnień algebraicznych: +  −  +  (wg wzoru (-1)^(i+j))

------------------------------------------------
KROK 2: TWORZENIE MINI MACIERZY
------------------------------------------------
Element a11 = 3
Usuwamy wiersz 1 i kolumnę 1:

[ 0  -3 ]
[ 5   1 ]

det(minor) = 0·1 − (-3)·5 = 0 + 15 = 15
Dopełnienie algebraiczne: (+)·3·15 = 45

--------------------------------
Element a12 = -1
Usuwamy wiersz 1 i kolumnę 2:

[ 4  -3 ]
[ -2  1 ]

det(minor) = 4·1 − (-3)·(-2) = 4 − 6 = -2
Dopełnienie algebraiczne: (-)·(-1)·(-2) = -2

--------------------------------
Element a13 = 2
Usuwamy wiersz 1 i kolumnę 3:

[ 4   0 ]
[ -2  5 ]

det(minor) = 4·5 − 0·(-2) = 20 − 0 = 20
Dopełnienie algebraiczne: (+)·2·20 = 40

------------------------------------------------
KROK 3: SUMOWANIE DOPEŁNIEŃ
------------------------------------------------
det(A) = 45 − 2 + 40
det(A) = 83

------------------------------------------------
UWAGI
------------------------------------------------
• det(A) = 0 → macierz nie ma odwrotności
• Dla macierzy nxn: rozwinięcie można zrobić względem dowolnego wiersza lub kolumny
• Mini macierz = usunięty wiersz i kolumna elementu
• Znaki dopełnień algebraicznych: (+ − + − …) wg wzoru (-1)^(i+j)
• Macierz MUSI być kwadratowa aby obliczyć wyznacznik
"""


INV_TEXT = """
MACIERZ ODWROTNA (A⁻¹) – WYJAŚNIENIE

MACIERZ ODWROTNA TO:
• Taka macierz A⁻¹, że A · A⁻¹ = I (macierz jednostkowa)
• Istnieje tylko wtedy, gdy det(A) ≠ 0

PO CO NAM MACIERZ ODWROTNA?
• Dzięki niej możemy „dzielić” macierze:
  A / B = A · B⁻¹
• Bez macierzy odwrotnej nie możemy odwrócić działania macierzowego (np. A · X = B)

================================================
PRZYKŁAD 1: MACIERZ 2x2
================================================
A = [ 2  3 ]
       [ 1  4 ]

------------------------------------------------
KROK 1: WYZNACZNIK
------------------------------------------------
det(A) = 2·4 − 3·1 = 8 − 3 = 5 ≠ 0
→ det ≠ 0, więc macierz odwrotna istnieje

------------------------------------------------
KROK 2: MACIERZ DOPEŁNIEŃ (COFAKTORY)
------------------------------------------------
• Dla elementów 2x2 cofaktor = minor × znak szachownicy

Liczymy minor każdego elementu:
- c11: usuwamy wiersz 1 i kolumnę 1 → zostaje [4] → det = 4 → znak (+1) → c11 = 4
- c12: usuwamy wiersz 1 i kolumnę 2 → zostaje [1] → det = 1 → znak (-1) → c12 = -1
- c21: usuwamy wiersz 2 i kolumnę 1 → zostaje [3] → det = 3 → znak (-1) → c21 = -3
- c22: usuwamy wiersz 2 i kolumnę 2 → zostaje [2] → det = 2 → znak (+1) → c22 = 2

C = [  4  -1 ]
       [ -3   2 ]

------------------------------------------------
KROK 3: TRANSPONOWANIE (ADJUGATA)
------------------------------------------------
Cᵀ = [ 4  -3 ]
         [ -1  2 ]

------------------------------------------------
KROK 4: PODZIAŁ PRZEZ WYZNACZNIK
------------------------------------------------
A⁻¹ = 1/det(A) · Cᵀ

A⁻¹ = 1/5 · [ 4  -3 ]
                   [ -1  2 ]

A⁻¹ = [ 4/5  -3/5 ]
           [ -1/5  2/5 ]

------------------------------------------------
SPRAWDZENIE
------------------------------------------------
A · A⁻¹ = I

I = [ 1  0 ]
     [ 0  1 ]

------------------------------------------------
BONUS
------------------------------------------------
• Przy macierzach 2x2 można skorzystać z uproszczonego wzoru:

A⁻¹ = 1 / (ad − bc) · [  d   −b ]
                                  [ −c    a ]


================================================
PRZYKŁAD 2: MACIERZ 3x3
================================================
A = [ 2   1  -1 ]
       [ 1   1   0 ]
       [ 3  -1   2 ]

------------------------------------------------
KROK 1: WYZNACZNIK
------------------------------------------------
det(A) = 2·det([1 0; -1 2]) 
             - 1·det([1 0; 3 2]) 
             + (-1)·det([1 1; 3 -1]) 

det([1 0;   -1 2]) = 1*2 - 0*(-1) = 2
det([1 0;    3 2])  = 1*2 - 0*3  = 2
det([1 1;    3 -1]) = 1*(-1) - 1*3 = -4

det(A) = 2*2 - 1*2 + (-1)*(-4) = 4 - 2 + 4 = 6

------------------------------------------------
KROK 2: MACIERZ DOPEŁNIEŃ (COFAKTORY)
------------------------------------------------
Liczymy cofaktory dla każdego elementu A[i][j]:

1) Pierwszy wiersz:
- c11 = det([1 0;   -1 2]) * (+1) = 2
- c12 = det([1 0;    3 2]) * (-1) = -2
- c13 = det([1 1;    3 -1]) * (+1) = -4

2) Drugi wiersz:
- c21 = det([1 -1;   -1 2]) * (-1) = (1*2 - (-1)*(-1)) * (-1) = (2-1)*(-1) = -1
- c22 = det([2 -1;   3 2]) * (+1) = (2*2 - (-1)*3) = 4+3 = 7
- c23 = det([2 1;    3 -1]) * (-1) = (2*(-1) - 1*3) * (-1) = (-2 -3)*(-1) = 5

3) Trzeci wiersz:
- c31 = det([1 -1;   1 0]) * (+1) = (1*0 - (-1)*1) = 1
- c32 = det([2 -1;   1 0]) * (-1) = (2*0 - (-1)*1)*(-1) = -1
- c33 = det([2 1;    1 1]) * (+1) = (2*1 - 1*1) = 1

Macierz cofaktorów C:

C = [  2  -2  -4 ]
       [ -1   7   5 ]
       [  1  -1   1 ]

------------------------------------------------
KROK 3: TRANSPONOWANIE (ADJUGATA)
------------------------------------------------
Cᵀ = [  2  -1   1 ]
         [ -2   7  -1 ]
         [ -4   5   1 ]

------------------------------------------------
KROK 4: PODZIAŁ PRZEZ WYZNACZNIK
------------------------------------------------
A⁻¹ = 1/6 · Cᵀ

A⁻¹ = [  2/6  -1/6   1/6 ]
          [ -2/6   7/6  -1/6 ]
          [ -4/6   5/6   1/6 ]

------------------------------------------------
SPRAWDZENIE
------------------------------------------------
A · A⁻¹ = I

I = [ 1  0  0 ]
     [ 0  1  0 ]
     [ 0  0  1 ]

================================================
PODSUMOWANIE
================================================
1) Cofaktory = minor × znak szachownicy (+/-)
2) Tworzymy macierz C z cofaktorów
3) Transponujemy C → adjugata
4) Dzielimy przez det(A) → macierz odwrotna
5) Sprawdzenie: A · A⁻¹ = I

• Dla 2x2 cofaktory i odwrotna można policzyć bardzo szybko
• Dla 3x3 i większych – cofaktory i adjugata dają systematyczny sposób


"""

DIV_TEXT = """
DZIELENIE MACIERZY

CO TO ZNACZY „DZIELENIE MACIERZY”?
Macierzy NIE DZIELIMY bezpośrednio.
DZIELENIE ZASTĘPUJEMY MNOŻENIEM przez macierz odwrotną.

WZÓR OGÓLNY:
A / B = A · B⁻¹

WARUNKI:
• B musi być macierzą kwadratową
• det(B) ≠ 0 (musi istnieć B⁻¹)
• Kolejność MA znaczenie!

================================================
PRZYKŁAD 1: DZIELENIE MACIERZY 2x2
================================================
DANE:
A = [ 2   1 ]
       [ -1  3 ]

B = [ 1  1 ]
       [ 2  3 ]

------------------------------------------------
KROK 1: WYZNACZNIK I MACIERZ ODWROTNA
------------------------------------------------
det(B) = 1·3 − 1·2 = 1 ≠ 0

B⁻¹ = 1/det(B) · [  3  -1 ]
                            [ -2   1 ]

B⁻¹ = [  3  -1 ]
          [ -2   1 ]

------------------------------------------------
KROK 2: ZAMIANA DZIELENIA NA MNOŻENIE
------------------------------------------------
A / B = A · B⁻¹

------------------------------------------------
KROK 3: MNOŻENIE
------------------------------------------------
A · B⁻¹ =

[ 2·3 + 1·(-2)     2·(-1) + 1·1 ]
[ -1·3 + 3·(-2)   -1·(-1) + 3·1 ]

------------------------------------------------
WYNIK:
------------------------------------------------
[ 4  -1 ]
[ -9  4 ]

================================================
PRZYKŁAD 2: DZIELENIE MACIERZY 3x3
================================================
DANE:
A = [ 1   2   0 ]
       [ -1  3   1 ]
       [ 2   1   1 ]

B = [ 2   1   1 ]
       [ 0   1   2 ]
       [ 1  -1   1 ]

------------------------------------------------
KROK 1: WYZNACZNIK MACIERZY B
(METODA ROZWINIĘCIA LAPLACE’A)
------------------------------------------------
WZÓR OGÓLNY:
det(B) = Σ aᵢⱼ · (-1)^(i+j) · det(Mᵢⱼ)

gdzie:
• Mᵢⱼ — MINI MACIERZ (usuwamy i-ty wiersz i j-tą kolumnę)
• (-1)^(i+j) — znak dopełnienia algebraicznego

Rozwijamy względem PIERWSZEGO WIERSZA (i = 1)

Znaki:
(-1)^(1+1) = +  
(-1)^(1+2) = −  
(-1)^(1+3) = +  

⇒ +  −  +

------------------------------------------------
MINI MACIERZE (MINORY)
------------------------------------------------
Element b11 = 2
Usuwamy wiersz 1 i kolumnę 1:

[ 1   2 ]
[ -1  1 ]

det = 1·1 − 2·(-1) = 3

--------------------------------
Element b12 = 1
Usuwamy wiersz 1 i kolumnę 2:

[ 0   2 ]
[ 1   1 ]

det = 0·1 − 2·1 = -2

--------------------------------
Element b13 = 1
Usuwamy wiersz 1 i kolumnę 3:

[ 0   1 ]
[ 1  -1 ]

det = 0·(-1) − 1·1 = -1

------------------------------------------------
SKŁADAMY WYZNACZNIK:
------------------------------------------------
det(B) =
+ 2·3
− 1·(-2)
+ 1·(-1)

det(B) = 6 + 2 − 1
det(B) = 7 ≠ 0

------------------------------------------------
KROK 2: DOPEŁNIENIA ALGEBRAICZNE
------------------------------------------------
WZÓR:
Cᵢⱼ = (-1)^(i+j) · det(Mᵢⱼ)

Z dopełnień budujemy
MACIERZ DOPEŁNIEŃ ALGEBRAICZNYCH,
a następnie wykonujemy TRANSPPOZYCJĘ (adjugata).

------------------------------------------------
KROK 3: MACIERZ ODWROTNA
------------------------------------------------
B⁻¹ = 1/7 · adj(B)

adj(B) =
[  3  -2   1 ]
[  2   1  -4 ]
[ -1   3   2 ]

B⁻¹ = 
[  3/7  -2/7   1/7 ]
[  2/7   1/7  -4/7 ]
[ -1/7   3/7   2/7 ]


------------------------------------------------
KROK 4: ZAMIANA DZIELENIA NA MNOŻENIE
------------------------------------------------
A / B = A · B⁻¹

------------------------------------------------
KROK 5: MNOŻENIE 3x3
------------------------------------------------
WYNIK:

[ 1    0    -1 ]
[ 2/7  8/7  -11/7 ]
[ 1    0     0 ]

================================================
UWAGI KOŃCOWE
================================================
• Mini macierz: usuwamy wiersz i kolumnę
• (-1)^(i+j) decyduje o znaku
• Dopełnienie algebraiczne ≠ mini macierz
• Dzielenie = mnożenie przez odwrotność
• A / B ≠ B / A
"""





# =========================
# GUI
# =========================

button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

buttons = [
    ("Dodawanie", ADD_TEXT),
    ("Odejmowanie", SUB_TEXT),
    ("Mnożenie", MUL_TEXT),
    ("Transpozycja", TRANSPOSE_TEXT),
    ("Wyznacznik", DET_TEXT),
    ("Macierz odwrotna", INV_TEXT),
    ("Dzielenie", DIV_TEXT),
]

for name, text in buttons:
    ttk.Button(
        button_frame,
        text=name,
        width=24,
        command=lambda n=name, t=text: show_text(n, t)
    ).pack(pady=4)

content_frame = tk.Frame(root)
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

text_title = tk.Label(
    content_frame,
    text="Wybierz operację",
    font=("Arial", 16, "bold")
)
text_title.pack(anchor="w")

text_box = tk.Text(
    content_frame,
    wrap=tk.WORD,
    font=("Arial", 12)
)
text_box.pack(fill=tk.BOTH, expand=True)
text_box.config(state="disabled")

root.mainloop()
