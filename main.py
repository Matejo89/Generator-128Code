import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter
import os

# Funkcja do generowania kodu kreskowego Code 128 i wyświetlania go w aplikacji
def generuj_kod_kreskowy():
    dane_wejsciowe = entry.get()

    if len(dane_wejsciowe) == 0:
        messagebox.showerror("Błąd", "Wpisz ciąg znaków.")
        return

    # Generowanie kodu kreskowego Code 128
    code128 = barcode.get('code128', dane_wejsciowe, writer=ImageWriter())
    filename = code128.save('code128_barcode')

    # Wyświetlenie kodu kreskowego w aplikacji
    image = Image.open(f"{filename}")
    image = image.resize((300, 150))  # Zmniejszenie rozmiaru obrazu do wyświetlenia
    photo = ImageTk.PhotoImage(image)
    barcode_label.config(image=photo)
    barcode_label.image = photo  # Zachowanie referencji do obrazka

# Funkcja do drukowania kodu kreskowego
def drukuj_kod_kreskowy():
    filename = "code128_barcode.png"
    if not os.path.exists(filename):
        messagebox.showerror("Błąd", "Brak kodu kreskowego do wydruku. Wygeneruj kod przed drukowaniem.")
        return

    image = Image.open(filename)
    image.show()  # To otwiera obraz, drukowanie można zaimplementować według konfiguracji drukarki

# Tworzenie okna aplikacji
root = tk.Tk()
root.title("Generator kodów")
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "favicon.ico")
root.iconbitmap(icon_path)
root.geometry("400x600")
root.resizable(0, 0)

# Funkcja dodająca logo
def add_logo():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "Naglak.png")
        logo_img = Image.open(icon_path)  # Podaj ścieżkę do pliku z logiem
        logo_img = logo_img.resize((250, 100))  # Zmiana rozmiaru loga
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(root, image=logo_photo)
        logo_label.image = logo_photo  # Referencja do obrazu (aby go nie usunęło)
        logo_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się wczytać loga: {e}")

# Wywołanie funkcji dodającej logo
add_logo()

# Etykieta i pole tekstowe do wprowadzania ciągu znaków
tk.Label(root, text="Wpisz ciąg znaków").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Przycisk do generowania kodu kreskowego
generuj_button = tk.Button(root, text="Generuj kod kreskowy", command=generuj_kod_kreskowy, font=("Arial", 12))
generuj_button.pack(pady=10)

# Przycisk do drukowania kodu kreskowego
drukuj_button = tk.Button(root, text="Drukuj kod kreskowy", command=drukuj_kod_kreskowy, font=("Arial", 12))
drukuj_button.pack(pady=10)

# Miejsce na wyświetlenie kodu kreskowego
barcode_label = tk.Label(root)
barcode_label.pack(pady=20)

# Pasek stanu
pasek_stanu = tk.Label(root, text="By Dawid Orchowski", bd=1, relief=tk.SUNKEN, anchor=tk.W)
pasek_stanu.pack(side=tk.BOTTOM, fill=tk.X)

# Uruchomienie głównej pętli aplikacji
root.mainloop()
