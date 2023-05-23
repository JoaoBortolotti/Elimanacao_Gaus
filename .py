import math
import tkinter as tk

def gaussPivoteamento():
    A = []
    b = []
    entries = []
    
    for i in range(len(entries)):
        row = []
        for j in range(len(entries[i])):
            row.append(float(entries[i][j].get()))
        A.append(row)
        b.append(float(entries[i][-1].get()))
    
    for i in range(len(A)):
        pivo = math.fabs(A[i][i])
        linhaPivo = i
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                linhaPivo = j
        if linhaPivo != i:
            linhaAuxiliar = A[i]
            A[i] = A[linhaPivo]
            A[linhaPivo] = linhaAuxiliar

            bAuxiliar = b[i]
            b[i] = b[linhaPivo]
            b[linhaPivo] = bAuxiliar
        for m in range(i+1, len(A)):
            multiplicador = A[m][i] / A[i][i]
            for n in range(i, len(A)):
                A[m][n] -= multiplicador * A[i][n]
            b[m] -= multiplicador * b[i]
    
    result = tk.Toplevel()
    result.title("Resultado")
    
    for k in range(len(A)):
        for n in range(len(A[k])):
            tk.Label(result, text=str(A[k][n])).grid(row=k, column=n)
        tk.Label(result, text="|").grid(row=k, column=len(A[k]))
        tk.Label(result, text=str(b[k])).grid(row=k, column=len(A[k])+1)
    
    tk.Label(result, text="Solução:").grid(row=len(A), column=0, sticky=tk.W)
    calculaSolucao(A, b, result)
    
def calculaSolucao(A, b, result):
    vetorSolucao = []
    for i in range(len(A)):
        vetorSolucao.append(0)
    linha = len(A) - 1
    while linha >= 0:
        x = b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x -= A[linha][coluna] * vetorSolucao[coluna]
            coluna -= 1
        x /= A[linha][linha]
        vetorSolucao[linha] = x
        linha -= 1
    
    for j in range(len(vetorSolucao)):
        tk.Label(result, text="x" + str(j) + " = " + str(vetorSolucao[j])).grid(row=len(A)+1+j, column=0, sticky=tk.W)

def create_entry(root, row, column):
    entry = tk.Entry(root, width=5)
    entry.grid(row=row, column=column)
    return entry

def create_matrix_input(root, rows, columns):
    entries = []
    for i in range(rows):
        row_entries = []
        for j in range(columns+1):
            entry = create_entry(root, i, j)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries

root = tk.Tk()
root.title("Eliminação de Gauss")

matrix_frame = tk.Frame(root)
matrix_frame.pack(pady=10)

tk.Label(matrix_frame, text="Matriz A").grid(row=0, columnspan=3)
tk.Label(matrix_frame, text="Vetor b").grid(row=0, column=4)

entries = create_matrix_input(matrix_frame, 3, 3)

calculate_button = tk.Button(root, text="Calcular", command=gaussPivoteamento)
calculate_button.pack(pady=5)

root.mainloop()