

#isto é basicamente um codigo que faz o input do nome e da mensagem
#deixando "nome - mensagem" no final.

import os

mensagens = []

nome = "@" + input("name: ")

while True:

    #limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            
    print("__________")

    #obtendo o texto
    print("Digite fim para cancelar a operação")
    texto = input("Mensagem: ")
    if texto == "fim":
        break


  #adicionar mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
    break