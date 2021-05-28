# EXERCÍCIO DESENVOLVIDO NA IDE: Visual Studio Code v1.55.2

notas = {} # Cria o dicionário vazio

def qtd_alunos():
    """Função para receber do usuário via teclado a quantidade
    de alunos a ser trabalhada. Descarta o 0 e todos os números
    negativos e descarta qualquer entrada que não seja do tipo float"""
    while True: # Loop infinito até a quantidade ser um número positivo de alunos
        try:
            qtd = int(input("Digite a quantidade de alunos: "))
            if qtd >= 0: break
            print("Digite um número válido de alunos!")
            continue
        except: # Reinicia o loop caso algo dê errado
            print("Digite um número válido de alunos!")
    return qtd # Retorna a quantidade de alunos

def pega_nota(frase):
    """Função para receber do usuário via teclado uma nota e
    vadidá=la quanto ao valor (entre 0 e 10) e também trata e 
    descarta qualquer valor que não seja do tipo float"""
    while True: # Loop infinito até a nota ser válida
        try:
            nota = float(input(frase))
            if nota >= 0 and nota <= 10: break # Nota entre 0.0 e 10.0
            print("Digite uma nota válida!")
            continue
        except: # Reinicia o loop caso algo dê errado
            print("Digite uma nota válida!")
            continue
    return nota # Retorna o valor da nota

# Programa principal
print("### CADASTRO DE NOTAS DE ALUNOS ###")
qtd = qtd_alunos() # Pega a quantidade de alunos a serem cadastrados

# Função lambda para cálculo de média aritmética
media = lambda n1, n2, n3, n4: (n1 + n2 + n3 + n4) / 4

# Declara os objetos necessários
nota = 0 
media_aluno = 0
# Lista de médias separada pois o enunciado define a estrutura do dicionário
medias = []  

for i in range(qtd): # Loop que cadastra a quantidade de alunos inserida
    nome = input("\nNome do aluno: ")
    notas[nome] = [] # Cria uma 'key' no dicionário com o nome do aluno
    for j in range(1, 5): # Loop para inserir as 4 notas do aluno
        nota = pega_nota(f"Digite a nota #{j} do aluno: ")
        notas[nome].append(nota) # Adiciona cada nota na lista relacionada ao nome no dic
    
    media_aluno = media(*notas[nome])
    if media_aluno >= 7: status = "Aprovado"
    else: status = "Reprovado"
    
    medias.append(media_aluno)
    notas[nome].append(status) # Adiciona o status à lista

# print(notas)

titulo = ["Notas dos alunos", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Média", "Status"]
print(f"\n\n{titulo[0]:<27} {titulo[1]:<7} {titulo[2]:<7} {titulo[3]:<7} {titulo[4]:<7} {titulo[5]:<7} {titulo[6]:<7}")
print("-"*20)

i = 0 # Iteração para índice da lista 'medias[]'
for nome in notas: # Loop para imprimir na tela os nomes dos alunos
    print(f"{nome:<28}",end="") # Imprime os nomes formatados
    for k in range(len(notas[nome])-1): # Loop para imprimir as todas dos alunos
        print(f"{notas[nome][k]:<8.1f}", end="") # Imprime todas as todas de cada alunos
    print(f"{medias[i]:<8.1f}", end="") # Imprime a média de cada aluno
    print(f"{notas[nome][-1]}") # Imprime por último, na mesma linha, o status
    print()
    i += 1
    