def escalonada_reduzida(matriz):
    # Determinando o número de linhas e colunas da matriz
    linha = len(matriz)
    coluna = len(matriz[0])

    # Inicializa uma lista de índices para seguir a ordem das equações
    zero = 0

    # Loop por todas as colunas na matriz
    for j in range(coluna):
        # Encontra o índice do primeiro elemento não nulo na coluna j
        for i in range(zero, linha):
            if matriz[i][j] != 0:
                # Troca as linhas para colocar o elemento não nulo na posição j
                matriz[zero], matriz[i] = matriz[i], matriz[zero]
                break
        else:
            # Se não houver elemento não nulo, passe para a próxima coluna
            continue

        # Divide a linha para tornar o elemento na posição j igual a 1 (Caso seja correto)
        # Variável (Atual) trabalha com o elemento "Pilar"
        atual = matriz[zero][j]

        # Variável (Arco) trabalha junto com a matriz / colunas / linhas
        matriz[zero] = [arco / atual for arco in matriz[zero]]

        # Subtrai a linha da posição 0 / j de todas as outras linhas para zerar todos os elementos na coluna j abaixo da posição 0 / j
        for i in range(linha):
            if i == zero:
                continue
            factor = matriz[i][j]
            matriz[i] = [arco - factor * arco_atual for arco, arco_atual in zip(matriz[i], matriz[zero])]

        # Avança para a próxima linha e coluna
        zero += 1


    for elemento in matriz:
        print(" |".join(str(pao) for pao in elemento))
    
    # Da um "Print" de forma elegante

#Matriz <----DIGITE ELA EM BAIXO---->
A = [[3, 2, 1, 4], [6, -5, 2, -1], [1, -1, -1, 1]]
escalonada_reduzida(A)

