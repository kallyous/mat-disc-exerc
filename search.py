# binary_search_find_or_get_next(primes, -1, len(primes), int_root_over)


def binary_search_find_or_get_next(prime_list, start, end, target_value):
    """ Uso: binary_search_find_or_get_next(list, 0, len(list), search_value)

        A busca é feita do indice 0 até end-1

        Se o valor não for encontrado, retorna o menor mais próximo presente na lista

        Se o valor buscado estiver acima do valor do ultimo índice, retorna o útimo
        índice, pois este é menor mais próximo presente na lista
        """

    # Normaliza start, caso necessário
    if (start == -1):
        start = 0

    # Evita erros devido a lista vazia
    if len(prime_list) < 1:
        return -1

    """ Cálculo do ponto médio.
        'mid' nunca irá cair em 'end', e cairá em 'start' se (start == end - 1) """
    mid = start + ((end - start) // 2)

    """ Se o valor encontrado é exatamente o alvo, retornamos o índice imediatamente """
    if target_value == prime_list[mid]:
        return mid

    """ Se o ponto médio é o mesmo que o limite esquerdo, mas o valor alvo não está aqui,
        então o maior valor inteiro mais próximo do alvo está fora da lista.
        Contudo, o valor que usaremos é o de mid, pois é o maior valor presente na lista
        menor que o valor alvo. """
    if mid == start:
        return mid

    # Determina se devemos continuar à esquerda ou direita
    if prime_list[mid] < target_value:
        """ Se o valor buscado é menor que o valor em mid, continue à esquerda """
        return binary_search_find_or_get_next(prime_list, start, mid, target_value)
    else:
        """ Caso o valor buscado seja maior que o valor em mid, continue à direita """
        return binary_search_find_or_get_next(prime_list, mid, end, target_value)
