import tkinter as tk
from tkinter import messagebox

def klik(t):
    unos_polje.insert(tk.END, t)

def izracunaj():
    try:
        izraz = unos_polje.get()
        rezultat = eval(izraz)
        unos_polje.delete(0, tk.END)
        unos_polje.insert(tk.END, str(rezultat))
    except Exception as e:
        messagebox.showerror("Greška", "Nevažeći izraz")

def obrisi():
    unos_polje.delete(0, tk.END)

# Prozor
prozor = tk.Tk()
prozor.title("Napredni Kalkulator")

# Unos
unos_polje = tk.Entry(prozor, width=30, font=("Arial", 16), borderwidth=3, relief="sunken", justify='right')
unos_polje.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Dugmad
dugmad = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '(', ')', '=', 
]

red = 1
kolona = 0

for dugme in dugmad:
    if dugme == "=":
        b = tk.Button(prozor, text=dugme, width=10, height=2, command=izracunaj)
        b.grid(row=red, column=kolona, columnspan=2, padx=5, pady=5)
        kolona += 2
    elif dugme == "C":
        b = tk.Button(prozor, text=dugme, width=5, height=2, command=obrisi)
        b.grid(row=red, column=kolona, padx=5, pady=5)
        kolona += 1
    else:
        b = tk.Button(prozor, text=dugme, width=5, height=2, command=lambda t=dugme: klik(t))
        b.grid(row=red, column=kolona, padx=5, pady=5)
        kolona += 1

    if kolona > 3:
        kolona = 0
        red += 1

prozor.mainloop()
