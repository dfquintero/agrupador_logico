import tkinter as tk
from tkinter import scrolledtext

PRECEDENCIA = {'¬': 4, '∧': 3, '∨': 3, '→': 2, '↔': 2}
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

    def agrupar_prioridad(expr):
        niveles = [
            ['¬'],
            ['∧', '∨'],
            ['→', '↔']
        ]
        for ops in niveles:
            i = 0
            while i < len(expr):
                t = expr[i]
                if t in ops:
                    if t == '¬':
                        count = 1
                        while i + count < len(expr) and expr[i + count] == '¬':
                            count += 1
                        if i + count < len(expr):
                            sub = expr[i + count]
                            for _ in range(count):
                                sub = f"(¬({sub}))"
                            expr[i:i + count + 1] = [sub]
                            pasos.append((f"{'¬'*count} aplicado → {sub}", sub))
                            i = max(i - 1, 0)
                        else:
                            i += count
                    else:
                        if i-1 >= 0 and i+1 < len(expr):
                            izq = expr[i-1]
                            der = expr[i+1]
                            agrupado = f"({izq} {t} {der})"
                            expr[i-1:i+2] = [agrupado]
                            pasos.append((f"Agrupar con '{t}' → {agrupado}", agrupado))
                            i = max(i-2, 0)
                        else:
                            i += 1
                else:
                    i += 1
        return expr

    def resolver_parentesis(expr):
        while '(' in expr:
            stack = []
            for i, t in enumerate(expr):
                if t == '(':
                    stack.append(i)
                elif t == ')':
                    if stack:
                        ini = stack.pop()
                        subexpr = expr[ini+1:i]
                        agrupado = agrupar_prioridad(subexpr)
                        expr[ini:i+1] = agrupado
                        break
            else:
                break
        return expr

    expr = resolver_parentesis(tokens[:])
    expr = agrupar_prioridad(expr)
    return expr[0] if expr else "", pasos

def a_latex(expr):
    rep = {'¬': r'\neg ', '∧': r'\wedge', '∨': r'\vee', '→': r'\to', '↔': r'\leftrightarrow'}
    for s, l in rep.items(): expr = expr.replace(s, f' {l} ')
    return f"${expr}$"

class LogicGUI:
    def __init__(self, root):
        root.title("Agrupador lógico")
        root.configure(bg='#f0f4fc')

        self.entry = tk.Entry(root, width=40, font=('Segoe UI', 11))
        self.entry.pack(pady=5); self.entry.focus_set()

        ops = ['¬','∧','∨','→','↔','(',')']
        btns = tk.Frame(root, bg='#f0f4fc')
        for o in ops:
            tk.Button(btns, text=o, width=4, height=2, font=('Segoe UI', 10),
                      bg='#dbeafe', command=lambda s=o: self.entry.insert(tk.INSERT, s))\
              .pack(side=tk.LEFT, padx=3, pady=3)
        btns.pack()

        tk.Button(root, text="Procesar", font=('Segoe UI', 10, 'bold'),
                  bg='#dbeafe', width=12, height=2, command=self.procesar).pack(pady=8)

        self.out = scrolledtext.ScrolledText(root, width=60, height=15, font=('Segoe UI', 10))
        self.out.pack(padx=10, pady=(0,5))
        self.out.tag_config('center', justify='center')
        self.out.tag_config('resultado', font=('Segoe UI', 12, 'bold'), foreground='darkblue', justify='center')

        latex_frame = tk.Frame(root, bg='#f0f4fc')
        tk.Label(latex_frame, text="LaTeX final:", bg='#f0f4fc', font=('Segoe UI', 10)).pack(side=tk.LEFT)
        self.latex_entry = tk.Entry(latex_frame, width=50, font=('Segoe UI', 10), fg='#006400', state='readonly')
        self.latex_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(latex_frame, text="Copiar", font=('Segoe UI', 9),
                  bg='#dbeafe', command=self.copy_latex).pack(side=tk.LEFT)
        latex_frame.pack(pady=(0,10))

    def procesar(self):
        expr = self.entry.get().replace(' ', '')
        tokens = tokenizar(expr)
        errores = validar(tokens)
        self.out.delete('1.0', tk.END)
        if errores:
            for e in errores:
                self.out.insert(tk.END, f"❌ {e}\n")
        else:
            final, pasos = agrupar_con_pasos(tokens)
            for desc, estado in pasos:
                self.out.insert(tk.END, f"{desc}\n")
                self.out.insert(tk.END, f"{estado}\n\n", 'resultado')
            self.out.insert(tk.END, f"🧾 Final:\n{final}\n", 'resultado')
            self.set_latex(a_latex(final))

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