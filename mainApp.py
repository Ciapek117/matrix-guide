# main_gui.py
# Matrix Guide - menu startowe w Tkinter
# By: Alan Gładyś, Martyna Hedeszyńska

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def run_gui():
    try:
        subprocess.run([sys.executable, "gui.py"])
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się uruchomić gui.py:\n{e}")

def run_tutorial():
    try:
        subprocess.run([sys.executable, "matrixTutorial.py"])
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się uruchomić matrixTutorial.py:\n{e}")

def quit_app():
    root.destroy()

# =========================
# Tworzenie okna startowego
# =========================

root = tk.Tk()
root.title("Matrix Guide - Menu Startowe 🧮")
root.geometry("700x700")
root.resizable(False, False)

tk.Label(
    root,
    text="Matrix Guide",
    font=("Arial", 20, "bold"),
    pady=20
).pack()

tk.Label(
    root,
    text="Wybierz opcję:",
    font=("Arial", 14)
).pack(pady=10)

btn_gui = tk.Button(
    root,
    text="Aplikacja GUI",
    font=("Arial", 12),
    width=20,
    height=2,
    command=run_gui
)
btn_gui.pack(pady=5)

btn_tutorial = tk.Button(
    root,
    text="Samouczek",
    font=("Arial", 12),
    width=20,
    height=2,
    command=run_tutorial
)
btn_tutorial.pack(pady=5)

btn_exit = tk.Button(
    root,
    text="Wyjście",
    font=("Arial", 12),
    width=20,
    height=2,
    command=quit_app
)
btn_exit.pack(pady=20)

root.mainloop()
