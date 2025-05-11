import re 



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
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("A senha deve conter pelo menos um caractere especial.")


    # se a lista conter algum erro, significa que a senha é fraca
    if erros: 
        print("Senha fraca: ")
        for e in erros:
            print("-" + e)


    # se não hoouver nenhum elemento 
    else :
        print("Senha Forte! 🔐")
    


#BLOCO PRINCIPAL
senha_usuario = input("Digite sua senha para validação:")
validar_senha(senha_usuario)
            