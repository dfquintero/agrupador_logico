import tkinter as tk
from tkinter import scrolledtext

PRECEDENCIA = {'¬': 4, '∧': 3, '∨': 2, '→': 1, '↔': 0}
ORDEN = ['¬', '∧', '∨', '→', '↔']

def tokenizar(expr):
    simbolos = ['¬', '∧', '∨', '→', '↔', '(', ')']
    tokens, palabra = [], ''
    for c in expr:
        if c in simbolos:
            if palabra: tokens.append(palabra); palabra = ''
            tokens.append(c)
        elif c.isalnum(): palabra += c
        elif c == ' ' and palabra: tokens.append(palabra); palabra = ''
    if palabra: tokens.append(palabra)
    return tokens

def validar(tokens):
    errores, paren, ant = [], 0, ''
    for i, t in enumerate(tokens):
        if t == '(': paren += 1
        elif t == ')': paren -= 1
        if paren < 0: errores.append("Paréntesis de cierre sin apertura.")
        if t in PRECEDENCIA and t != '¬':
            if ant in PRECEDENCIA or ant == '' or ant == '(': errores.append(f"Operador '{t}' sin operando izquierdo.")
            if i == len(tokens)-1: errores.append(f"Operador '{t}' sin operando derecho.")
        elif not t.isalnum() and t not in PRECEDENCIA and t not in '()': errores.append(f"Símbolo desconocido: '{t}'")
        ant = t
    if paren > 0: errores.append("Faltan paréntesis de cierre.")
    return errores

def agrupar_con_pasos(tokens):
    pasos = []
    expr = tokens[:]
    for op in ORDEN:
        i = 0
        while i < len(expr):
            if expr[i] == op:
                if op == '¬':
                    if i+1 < len(expr):
                        sub = expr[i+1]
                        agrupado = f"(¬{sub})"
                        expr[i:i+2] = [agrupado]
                        pasos.append(f"Negación → {agrupado}")
                        i = max(i-1, 0)
                    else: i += 1
                else:
                    if i-1 >= 0 and i+1 < len(expr):
                        izq = expr[i-1]
                        der = expr[i+1]
                        agrupado = f"({izq} {op} {der})"
                        expr[i-1:i+2] = [agrupado]
                        pasos.append(f"Agrupar con '{op}' → {agrupado}")
                        i = max(i-2, 0)
                    else: i += 1
            else: i += 1
    return expr[0] if expr else "", pasos

def a_latex(expr):
    rep = {'¬': r'\neg ', '∧': r'\wedge', '∨': r'\vee', '→': r'\to', '↔': r'\leftrightarrow'}
    for s, l in rep.items(): expr = expr.replace(s, f' {l} ')
    return f"${expr}$"

class LogicGUI:
    def __init__(self, root):
        root.title("Agrupador lógico con GUI")
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5); self.entry.focus_set()

        ops = ['¬','∧','∨','→','↔','(',')']
        btns = tk.Frame(root)
        for o in ops:
            tk.Button(btns, text=o, width=3,
                      command=lambda s=o: self.entry.insert(tk.INSERT, s))\
              .pack(side=tk.LEFT, padx=2)
        btns.pack()

        tk.Button(root, text="Procesar", command=self.procesar).pack(pady=5)

        self.out = scrolledtext.ScrolledText(root, width=60, height=10, state='disabled')
        self.out.pack(padx=10, pady=(0,5))

        latex_frame = tk.Frame(root)
        tk.Label(latex_frame, text="LaTeX final:").pack(side=tk.LEFT)
        self.latex_entry = tk.Entry(latex_frame, width=50, state='readonly')
        self.latex_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(latex_frame, text="Copiar", command=self.copy_latex).pack(side=tk.LEFT)
        latex_frame.pack(pady=(0,10))

    def procesar(self):
        expr = self.entry.get().replace(' ', '')
        tokens = tokenizar(expr)
        errores = validar(tokens)
        if errores:
            self.set_output("❌ Errores:\n" + "\n".join(f" - {e}" for e in errores))
            self.set_latex("")
        else:
            final, pasos = agrupar_con_pasos(tokens)
            texto = "🔧 Agrupación paso a paso:\n" + "\n".join(f" - {p}" for p in pasos)
            texto += f"\n\n🧾 Final: {final}"
            self.set_output(texto)
            self.set_latex(a_latex(final))

    def set_output(self, text):
        self.out.config(state='normal')
        self.out.delete('1.0', tk.END)
        self.out.insert(tk.END, text)
        self.out.config(state='disabled')

    def set_latex(self, latex):
        self.latex_entry.config(state='normal')
        self.latex_entry.delete(0, tk.END)
        self.latex_entry.insert(0, latex)
        self.latex_entry.config(state='readonly')

    def copy_latex(self):
        self.entry.clipboard_clear()
        self.entry.clipboard_append(self.latex_entry.get())

if __name__ == "__main__":
    root = tk.Tk()
    LogicGUI(root)
    root.mainloop()
    