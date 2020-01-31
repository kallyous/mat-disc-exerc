def mdc_eucli_coef(a, b, coef: list):
    if b == 0:
        return a, coef

    q = a // b
    r = a % b

    i = len(coef)
    m = coef[i - 2]['m'] - (q * coef[i - 1]['m'])
    n = coef[i - 2]['n'] - (q * coef[i - 1]['n'])

    c = {'r': r, 'q': q, 'm': m, 'n': n}

    coef.append(c)

    return mdc_eucli_coef(b, r, coef)


def mdc_eucli_ext(a, b):
    pack = [{'r': a, 'q': None, 'm': 1, 'n': 0},
            {'r': b, 'q': None, 'm': 0, 'n': 1}]

    return mdc_eucli_coef(a, b, pack)


if __name__ == '__main__':
    print('\n ----- Teorema de Euclides Extendido para encontrar a*s + b*t = r -----')
    while True:
        opt = input('\nEntre dois números separados por espaço\n > ')
        args = opt.split()
        if len(args) < 2:
            print('Argumentos insuficientes.')
            continue
        elif not (args[0].isnumeric() and args[1].isnumeric()):
            print('Argumentos inválidos.')
            continue
        a = int(args[0])
        b = int(args[1])

        res, coef = mdc_eucli_ext(a, b)

        print(f'\nmdc({a},{b}) = {res}\n')
        print('Combinações lineares encontradas, na forma a*s + b*t = r :   ')

        for i in range(0, len(coef)):
            print('  {}*({}) + {}*({}) = {}'.format(
                a, coef[i]['m'], b, coef[i]['n'], coef[i]['r']))

        i = len(coef) - 2
        print('\nResposta:\n  {}*({}) + {}*({}) = {}'.format(
            a, coef[i]['m'], b, coef[i]['n'], coef[i]['r']))

        print()
