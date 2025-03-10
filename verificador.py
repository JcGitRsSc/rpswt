import re

def verificar_senha(senha):
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    if not re.search(r"[A-Z]", senha):
        return False, "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search(r"[a-z]", senha):
        return False, "A senha deve conter pelo menos uma letra minúscula."

    if not re.search(r"\d", senha):
        return False, "A senha deve conter pelo menos um número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "A senha deve conter pelo menos um caractere especial."

    return True, "Senha válida!"


senha = input("Digite a senha: ")
valida, mensagem = verificar_senha(senha)

if valida:
    print("Senha válida!")
else:
    print(mensagem)

if valida:
    print("Senha válida!")
else:
    print(mensagem)