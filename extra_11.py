
def p2_exp_mod(a, k, m):
    """Calcula  a^k mod m  onde k é potência de 2.
    :param a: Valor da base.
    :param k: Potência de 2.
    :param m: Valor para o qual calcular módulo.
    :return: (a^k) mod m
    """
    if k <= 2:
        return a**k % m
    else:
        return (p2_exp_mod(a, k//2, m) * p2_exp_mod(a, k//2, m)) % m

if __name__ == '__main__':
    print('\n ----- Exponenciação Modular Rápida para Potência de 2 -----\n')
    a, k, m = input('Entre três números a k m, para calcular a^k mod m, separados por espaço, '''
                    'onde k é potência de 2.\n > ').split()
    a = int(a)
    k = int(k)
    m = int(m)

    bin_str = f'{k:b}'
    print(f'{a}^{k} mod {m} = {p2_exp_mod(a,k,m)}')
