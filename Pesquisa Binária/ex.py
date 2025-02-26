def pesquisa_binaria(lista, item):
    baixo = 0 #elemento mais baixo (lembrando que o indice começa no zero)
    alto = len(lista) - 1 #elemento mais alto (o ultimo indice é o tamanho da lista - 1)

    while baixo <= alto: #enquanto tiver elemento pra pesquisar
        meio = (baixo + alto) // 2 #encontra o meio
        chute = lista[meio] #mostra o indice do meio

        if chute == item:
            return meio #caso acerte o item
        
        if chute > item: 
            alto = meio - 1 #caso o chute for maior que o item, então o maior indice passa a ser o meio - 1
        else:
            baixo = meio + 1 #caso contrario, o indice mais baixo passa a ser o meio + 1
        
    return None #o numero que foi quera pra ser encontrado não foi achado
    
num = [1, 3, 5, 7, 9]

print(pesquisa_binaria(num, 3)) #retorna o indice dele

print(pesquisa_binaria(num, -1)) #retorna None