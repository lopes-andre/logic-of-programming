# EXERCÍCIO DESENVOLVIDO NA IDE: Visual Studio Code v1.55.2

# Declaração das listas
nomes = []
tels = []
idades = []
# Declaração de dicionários
agenda = {}
agendaMenores = {}
agendaMaiores = {}

print("\n#### ADICIONAR NOVOS CONTATOS (contato vazio para sair) ###")
while True: # Loop para adição de novos contatos, até que string vazia seja inserida
    nome = input("\nDigite o nome do contato: ") # Salve o nome no objeto 'nome'

    if nome == "": break # Quebra o loop de adicionar contatos caso string vazia

    elif nome in nomes: # Verifica se o nome já existe na lista
        print("Contato já cadastrado!")
        continue

    nomes.append(nome) # Adiciona o nome à lista nomes[]

    # Recebe o telefone e salva na lista telefones[]
    tel = input(f"Digite o telefone do(a) {nome}: ")
    tels.append(tel)
    
    # Faz um loop para validar a idade como int e maior que zero
    while True:
        try:
            idade = int(input(f"Digite a idade do(a) {nome}: "))
            if idade > 0: break
            continue
        except: continue
    idades.append(idade) # Adiciona a idade na lista idades[]

# Faz um loop pelos nomes adicionandos os nomes como keys do 
# dicionário agenda{} e inserindo uma lista como value contendo
# o telefone e a idade de cada contato 
for i in range(len(nomes)):
    agenda[nomes[i]] = [tels[i], idades[i]]

# Imprime o cabeçalho da agenda completa
titulo = "### AGENDA DE TODOS OS CONTATOS ###"
menu = ["NOME", "TELEFONE", "IDADE"]
print(f"\n{titulo:^59}")
print(f"{menu[0]:^28} | {menu[1]:^18} | {menu[2]:^7}\n"+("-"*59))

# Loop pegando nome e dados da agenda.items() organizada em ordem
# alfabética e imprimindo na tela de forma formatada
for nome, dados in sorted(agenda.items()):
    
    print(f"{nome:^28} | {dados[0]:^18} | {dados[1]:^7}")

    # Condicional para verificar se o contato é maior ou menor de 18 anos
    # Adiciona ao dicionário agendaMaiores{} se for maior de idaade
    # ou ao dicionario agendaMenores{} se for menor de idade
    if(dados[1] >= 18): agendaMaiores[nome] = [dados[0], dados[1]]

    else: agendaMenores[nome] = [dados[0], dados[1]]

agenda.clear() # Eliminação do dicionário original

# Imprime o cabeçalho da agenda de maiores de idade
titulo = "### AGENDA DE MAIORES DE IDADE ###"
menu = ["NOME", "TELEFONE", "IDADE"]
print(f"\n{titulo:^59}")
print(f"{menu[0]:^28} | {menu[1]:^18} | {menu[2]:^7}\n"+("-"*59))
# Loop pegando nome e dados da agendaMaiores.items() organizada em ordem
# alfabética e imprimindo na tela de forma formatada
for nome, dados in sorted(agendaMaiores.items()):
    print(f"{nome:^28} | {dados[0]:^18} | {dados[1]:^7}")

# Imprime o cabeçalho da agenda de menores de idade
titulo = "### AGENDA DE MENORES DE IDADE ###"
menu = ["NOME", "TELEFONE", "IDADE"]
print(f"\n{titulo:^59}")
print(f"{menu[0]:^28} | {menu[1]:^18} | {menu[2]:^7}\n"+("-"*59))
# Loop pegando nome e dados da agendaMenores.items() organizada em ordem
# alfabética e imprimindo na tela de forma formatada
for nome, dados in sorted(agendaMenores.items()):
    print(f"{nome:^28} | {dados[0]:^18} | {dados[1]:^7}")

print()
