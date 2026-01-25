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

        self.A = [[3, 1], [3, -2]]
        self.B = [[2, 1], [1, 1]]

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

        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ("A + B", self.add),
            ("A - B", self.sub),
            ("A · B", self.mul),
            ("A · B⁻¹", self.div_ab),
            ("B⁻¹ · A", self.div_ba),
            ("Transpozycja A", lambda: self.transpose("A")),
            ("Transpozycja B", lambda: self.transpose("B")),
            ("Losuj nowe macierze", self.random_matrices),
            ("Wyjście", self.root.quit)
        ]

        for i, (txt, cmd) in enumerate(buttons):
            tk.Button(
                frame,
                text=txt,
                width=22,
                height=2,
                command=cmd
            ).grid(row=i // 3, column=i % 3, padx=6, pady=6)

    # ================= DISPLAY =================

    def refresh(self, result_text=""):
        self.display.config(state="normal")
        self.display.delete(1.0, tk.END)

        self.display.insert(tk.END, "Macierz A:\n")
        self.display.insert(tk.END, self.format(self.A))
        self.display.insert(tk.END, "\nMacierz B:\n")
        self.display.insert(tk.END, self.format(self.B))

        if result_text:
            self.display.insert(tk.END, "\n" + "-" * 50 + "\n")
            self.display.insert(tk.END, result_text)

        self.display.config(state="disabled")

    def format(self, M):
        return "\n".join(
            " ".join(f"{v:8.2f}" for v in row) for row in M
        ) + "\n"

    # ================= OPERATIONS =================

    def add(self):
        if not functions.can_add(self.A, self.B):
            self.error("Nie można dodać macierzy (różne wymiary).")
            return

        result = [
            [self.A[i][j] + self.B[i][j] for j in range(len(self.A[0]))]
            for i in range(len(self.A))
        ]
        self.refresh("Suma A + B:\n" + self.format(result))

    def sub(self):
        if not functions.can_add(self.A, self.B):
            self.error("Nie można odjąć macierzy (różne wymiary).")
            return

        result = [
            [self.A[i][j] - self.B[i][j] for j in range(len(self.A[0]))]
            for i in range(len(self.A))
        ]
        self.refresh("Różnica A - B:\n" + self.format(result))

    def mul(self):
        if not functions.can_multiply(self.A, self.B):
            self.error("Nie można mnożyć macierzy (złe wymiary).")
            return

        result = self.multiply(self.A, self.B)
        self.refresh("Iloczyn A · B:\n" + self.format(result))

    # ================= DZIELENIE (POPRAWIONE) =================

    def div_ab(self):
        self.divide("A · B⁻¹", reverse=False)

    def div_ba(self):
        self.divide("B⁻¹ · A", reverse=True)

    def divide(self, label, reverse=False):
        # ZAWSZE odwracamy tylko macierz B
        invB = functions.inverse_matrix(self.B)
        if invB is None:
            self.error("Macierz B jest nieodwracalna.")
            return

        if reverse:
            left, right = invB, self.A
        else:
            left, right = self.A, invB

        if not functions.can_multiply(left, right):
            self.error("Nieprawidłowe wymiary.")
            return

        result = self.multiply(left, right)
        self.refresh(f"Wynik {label}:\n" + self.format(result))

    # ================= POMOCNICZE =================

    def multiply(self, A, B):
        return [
            [
                round(sum(A[i][k] * B[k][j] for k in range(len(B))), 2)
                for j in range(len(B[0]))
            ]
            for i in range(len(A))
        ]

    def transpose(self, which):
        if which == "A":
            result = functions.transpose_matrix(self.A)
            self.refresh("Transpozycja A:\n" + self.format(result))
        else:
            result = functions.transpose_matrix(self.B)
            self.refresh("Transpozycja B:\n" + self.format(result))

    def random_matrices(self):
        size = random.choice([2, 3])
        self.A = [[random.randint(-5, 5) for _ in range(size)] for _ in range(size)]
        self.B = [[random.randint(-5, 5) for _ in range(size)] for _ in range(size)]
        self.refresh("Wylosowano nowe macierze.")

    def error(self, msg):
        messagebox.showerror("Błąd", msg)


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixGUI(root)
    root.mainloop()
