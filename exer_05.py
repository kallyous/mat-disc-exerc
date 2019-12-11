def mdc_eucli(a, b):
    if b == 0:
        return a
    return mdc_eucli(b, a % b)


if __name__ == '__main__':

    while True:

        print('\nAlgorítmo de Euclides para encontrar o Maior Divisor Comum entre dois números.')
        print('Entre dois números separados por um espaço para encontrar o MDC.')
        print('Entre linha em branco para sair.\n')

        arg_str = input(' >>> ')
        if arg_str == '':
            break

        args = arg_str.split()

        if len(args) < 2:
            print('Entrada inválida.')
            continue

        if not (args[0].isnumeric() and args[1].isnumeric()):
            print('Entrada inválida.')
            continue

        a = int(args[0])
        b = int(args[1])
        res = mdc_eucli(a, b)

        print(f'mdc({a},{b}) = {res}')
