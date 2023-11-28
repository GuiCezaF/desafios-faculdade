def isPerfectSquare(n):
    # Função para verificar se n é uma raiz quadrada perfeita
    raiz = int(n**0.5)
    return raiz * raiz == n


def WordSquare(letters):
    n = len(letters)

    # Verifique se o comprimento é uma raiz quadrada perfeita
    if not isPerfectSquare(n):
        return False

    tamanho = int(n**0.5)

    # Crie um array bidimensional
    quadrado_palavras = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

    # Preencha o array bidimensional com as letras da string
    for i in range(tamanho):
        for j in range(tamanho):
            quadrado_palavras[i][j] = letters[i * tamanho + j]

    # Verifique se as palavras nas linhas são iguais às palavras nas colunas
    for i in range(tamanho):
        palavra_linha = ''.join(quadrado_palavras[i])
        palavra_coluna = ''.join(
            quadrado_palavras[j][i] for j in range(tamanho))
        if palavra_linha != palavra_coluna:
            return False

    return True


# Exemplos de uso:
letras1 = "SATORAREPOTENETOPERAROTAS"
print(WordSquare(letras1))  # Deve imprimir True

letras3 = "NOTSQUARE"
print(WordSquare(letras3))  # Deve imprimir False
