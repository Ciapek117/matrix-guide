import tkinter as tk
from tkinter import messagebox
import random
import functions


class MatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix dla opornych 🧮")
        self.root.geometry("740x580")
        self.root.resizable(False, False)

        self.matrix_a = [[3, 1], [3, -2]]
        self.matrix_b = [[2, 1], [1, 1]]

        self.build_ui()
        self.refresh()

    # ================= UI =================

    def build_ui(self):
        tk.Label(
            self.root,
            text="Matrix dla opornych",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        self.display = tk.Text(
            self.root,
            height=16,
            width=85,
            font=("Consolas", 11),
            bg="#f7f7f7",
            state="disabled"
        )
        self.display.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ("A + B", self.add_matrices),
            ("A - B", self.subtract_matrices),
            ("A · B", self.multiply_matrices),
            ("A · B⁻¹", self.divide_a_by_b),
            ("B⁻¹ · A", self.divide_b_by_a),
            ("Transpozycja A", lambda: self.transpose_matrix("A")),
            ("Transpozycja B", lambda: self.transpose_matrix("B")),
            ("Edytuj macierz A", lambda: self.edit_matrix("A")),
            ("Edytuj macierz B", lambda: self.edit_matrix("B")),
            ("Losuj nowe macierze", self.generate_random_matrices),
            ("Wyjście", self.root.quit)
        ]

        for i, (label, command) in enumerate(buttons):
            tk.Button(
                button_frame,
                text=label,
                width=22,
                height=2,
                command=command
            ).grid(row=i // 3, column=i % 3, padx=6, pady=6)

    # ================= DISPLAY =================

    def refresh(self, result_text=""):
        self.display.config(state="normal")
        self.display.delete(1.0, tk.END)

        self.display.insert(tk.END, "Macierz A:\n")
        self.display.insert(tk.END, self.format_matrix(self.matrix_a))
        self.display.insert(tk.END, "\nMacierz B:\n")
        self.display.insert(tk.END, self.format_matrix(self.matrix_b))

        if result_text:
            self.display.insert(tk.END, "\n" + "-" * 50 + "\n")
            self.display.insert(tk.END, result_text)

        self.display.config(state="disabled")

    def format_matrix(self, matrix):
        return "\n".join(
            " ".join(f"{value:8.2f}" for value in row) for row in matrix
        ) + "\n"

    # ================= OPERATIONS =================

    def add_matrices(self):
        if not functions.can_add(self.matrix_a, self.matrix_b):
            self.show_error("Nie można dodać macierzy (różne wymiary).")
            return

        result = [
            [self.matrix_a[i][j] + self.matrix_b[i][j] for j in range(len(self.matrix_a[0]))]
            for i in range(len(self.matrix_a))
        ]
        self.refresh("Suma A + B:\n" + self.format_matrix(result))

    def subtract_matrices(self):
        if not functions.can_add(self.matrix_a, self.matrix_b):
            self.show_error("Nie można odjąć macierzy (różne wymiary).")
            return

        result = [
            [self.matrix_a[i][j] - self.matrix_b[i][j] for j in range(len(self.matrix_a[0]))]
            for i in range(len(self.matrix_a))
        ]
        self.refresh("Różnica A - B:\n" + self.format_matrix(result))

    def multiply_matrices(self):
        if not functions.can_multiply(self.matrix_a, self.matrix_b):
            self.show_error("Nie można mnożyć macierzy (złe wymiary).")
            return

        result = self.perform_multiplication(self.matrix_a, self.matrix_b)
        self.refresh("Iloczyn A · B:\n" + self.format_matrix(result))

    def divide_a_by_b(self):
        self.perform_division("A · B⁻¹", reverse=False)

    def divide_b_by_a(self):
        self.perform_division("B⁻¹ · A", reverse=True)

    def perform_division(self, label, reverse=False):
        inverse_b = functions.inverse_matrix(self.matrix_b)
        if inverse_b is None:
            self.show_error("Macierz B jest nieodwracalna.")
            return

        left_matrix, right_matrix = (inverse_b, self.matrix_a) if reverse else (self.matrix_a, inverse_b)

        if not functions.can_multiply(left_matrix, right_matrix):
            self.show_error("Nieprawidłowe wymiary.")
            return

        result = self.perform_multiplication(left_matrix, right_matrix)
        self.refresh(f"Wynik {label}:\n" + self.format_matrix(result))

    # ================= POMOCNICZE =================

    def perform_multiplication(self, matrix_a, matrix_b):
        return [
            [
                round(sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b))), 2)
                for j in range(len(matrix_b[0]))
            ]
            for i in range(len(matrix_a))
        ]

    def transpose_matrix(self, matrix_name):
        if matrix_name == "A":
            result = functions.transpose_matrix(self.matrix_a)
            self.refresh("Transpozycja A:\n" + self.format_matrix(result))
        else:
            result = functions.transpose_matrix(self.matrix_b)
            self.refresh("Transpozycja B:\n" + self.format_matrix(result))

    # ================= EDYCJA MACIERZY =================

    def center_window(self, window, width, height):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    
    def edit_matrix(self, matrix_name):
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

                self.refresh(f"Zaktualizowano macierz {matrix_name}.")
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
        size = random.choice([2, 3])
        self.matrix_a = [[random.randint(-5, 5) for _ in range(size)] for _ in range(size)]
        self.matrix_b = [[random.randint(-5, 5) for _ in range(size)] for _ in range(size)]
        self.refresh("Wylosowano nowe macierze.")

    def show_error(self, message):
        messagebox.showerror("Błąd", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixGUI(root)
    root.mainloop()
