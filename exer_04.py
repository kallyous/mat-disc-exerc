from exer_03 import find_prime_factors

def mdc(a, b):
    """Máximo Divisor Comum"""
    factors_a = find_prime_factors(a)
    factors_b = find_prime_factors(b)

    commom_factors = {}

    """Olhamos para factors_a"""
    for f in factors_a:
        """Se for fator comum, pegamos o de menor potência e guardamos em commom_factors"""
        if f in factors_b:
            if factors_b[f] < factors_a[f]:
                commom_factors[f] = factors_b[f]
            else:
                commom_factors[f] = factors_a[f]

    """Por fim, tiramos o produto dos fatores comuns em suas menores potências e retornamos o resultado"""
    result = 1
    for factor in commom_factors:
        result = result * pow(factor, commom_factors[factor])

    return result


def mmc(a, b):
    """Mínimo Múltiplo Comum"""
    factors_a = find_prime_factors(a)
    factors_b = find_prime_factors(b)

    commom_factors = {}

    """Olhamos para factors_a"""
    for f in factors_a:
        """Se for fator comum, pegamos o de maior potência e guardamos em commom_factors"""
        if f in factors_b:
            if factors_b[f] > factors_a[f]:
                commom_factors[f] = factors_b[f]
            else:
                commom_factors[f] = factors_a[f]
        else:
            """Senão, apenas adicionamos"""
            commom_factors[f] = factors_a[f]

    """Olhamos para factors_b, e incluimos agora os fatores unicos a b em common_factors"""
    for f in factors_b:
        if f not in factors_a:
            commom_factors[f] = factors_b[f]

    """Por fim, tiramos o produto dos fatores comuns em suas maiores potências e retornamos o resultado"""
    result = 1
    for factor in commom_factors:
        result = result * pow(factor, commom_factors[factor])

    return result


if __name__ == '__main__':

    print('Calcula MDC e MMC de dois números. Entre linha em branco para sair.\n')
    print('Máximo Divisor Comum de \'a\' e \'b\':   mdc a b')
    print('Mínimo Múltiplo Comum de \'a\' e \'b\':  mmc a b')

    while True:

        arg_string = input(' >>> ').lower()
        if arg_string == '':
            break

        args = arg_string.split()
        argc = len(args)

        if (argc > 0) and (argc < 3):
            print('Máximo Divisor Comum de \'a\' e \'b\':   mdc a b')
            print('Mínimo Múltiplo Comum de \'a\' e \'b\':  mmc a b')
            print('Sair: entrar linha vazia')
            continue

        if not (args[1].isnumeric() and args[2].isnumeric()):
            print('\n\'a\' e \'b\' devem ser números inteiros.')
            continue

        if args[0] == 'mdc':
            a = int(args[1])
            b = int(args[2])
            res = mdc(a, b)
            print(f'mdc({a},{b}) = {res}')

        elif args[0] == 'mmc':
            a = int(args[1])
            b = int(args[2])
            res = mmc(a, b)
            print(f'mmc({a},{b}) = {res}')
        else:
            print(f'Comando \'{args[0]}\' não é válido.')

    print('\nEncerrado.')
