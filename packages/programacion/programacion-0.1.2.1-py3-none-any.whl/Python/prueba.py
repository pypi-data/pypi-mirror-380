import tkinter as tk
from tkinter import simpledialog, messagebox
import math
from typing import Any

class CalculadoraColores:
    def __init__(self, root: tk.Tk) -> None:
        """Función __init__(self, root)"""
        self.root: tk.Tk = root
        self.root.title("Calculadora")
        self.root.geometry("575x795")

        # Display
        self.entry: tk.Entry = tk.Entry(root, font=("Arial", 20), borderwidth=2,
                                        relief="sunken", justify="right")
        self.entry.pack(fill="both", padx=10, pady=10, ipady=10)

        # Frame principal para botones
        self.frame: tk.Frame = tk.Frame(root)
        self.frame.pack()

        # Memoria y operación
        self.operacion: str = ""
        self.memoria: list[float] = []

        # Crear bloques de botones
        self.crear_bloque("Básicas",
                          ["7","8","9","/","4","5","6","*",
                           "1","2","3","-","0",".","=","+"],
                          "#add8e6")
        self.crear_bloque("Científicas",
                          ["√","^","x!","π","e","log","ln",
                           "rad→deg","deg→rad","mod","media"],
                          "#90ee90")
        self.crear_bloque("Trigonométricas",
                          ["sin","cos","tan","AC"],
                          "#ffb6c1")

    def crear_bloque(self, nombre: str, botones: list[str], color: str) -> None:
        """Función crear_bloque(self, nombre, botones, color)"""
        frame_bloque: tk.LabelFrame = tk.LabelFrame(
            self.frame, text=nombre, padx=5, pady=5, bg=color, font=("Arial", 12)
        )
        frame_bloque.pack(padx=5, pady=5, fill="both")

        fila: int = 0
        col: int = 0
        for b in botones:
            btn: tk.Button = tk.Button(frame_bloque, text=b, width=6, height=2,
                                       font=("Arial", 14),
                                       command=lambda t=b: self.click(t),
                                       bg="white")
            btn.grid(row=fila, column=col, padx=3, pady=3)
            col += 1
            if col > 3:
                col = 0
                fila += 1

    def click(self, texto: str) -> None:
        """Función click(self, texto)"""
        try:
            if texto in '0123456789.':
                self.entry.insert(tk.END, texto)
            elif texto in '+-*/^':
                self.operacion = texto
                self.memoria.append(float(self.entry.get()))
                self.entry.delete(0, tk.END)
            elif texto == '=':
                self.memoria.append(float(self.entry.get()))
                self.calcular()
            elif texto == 'AC':
                self.entry.delete(0, tk.END)
                self.operacion = ""
                self.memoria = []
            elif texto == '√':
                x: float = float(self.entry.get())
                if x < 0:
                    raise ValueError("Raíz de número negativo")
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.sqrt(x))
            elif texto == 'x!':
                x = float(self.entry.get())
                if x < 0 or not x.is_integer():
                    raise ValueError("Factorial solo enteros ≥0")
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.factorial(int(x)))
            elif texto == 'π':
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.pi)
            elif texto == 'e':
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.e)
            elif texto == 'log':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.log10(x))
            elif texto == 'ln':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.log(x))
            elif texto == 'sin':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.sin(x))
            elif texto == 'cos':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.cos(x))
            elif texto == 'tan':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.tan(x))
            elif texto == 'rad→deg':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.degrees(x))
            elif texto == 'deg→rad':
                x = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, math.radians(x))
            elif texto == 'mod':
                self.operacion = 'mod'
                self.memoria.append(float(self.entry.get()))
                self.entry.delete(0, tk.END)
            elif texto == 'media':
                nums: str | None = simpledialog.askstring("Media", "Introduce números separados por comas:")
                if nums:
                    lista: list[float] = [float(n) for n in nums.split(",")]
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, sum(lista) / len(lista))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular(self) -> None:
        """Función calcular(self)"""
        try:
            a: float = self.memoria.pop(0)
            b: float = self.memoria.pop(0)
            if self.operacion == '+':
                res: float = a + b
            elif self.operacion == '-':
                res = a - b
            elif self.operacion == '*':
                res = a * b
            elif self.operacion == '/':
                if b == 0:
                    raise ValueError("División entre 0")
                res = a / b
            elif self.operacion == '^':
                res = a ** b
            elif self.operacion == 'mod':
                res = a % b
            else:
                res = 0.0
            self.entry.delete(0, tk.END)
            self.entry.insert(0, res)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    calc = CalculadoraColores(root)
    root.mainloop()
