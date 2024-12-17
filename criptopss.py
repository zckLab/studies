import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


def main():
    print("gerador de senhas")
    while True:
        try:
            comprimento = int(input("Quantos caracteres você deseja em sua senha (entre 8 e 50)? "))
            if comprimento < 8 or comprimento > 50:
                print("escolha um número entre 8 e 50.")
            else:
                senha = gerar_senha(comprimento)
                print("Sua senha gerada é:", senha)
                break
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
