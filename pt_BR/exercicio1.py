# EXERCÍCIO DESENVOLVIDO NA IDE: Visual Studio Code v1.55.2

while True: # Loop infinito que será quebrado caso o usuário digite "sair" (non case-sensitive)
    print("### VERIFICAÇÃO DE CATEGORIAS DE LUTADORES ###\n(Digite \"sair\" para fechar o programa)")

    nome = input("Nome fornecido: ") # Recebe do teclado o nome do lutador

    if nome.upper() == "SAIR": break # Encerra o programa caso o usuário digite sair

    while True: # Loop para receber um peso válido, maior que zero e que seja um número real (float)
        try:
            peso = float(input("Peso fornecido: ")) # Recebe o peso num objeto de tipo float
            
            if peso > 0: # Se o peso for maior do que zero, o loop é quebrado e o programa segue com a execução
                break
        
        except: # Caso haja algum erro no input de valor do peso, o loop roda novamente
            print("Informe um peso válido!")
            continue

    # Início das condições para verificar a categoria do lutador
    # são usadas condicionais de múltipla escolha
    if peso < 65: categ = "Pena"

    elif peso > 65 and peso < 72: categ = "Leve"

    elif peso > 72 and peso < 79: categ = "Ligeiro"

    elif peso > 79 and peso < 86: categ = "Meio-médio"

    elif peso > 86 and peso < 93: categ = "Médio"

    elif peso > 93 and peso < 100: categ = "Meio-pesado"

    else: categ = "Pesado"

    print(f"O lutador {nome} pesa {peso:.1f}kg e se enquadra na categoria {categ}.\n")

print("\nFechando o programa...")