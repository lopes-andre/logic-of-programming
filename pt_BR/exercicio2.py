# EXERCÍCIO DESENVOLVIDO NA IDE: Visual Studio Code v1.55.2

def pegaInt(frase, min, max):
    """Função que recebe três parâmetros e valida o número de entrada dentro do intervalo definido pelo usuário.
    Parâmetro 1: frase a ser impressa na tela;
    Parâmetro 2: valor mínimo do intervalo que o número deve estar dentro;
    Parâmetro 3: valor máximo do intervalo que o número deve estar dentro."""

    while True: # Loop infitino até receber um valor válido
        try:
            a = int(input(frase)) # Recebe o valor do teclado e tenta converter para int
        except:
            print("Digite um número válido!") # Caso haja algum erro, imprime o alerta e retorna o loop
            continue
        else:
            if (a > min) and (a < max): # Verifica se o número está dentro do intervalo
                break
            elif a == 0: # Fecha o programa caso o usuário digite 0
                quit()
            else:
                print(f"Digite um número entre {min} e {max}!") # Imprime alerta caso fora do intervalo
                continue
    return a

# Programa principal
print("### GERADOR DE CÓDIGO VERIFICADOR DOS PRODUTOS ###")
while True:
    cod = pegaInt("\nDigite o código do produto (0 para sair): ", 10000, 30000)
    digito = str(cod) # Converte o código em string
    digito = map(int, digito) # Mapeia cada digito da string para um int
    digito = list(digito) # Converte para lista

    j = 2 # Objeto 'peso' iniciando em 2 e sendo iterado
    for i in range(len(digito)): # Loop para multiplicar cada item pelo peso
        digito[i] *= j
        j += 1
    digito = sum(digito) # Soma todos os valores da lista
    digito %= 7 # Realiza o cálculo do resto na divisão por 7
    
    print(f"\nCódigo do produto com dígito verificador: {cod}-{digito}.")

