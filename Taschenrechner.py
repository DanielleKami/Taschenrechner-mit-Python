import tkinter as tk
from tkinter import ttk, scrolledtext
import math

class KomponenteCalco(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.konponenE()
        
    def konponenE(self):
        self.ButtonE()
        self.textFE()
        self.historyDisplayE()
        
    def ButtonE(self):
        # Erste Spalte
        self.sieben = ttk.Button(self, text="7")
        self.sieben.place(x=0, y=100, width=50, height=50)
        
        self.vier = ttk.Button(self, text="4")
        self.vier.place(x=0, y=150, width=50, height=50)
        
        self.ein = ttk.Button(self, text="1")
        self.ein.place(x=0, y=200, width=50, height=50)
        
        self.nul = ttk.Button(self, text="0")
        self.nul.place(x=0, y=250, width=50, height=50)
        
        # Zweite Spalte
        self.acht = ttk.Button(self, text="8")
        self.acht.place(x=50, y=100, width=50, height=50)
        
        self.fuenf = ttk.Button(self, text="5")
        self.fuenf.place(x=50, y=150, width=50, height=50)
        
        self.zwei = ttk.Button(self, text="2")
        self.zwei.place(x=50, y=200, width=50, height=50)
        
        self.gleich = ttk.Button(self, text="=")
        self.gleich.place(x=50, y=250, width=50, height=50)
        
        # Dritte Spalte
        self.neun = ttk.Button(self, text="9")
        self.neun.place(x=100, y=100, width=50, height=50)
        
        self.sechs = ttk.Button(self, text="6")
        self.sechs.place(x=100, y=150, width=50, height=50)
        
        self.drei = ttk.Button(self, text="3")
        self.drei.place(x=100, y=200, width=50, height=50)
        
        self.punkt = ttk.Button(self, text=".")
        self.punkt.place(x=100, y=250, width=50, height=50)
        
        # Vierte Spalte - Grundoperationen
        self.plus = ttk.Button(self, text="+")
        self.plus.place(x=150, y=100, width=50, height=50)
        
        self.minus = ttk.Button(self, text="-")
        self.minus.place(x=150, y=150, width=50, height=50)
        
        self.mal = ttk.Button(self, text="*")
        self.mal.place(x=150, y=200, width=50, height=50)
        
        self.div = ttk.Button(self, text="/")
        self.div.place(x=150, y=250, width=50, height=50)
        
        # Fünfte Spalte - Erweiterte Funktionen
        self.quadrat = ttk.Button(self, text="x²")
        self.quadrat.place(x=200, y=100, width=50, height=50)
        
        self.sqr = ttk.Button(self, text="√")
        self.sqr.place(x=200, y=150, width=50, height=50)
        
        # NEUE BUTTONS: ln, exp, mod
        self.ln = ttk.Button(self, text="ln")
        self.ln.place(x=200, y=200, width=50, height=50)
        
        self.exp = ttk.Button(self, text="e^")
        self.exp.place(x=200, y=250, width=50, height=50)
        
        self.mod = ttk.Button(self, text="%")
        self.mod.place(x=250, y=100, width=50, height=50)
        
        # Steuerungs-Buttons
        self.delet = ttk.Button(self, text="<-")
        self.delet.place(x=250, y=150, width=50, height=50)
        
        self.clr = ttk.Button(self, text="C")
        self.clr.place(x=250, y=200, width=50, height=50)
        
    def textFE(self):
        self.menu = tk.Entry(self, justify='right', font=('TimesRoman', 20, 'bold'),
                           bg='black', fg='white', disabledbackground='black',
                           disabledforeground='white')
        self.menu.insert(0, "0")
        self.menu.config(state='disabled')
        self.menu.place(x=0, y=50, width=300, height=50)
        
    def historyDisplayE(self):
        self.historyDisplay = scrolledtext.ScrolledText(self, wrap=tk.WORD,
                                                      bg='dark gray', fg='green',
                                                      font=('Courier New', 12),
                                                      state='disabled')
        self.historyDisplay.place(x=0, y=0, width=300, height=50)
        
    def addToHistory(self, operation):
        self.historyDisplay.config(state='normal')
        self.historyDisplay.insert(tk.END, operation + "\n")
        self.historyDisplay.see(tk.END)
        self.historyDisplay.config(state='disabled')
        
    def clearHistory(self):
        self.historyDisplay.config(state='normal')
        self.historyDisplay.delete(1.0, tk.END)
        self.historyDisplay.config(state='disabled')


class Taschenrechner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced Calculator")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        
        # Center the window
        window_width = 310
        window_height = 350
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.pan = KomponenteCalco(self.root)
        self.pan.pack(fill='both', expand=True)
        
        self.text = ""
        self.op1 = 0
        self.op2 = 0
        self.result = 0
        self.sign = ''
        self.isOPdran = False
        self.newCalculation = True
        self.currentOperation = ""
        
        self.deaktierenalleB(False)
        self.setupActionListeners()
        
    def setupActionListeners(self):
        # Nummern Buttons
        self.pan.ein.config(command=lambda: self.zahlHinzufuegen("1"))
        self.pan.zwei.config(command=lambda: self.zahlHinzufuegen("2"))
        self.pan.drei.config(command=lambda: self.zahlHinzufuegen("3"))
        self.pan.vier.config(command=lambda: self.zahlHinzufuegen("4"))
        self.pan.fuenf.config(command=lambda: self.zahlHinzufuegen("5"))
        self.pan.sechs.config(command=lambda: self.zahlHinzufuegen("6"))
        self.pan.sieben.config(command=lambda: self.zahlHinzufuegen("7"))
        self.pan.acht.config(command=lambda: self.zahlHinzufuegen("8"))
        self.pan.neun.config(command=lambda: self.zahlHinzufuegen("9"))
        self.pan.nul.config(command=lambda: self.zahlHinzufuegen("0"))
        
        # Grund-Operatoren
        self.pan.plus.config(command=lambda: self.operatorSetzen('+'))
        self.pan.minus.config(command=lambda: self.operatorSetzen('-'))
        self.pan.mal.config(command=lambda: self.operatorSetzen('*'))
        self.pan.div.config(command=lambda: self.operatorSetzen('/'))
        self.pan.mod.config(command=lambda: self.operatorSetzen('%'))
        
        # Spezialfunktionen
        self.pan.gleich.config(command=self.berechnen)
        self.pan.delet.config(command=self.loeschen)
        self.pan.punkt.config(command=self.punktHinzufuegen)
        self.pan.quadrat.config(command=self.quadratBerechnen)
        self.pan.sqr.config(command=self.wurzelBerechnen)
        
        # NEUE FUNKTIONEN
        self.pan.ln.config(command=self.naturalLogarithmusBerechnen)
        self.pan.exp.config(command=self.exponentialBerechnen)
        
        self.pan.clr.config(command=self.allesLoeschen)
        
    def zahlHinzufuegen(self, zahl):
        if self.newCalculation:
            self.text = ""
            self.newCalculation = False
            
        current_text = self.getDisplayText()
        if current_text == "0" or current_text == "Error":
            self.text = zahl
        else:
            self.text = self.text + zahl
            
        self.updateDisplay(self.text)
        self.deaktierenalleB(True)
        
    def operatorSetzen(self, operator):
        if self.text:
            try:
                self.op1 = float(self.text)
                self.sign = operator
                
                # Für History
                self.currentOperation = self.text + " " + operator
                
                self.text = ""
                self.updateDisplay(str(self.op1))
                self.isOPdran = True
                self.newCalculation = False
            except ValueError:
                self.updateDisplay("Error")
                
    def berechnen(self):
        if self.isOPdran and self.text:
            try:
                self.op2 = float(self.text)
                self.result = self.doOperation(self.op1, self.op2, self.sign)
                gerundet = self.arrondi(self.result)
                
                # Zur History hinzufügen
                history_entry = self.currentOperation + " " + self.text + " = " + str(gerundet)
                self.pan.addToHistory(history_entry)
                
                self.updateDisplay(str(gerundet))
                self.text = str(gerundet)
                self.isOPdran = False
                self.currentOperation = ""
                self.newCalculation = True
            except (ValueError, ZeroDivisionError):
                self.updateDisplay("Error")
                self.pan.addToHistory(self.currentOperation + " " + self.text + " = Error")
                self.text = ""
                self.newCalculation = True
                
    def loeschen(self):
        if len(self.text) > 0:
            self.text = self.text[:-1]
            if not self.text:
                self.text = "0"
                self.deaktierenalleB(False)
                self.newCalculation = True
            self.updateDisplay(self.text)
            
    def punktHinzufuegen(self):
        if self.newCalculation:
            self.text = "0."
            self.newCalculation = False
        elif "." not in self.text:
            if not self.text:
                self.text = "0."
            else:
                self.text = self.text + "."
        self.updateDisplay(self.text)
        
    def quadratBerechnen(self):
        if self.text:
            try:
                value = float(self.text)
                ergebnis = value * value
                gerundet = self.arrondi(ergebnis)
                
                self.pan.addToHistory(self.text + "² = " + str(gerundet))
                self.updateDisplay(str(gerundet))
                self.text = str(gerundet)
                self.newCalculation = True
            except ValueError:
                self.updateDisplay("Error")
                
    def wurzelBerechnen(self):
        if self.text:
            try:
                value = float(self.text)
                if value >= 0:
                    ergebnis = math.sqrt(value)
                    gerundet = self.arrondi(ergebnis)
                    
                    self.pan.addToHistory("√" + self.text + " = " + str(gerundet))
                    self.updateDisplay(str(gerundet))
                    self.text = str(gerundet)
                    self.newCalculation = True
                else:
                    self.updateDisplay("Error")
                    self.pan.addToHistory("√" + self.text + " = Error")
                    self.text = ""
                    self.newCalculation = True
            except ValueError:
                self.updateDisplay("Error")
                
    def naturalLogarithmusBerechnen(self):
        if self.text:
            try:
                value = float(self.text)
                if value > 0:
                    ergebnis = math.log(value)
                    gerundet = self.arrondi(ergebnis)
                    
                    self.pan.addToHistory("ln(" + self.text + ") = " + str(gerundet))
                    self.updateDisplay(str(gerundet))
                    self.text = str(gerundet)
                    self.newCalculation = True
                else:
                    self.updateDisplay("Error")
                    self.pan.addToHistory("ln(" + self.text + ") = Error")
                    self.text = ""
                    self.newCalculation = True
            except ValueError:
                self.updateDisplay("Error")
                
    def exponentialBerechnen(self):
        if self.text:
            try:
                value = float(self.text)
                ergebnis = math.exp(value)
                gerundet = self.arrondi(ergebnis)
                
                self.pan.addToHistory("e^" + self.text + " = " + str(gerundet))
                self.updateDisplay(str(gerundet))
                self.text = str(gerundet)
                self.newCalculation = True
            except ValueError:
                self.updateDisplay("Error")
                
    def allesLoeschen(self):
        self.text = ""
        self.op1 = 0
        self.op2 = 0
        self.result = 0
        self.updateDisplay("0")
        self.pan.clearHistory()
        self.deaktierenalleB(False)
        self.isOPdran = False
        self.currentOperation = ""
        self.newCalculation = True
        
    def doOperation(self, op1, op2, sign):
        try:
            if sign == '+':
                return op1 + op2
            elif sign == '-':
                return op1 - op2
            elif sign == '*':
                return op1 * op2
            elif sign == '/':
                if op2 != 0:
                    return op1 / op2
                else:
                    self.updateDisplay("Error")
                    self.pan.addToHistory("Division durch 0!")
                    self.newCalculation = True
                    return 0
            elif sign == '%':
                if op2 != 0:
                    return op1 % op2
                else:
                    self.updateDisplay("Error")
                    self.pan.addToHistory("Modulo durch 0!")
                    self.newCalculation = True
                    return 0
            else:
                return 0
        except Exception as e:
            self.updateDisplay("Error")
            return 0
            
    def deaktierenalleB(self, b):
        state = 'normal' if b else 'disabled'
        self.pan.plus.config(state=state)
        self.pan.minus.config(state=state)
        self.pan.mal.config(state=state)
        self.pan.div.config(state=state)
        self.pan.mod.config(state=state)
        self.pan.gleich.config(state=state)
        self.pan.punkt.config(state=state)
        self.pan.quadrat.config(state=state)
        self.pan.sqr.config(state=state)
        self.pan.ln.config(state=state)
        self.pan.exp.config(state=state)
        
    def arrondi(self, nbr):
        return round(nbr * 100000.0) / 100000.0
        
    def getDisplayText(self):
        self.pan.menu.config(state='normal')
        text = self.pan.menu.get()
        self.pan.menu.config(state='disabled')
        return text
        
    def updateDisplay(self, text):
        self.pan.menu.config(state='normal')
        self.pan.menu.delete(0, tk.END)
        self.pan.menu.insert(0, text)
        self.pan.menu.config(state='disabled')
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calculator = Taschenrechner()
    calculator.run()