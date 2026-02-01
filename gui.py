import tkinter as tk
from tkinter import messagebox
import random
import functions


class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix dla opornych 🧮")
        self.root.geometry("740x580")
        self.root.resizable(False, False)

        self.matrix_a = [[3, 1], [3, -2]]
        self.matrix_b = [[2, 1], [1, 1]]

        self.initialize_ui()
        self.center_window(self.root, 1200, 800)
        self.update_display()

    # ================= UI =================

    def center_window(self, window, width, height):
        """Centruje okno na ekranie."""
        window.update_idletasks()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def initialize_ui(self):
        """Inicjalizuje komponenty interfejsu użytkownika."""
        tk.Label(
            self.root,
            text="Matrix dla opornych",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        self.display_area = tk.Text(
            self.root,
            height=16,
            width=85,
            font=("Consolas", 11),
            bg="#f7f7f7",
            state="disabled"
        )
        self.display_area.pack(pady=10)

        # ================= SEKCJE =================

        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=5)

        left_panel = tk.Frame(main_frame)
        left_panel.pack(side=tk.LEFT, padx=10)

        right_panel = tk.Frame(main_frame)
        right_panel.pack(side=tk.LEFT, padx=10)

        def create_section(parent, title):
            """Tworzy sekcję z etykietą."""
            frame = tk.LabelFrame(
                parent,
                text=title,
                font=("Arial", 10, "bold"),
                padx=10,
                pady=10
            )
            frame.pack_propagate(False)
            return frame

        # ---- Operacje podstawowe (LEWY PANEL) ----
        basic_operations = create_section(left_panel, "Operacje na macierzach")
        basic_operations.pack(pady=(0, 10))

        tk.Button(basic_operations, text="A + B", width=22, command=self.add_matrices).grid(row=0, column=0, padx=6, pady=4)
        tk.Button(basic_operations, text="A - B", width=22, command=self.subtract_matrices).grid(row=0, column=1, padx=6, pady=4)
        tk.Button(basic_operations, text="A · B", width=22, command=self.multiply_matrices).grid(row=1, column=0, padx=6, pady=4)
        tk.Button(basic_operations, text="A · B⁻¹", width=22, command=self.divide_a_by_b).grid(row=1, column=1, padx=6, pady=4)
        tk.Button(basic_operations, text="B⁻¹ · A", width=46, command=self.divide_b_by_a).grid(row=2, column=0, columnspan=2, pady=4)

        # ---- Benchmarki ----
        benchmark_section = create_section(left_panel, "Benchmark")
        benchmark_section.pack()

        tk.Button(
            benchmark_section,
            text="A + B",
            width=22,
            command=lambda: self.run_benchmark("add", "Suma A + B")
        ).grid(row=0, column=0, padx=6, pady=4)

        tk.Button(
            benchmark_section,
            text="A - B",
            width=22,
            command=lambda: self.run_benchmark("sub", "Różnica A - B")
        ).grid(row=0, column=1, padx=6, pady=4)

        tk.Button(
            benchmark_section,
            text="A · B",
            width=22,
            command=lambda: self.run_benchmark("mul", "Iloczyn A · B")
        ).grid(row=1, column=0, padx=6, pady=4)

        tk.Button(
            benchmark_section,
            text="A · B⁻¹",
            width=22,
            command=lambda: self.run_benchmark("a_div_b", "A · B⁻¹")
        ).grid(row=1, column=1, padx=6, pady=4)

        tk.Button(
            benchmark_section,
            text="B⁻¹ · A",
            width=46,
            command=lambda: self.run_benchmark("b_div_a", "B⁻¹ · A")
        ).grid(row=2, column=0, columnspan=2, pady=4)

        # ---- Operacje zaawansowane (PRAWY PANEL) ----
        advanced_operations = create_section(right_panel, "Operacje specjalne")
        advanced_operations.pack(anchor="n")

        tk.Button(advanced_operations, text="Transpozycja A", width=22, command=lambda: self.transpose_matrix("A")).grid(row=0, column=0, padx=6, pady=4)
        tk.Button(advanced_operations, text="Transpozycja B", width=22, command=lambda: self.transpose_matrix("B")).grid(row=0, column=1, padx=6, pady=4)

        tk.Button(advanced_operations, text="Wyznacznik A", width=22, command=lambda: self.show_determinant("A")).grid(row=1, column=0, padx=6, pady=4)
        tk.Button(advanced_operations, text="Wyznacznik B", width=22, command=lambda: self.show_determinant("B")).grid(row=1, column=1, padx=6, pady=4)

        tk.Button(advanced_operations, text="Macierz odwrotna A", width=22, command=lambda: self.show_inverse("A")).grid(row=2, column=0, padx=6, pady=4)
        tk.Button(advanced_operations, text="Macierz odwrotna B", width=22, command=lambda: self.show_inverse("B")).grid(row=2, column=1, padx=6, pady=4)

        edit_section = tk.LabelFrame(
            right_panel,
            text="Edycja",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10
        )
        edit_section.pack(pady=(20, 0))

        tk.Button(edit_section, text="Edytuj macierz A", width=22, command=lambda: self.edit_matrix("A")).grid(row=0, column=0, padx=6, pady=4)
        tk.Button(edit_section, text="Edytuj macierz B", width=22, command=lambda: self.edit_matrix("B")).grid(row=0, column=1, padx=6, pady=4)
        tk.Button(edit_section, text="Losuj nowe macierze", width=46, command=self.generate_random_matrices).grid(row=1, column=0, columnspan=2, pady=4)

        # ---- Przycisk wyjścia ----
        tk.Button(
            self.root,
            text="Wyjście",
            width=50,
            height=2,
            bg="#e74c3c",
            fg="white",
            command=self.root.quit
        ).pack(pady=10)

    # ================= WYŚWIETLANIE =================

    def update_display(self, result_text=""):
        """Aktualizuje obszar wyświetlania macierzy i opcjonalnego wyniku."""
        self.display_area.config(state="normal")
        self.display_area.delete(1.0, tk.END)

        self.display_area.insert(tk.END, "Macierz A:\n")
        self.display_area.insert(tk.END, self.format_matrix(self.matrix_a))
        self.display_area.insert(tk.END, "\nMacierz B:\n")
        self.display_area.insert(tk.END, self.format_matrix(self.matrix_b))

        if result_text:
            self.display_area.insert(tk.END, "\n" + "-" * 50 + "\n")
            self.display_area.insert(tk.END, result_text)

        self.display_area.config(state="disabled")

    def format_matrix(self, matrix):
        """Formatuje macierz jako tekst do wyświetlenia."""
        return "\n".join(
            " ".join(f"{value:8.2f}" for value in row) for row in matrix
        ) + "\n"

    # ================= OPERACJE =================

    def add_matrices(self):
        """Dodaje dwie macierze i aktualizuje wyświetlacz wynikiem."""
        if not functions.can_add(self.matrix_a, self.matrix_b):
            self.show_error("Nie można dodać macierzy (różne wymiary).")
            return

        result = [
            [self.matrix_a[i][j] + self.matrix_b[i][j] for j in range(len(self.matrix_a[0]))]
            for i in range(len(self.matrix_a))
        ]
        self.update_display("Suma A + B:\n" + self.format_matrix(result))

    def subtract_matrices(self):
        """Odejmuje macierz B od A i aktualizuje wyświetlacz wynikiem."""
        if not functions.can_add(self.matrix_a, self.matrix_b):
            self.show_error("Nie można odjąć macierzy (różne wymiary).")
            return

        result = [
            [self.matrix_a[i][j] - self.matrix_b[i][j] for j in range(len(self.matrix_a[0]))]
            for i in range(len(self.matrix_a))
        ]
        self.update_display("Różnica A - B:\n" + self.format_matrix(result))

    def multiply_matrices(self):
        """Mnoży dwie macierze i aktualizuje wyświetlacz wynikiem."""
        if not functions.can_multiply(self.matrix_a, self.matrix_b):
            self.show_error("Nie można mnożyć macierzy (złe wymiary).")
            return

        result = self.perform_multiplication(self.matrix_a, self.matrix_b)
        self.update_display("Iloczyn A · B:\n" + self.format_matrix(result))

    def divide_a_by_b(self):
        """Dzieli macierz A przez odwrotność B i aktualizuje wyświetlacz wynikiem."""
        self.perform_division("A · B⁻¹", reverse=False)

    def divide_b_by_a(self):
        """Dzieli macierz B przez odwrotność A i aktualizuje wyświetlacz wynikiem."""
        self.perform_division("B⁻¹ · A", reverse=True)

    def perform_division(self, label, reverse=False):
        """Wykonuje dzielenie macierzy z użyciem odwrotności i aktualizuje wyświetlacz wynikiem."""
        inverse_b = functions.inverse_matrix(self.matrix_b)
        if inverse_b is None:
            self.show_error("Macierz B jest nieodwracalna.")
            return

        left_matrix, right_matrix = (inverse_b, self.matrix_a) if reverse else (self.matrix_a, inverse_b)

        if not functions.can_multiply(left_matrix, right_matrix):
            self.show_error("Nieprawidłowe wymiary.")
            return

        result = self.perform_multiplication(left_matrix, right_matrix)
        self.update_display(f"Wynik {label}:\n" + self.format_matrix(result))

    def show_determinant(self, matrix_name):
        """Oblicza i wyświetla wyznacznik podanej macierzy."""
        matrix = self.matrix_a if matrix_name == "A" else self.matrix_b

        det = functions.determinant(matrix)
        if det is None:
            self.show_error("Nie można obliczyć wyznacznika (macierz nie jest kwadratowa).")
            return

        self.update_display(f"Wyznacznik macierzy {matrix_name}:\n\ndet({matrix_name}) = {round(det, 2)}")
    

    def show_inverse(self, matrix_name):
        """Oblicza i wyświetla odwrotność podanej macierzy."""
        matrix = self.matrix_a if matrix_name == "A" else self.matrix_b

        inverse = functions.inverse_matrix(matrix)
        if inverse is None:
            self.show_error(f"Macierz {matrix_name} jest nieodwracalna lub nie jest kwadratowa.")
            return

        self.update_display(f"Macierz odwrotna {matrix_name}:\n" + self.format_matrix(inverse))
    
    def run_benchmark(self, operation, label):
        """Uruchamia benchmark dla podanej operacji na macierzach i wyświetla wyniki."""
        data = functions.benchmark(operation, self.matrix_a, self.matrix_b)

        if data is None:
            self.show_error("Nie można wykonać operacji (macierz nieodwracalna).")
            return

        speedup = (
            data["manual_time"] / data["numpy_time"]
            if data["numpy_time"] > 0 else float("inf")
        )

        text = (
            f"{label} (benchmark):\n\n"
            + self.format_matrix(data["manual_result"])
            + "\nCzas ręczny : {:.8f} s"
            + "\nCzas numpy  : {:.8f} s"
            + "\nPrzyspieszenie: {:.2f}x 🚀"
        ).format(
            data["manual_time"],
            data["numpy_time"],
            speedup
        )

        self.update_display(text)



    # ================= POMOCNICZE =================

    def perform_multiplication(self, matrix_a, matrix_b):
        """Wykonuje mnożenie macierzy i zwraca wynik."""
        return [
            [
                round(sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b))), 2)
                for j in range(len(matrix_b[0]))
            ]
            for i in range(len(matrix_a))
        ]

    def transpose_matrix(self, matrix_name):
        """Transponuje podaną macierz i aktualizuje wyświetlacz wynikiem."""
        if matrix_name == "A":
            result = functions.transpose_matrix(self.matrix_a)
            self.update_display("Transpozycja A:\n" + self.format_matrix(result))
        else:
            result = functions.transpose_matrix(self.matrix_b)
            self.update_display("Transpozycja B:\n" + self.format_matrix(result))

    # ================= EDYCJA MACIERZY =================
    
    def edit_matrix(self, matrix_name):
        """Otwiera okno do edycji wartości podanej macierzy."""
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edycja macierzy {matrix_name}")
        self.center_window(edit_window, 600, 550)
        edit_window.resizable(False, False)

        tk.Label(
            edit_window,
            text=f"Edycja macierzy {matrix_name}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        config_frame = tk.Frame(edit_window)
        config_frame.pack(pady=10)

        tk.Label(config_frame, text="Liczba wierszy:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(config_frame, text="Liczba kolumn:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

        rows_entry = tk.Entry(config_frame, width=6)
        cols_entry = tk.Entry(config_frame, width=6)
        rows_entry.grid(row=0, column=1, pady=5)
        cols_entry.grid(row=1, column=1, pady=5)


        def create_inputs():
            try:
                rows = int(rows_entry.get())
                cols = int(cols_entry.get())
                if rows <= 0 or cols <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Błąd", "Podaj poprawne wymiary.")
                return

            matrix_frame = tk.LabelFrame(
                edit_window,
                text="Wpisz wartości macierzy",
                padx=10,
                pady=10
            )

            matrix_frame.pack(pady=15)

            entries = []

            for i in range(rows):
                row_entries = []
                for j in range(cols):
                    entry = tk.Entry(matrix_frame, width=6, justify="center")
                    entry.grid(row=i, column=j, padx=4, pady=4)
                    row_entries.append(entry)
                entries.append(row_entries)

            

            def save_matrix():
                try:
                    matrix = [
                        [float(entries[i][j].get()) for j in range(cols)]
                        for i in range(rows)
                    ]
                except ValueError:
                    messagebox.showerror("Błąd", "Wszystkie pola muszą być liczbami.")
                    return

                if matrix_name == "A":
                    self.matrix_a = matrix
                else:
                    self.matrix_b = matrix

                self.update_display(f"Zaktualizowano macierz {matrix_name}.")
                edit_window.destroy()

            tk.Button(edit_window,
                text="Zapisz macierz",
                width=20,
                height=2,
                command=save_matrix
            ).pack(pady=10)

        tk.Button(
            config_frame,
            text="Dalej",
            width=15,
            command=create_inputs
        ).grid(row=2, column=0, columnspan=2, pady=10)
    
    def generate_random_matrices(self):
        """Generuje losowe macierze A i B oraz aktualizuje wyświetlacz."""
        size = random.choice([2, 3])
        self.matrix_a = [[random.randint(-5, 5) for _ in range(size)] for _ in range(size)]
        self.matrix_b = [[random.randint(-5, 5) for _ in range(size)] for _ in range(size)]
        self.update_display("Wylosowano nowe macierze.")

    def show_error(self, message):
        """Wyświetla okno komunikatu o błędzie."""
        messagebox.showerror("Błąd", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()
