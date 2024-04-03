
#apenas um exemplo, não um projeto

for x in range(5):
    print(x)
    #repetição do valor inicial 0, até o 4, pois não pode alcançar o valor maximo

numerosPrimos = [1, 2, 3, 5, 7 ,11, 13, 17]
print(numerosPrimos)
#insert é usado para adicionar um elemento em um local especifico de uma lista
#escolha a posição do numero (começa com 0 e vai em diante) e depois o que vc quer inserir T
#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
numerosPrimos.insert(4, "5.2")
print(numerosPrimos)

notas = []
for x in range(2):
    codigo_aluno = input("RM: ")
    nota = float(input("Digite sua nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)  #append é basicamente um insert( ), mas você só pode adicionar um elemento no final da lista
    print(notas)

    print("Quantidade de notas:", len(notas)) #obtem o comprimento de uma variavel
    for n in notas:
        codigo_aluno = n[0]
        nota = n[1]
        print("O RM: ", codigo_aluno, "tirou a nota: ", nota)