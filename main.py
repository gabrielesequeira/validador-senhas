import re 
import tkinter as tk
from tkinter import messagebox



#FUNÇÕES
def validar_senha(senha):
    erros = []

    # Verifica se a senha tem menos de 8 caracteres
    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    # Verifica se a senha contém pelo menos uma letra maiúscula (A-Z)
    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")

    # Verifica se a senha contém pelo menos uma letra minúscula (a-z)
    if not re.search(r"[a-z]", senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")

    # Verifica se a senha contém pelo menos um número (0-9)
    if not re.search(r"[0-9]", senha):
        erros.append("A senha deve conter pelo menos um número.")

    # Verifica se a senha contém pelo menos um símbolo especial (!@#... etc)
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha): #re.search(...) retorna None se não encontrar, então usamos not para testar a ausência.
        erros.append("A senha deve conter pelo menos um caractere especial.")

    return erros


#função chamada quando o botão "Validar é clicado"

def ao_clicar_validar():
    senha = entrada_senha.get()
    erros= validar_senha(senha)

    if erros:
        resultado = "Senha fraca \n" + "\n".join(f"- {e}" for e in erros)
        messagebox.showwarning ("Resultado" , resultado)
    else: 
        messagebox.showinfo("Resultado", "Senha forte! 🔐")    


#BLOCO PRINCIPAL
janela = tk.Tk()
janela.title = ("Validador de senhas")
janela.geometry("300x150")
label = tk.Label(janela, text = "Digite sua senha: ")
label.pack(pady=5)
entrada_senha = tk.Entry(janela, show="*", width = 30) # show="*" - oculpa os caracteres digitados
entrada_senha.pack(pady=5)
botao = tk.Button(janela,text="Validar", command=ao_clicar_validar)
botao.pack (pady=10)

janela.mainloop()