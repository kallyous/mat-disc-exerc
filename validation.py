def validate_list_str_num(str_list, expected_length):
    """Retorna lista convertida em int se validação for bem sucedida, ou uma lista vazia caso contrário."""

    if len(str_list) < expected_length:
        print('Argumentos insuficientes')
        return []

    cast_list = []

    for i in range(0, len(str_list)):
        if not str_list[i].strip('-').isnumeric():
            print('Argumentos inválidos')
            return []
        else:
            cast_list.append(int(str_list[i]))

    return cast_list
