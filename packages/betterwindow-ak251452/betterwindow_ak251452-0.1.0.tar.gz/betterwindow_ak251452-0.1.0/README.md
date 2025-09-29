# 🪟 BetterWindow

**BetterWindow** to nowoczesna biblioteka Python ułatwiająca tworzenie niestandardowych okien w tkinter.  
Dodaje własny pasek tytułu, przyciski minimalizacji i zamknięcia, a także przyciski z efektami hover.

## ✨ Funkcje

- 🎨 **CustomTk** – główne okno aplikacji z własnym paskiem tytułu
- 🗨️ **CustomToplevel** – dodatkowe okna dialogowe (modalne i niemodalne)
- 🖱️ **Przeciąganie okien** – intuicyjne przesuwanie okien poprzez pasek tytułu
- ⚡ **CButton** – przyciski z efektami hover i animacjami wciśnięcia
- 🖥️ **Kompatybilność wieloplatformowa** – działa na Windows, macOS, Linux
- 🎯 **Łatwa integracja** – prosta wymiana standardowych komponentów tkinter

## 📦 Instalacja

```bash
pip install betterwindow
```

## 🚀 Szybki start

```python
from betterwindow import CustomTk, CButton

# Utwórz główne okno aplikacji
app = CustomTk()
app.set_title("Moja aplikacja")

# Dodaj przycisk z efektami hover
btn = CButton(app.window, text="Kliknij mnie!", command=lambda: print("Kliknięto!"))
btn.pack(pady=20)

# Uruchom aplikację
app.mainloop()
```

## 📋 Pełny przykład

```python
from betterwindow import CustomTk, CButton, CustomToplevel
import tkinter as tk

class MojaAplikacja:
    def __init__(self):
        # Główne okno
        self.app = CustomTk()
        self.app.set_title("Przykład BetterWindow")
        
        # Zawartość okna
        label = tk.Label(self.app.window, text="Witaj w BetterWindow!", 
                        bg=self.app.DGRAY, fg='lightgray', 
                        font=('Arial', 14))
        label.pack(pady=20)
        
        # Przyciski
        btn1 = CButton(self.app.window, text="Pokaż dialog", 
                      command=self.pokaz_dialog)
        btn1.pack(pady=5)
        
        btn2 = CButton(self.app.window, text="Zamknij", 
                      command=self.app.destroy)
        btn2.pack(pady=5)
    
    def pokaz_dialog(self):
        # Okno dialogowe
        dialog = CustomToplevel(self.app)
        dialog.set_title("Dialog")
        dialog.geometry("300x200")
        
        tk.Label(dialog.window, text="To jest okno dialogowe!", 
                bg=dialog.DGRAY, fg='lightgray').pack(pady=20)
        
        CButton(dialog.window, text="Zamknij", 
               command=dialog.destroy).pack()
    
    def uruchom(self):
        self.app.mainloop()

# Uruchom aplikację
if __name__ == "__main__":
    app = MojaAplikacja()
    app.uruchom()
```

## 🎮 Demo i przykłady

Po zainstalowaniu możesz uruchomić przykład demonstracyjny:

```bash
python example.py
```

Przykład pokazuje:
- Przeciąganie okien za pasek tytułu
- Minimalizację i zamykanie okien
- Efekty hover na przyciskach
- Okna modalne i niemodalne
- Stylizację i kolory

## 🔧 Dokumentacja API

### CustomTk
Główne okno aplikacji oparte na `tkinter.Tk`.

```python
app = CustomTk()
app.set_title("Tytuł okna")        # Ustaw tytuł
app.geometry("800x600")            # Ustaw rozmiar
app.mainloop()                     # Uruchom aplikację
```

### CustomToplevel  
Dodatkowe okna dialogowe oparte na `tkinter.Toplevel`.

```python
# Okno niemodalne
dialog = CustomToplevel()

# Okno modalne
modal = CustomToplevel(parent_window)
```

### CButton
Przycisk z efektami wizualnymi.

```python
btn = CButton(parent, text="Tekst", command=funkcja)
btn.pack()
```

### Kolory motywu
Biblioteka używa spójnego motywu kolorów:

- `LGRAY = '#232323'` - jasny szary
- `DGRAY = '#161616'` - ciemny szary (tło)
- `RGRAY = '#2c2c2c'` - regularny szary
- `MGRAY = '#1D1c1c'` - średni szary

## 🖥️ Kompatybilność

- **Python**: 3.7+
- **Systemy**: Windows, macOS, Linux
- **Zależności**: tkinter (wbudowane w Python)

## 📄 Licencja

MIT License - szczegóły w pliku `LICENSE.txt`.

## 🤝 Rozwój

Projekt jest otwarty na pull requesty i sugestie. GitHub: [BetterWindow](https://github.com/AndrzejKoprowski251452/BetterWindow.git)

---

*BetterWindow - Czyń tkinter piękniejszym! 🎨*
