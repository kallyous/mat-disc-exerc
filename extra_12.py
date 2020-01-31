from extra_11 import p2_exp_mod


def exp_mod(a, k, m):
    # Gera string com representação binária do valor de k.
    binary_k = f'{k:b}'
    # Pega contagem de bits.
    bitcount = len(binary_k)

    # Prepara variável para segurar as multiplicações.
    A = 1

    # Passa de bit em bit,
    for i in range(0, bitcount):
        # Checa se bit é 1, pois não nos interessa os 0.
        if binary_k[i] == '1':
            # Calcula a potência a elevar o 2, baseado na casa do bit.
            p = bitcount - 1 - i
            # Chama recursão que calcula exponenciação modular para potêcnias de 2 para o bit atual e incrementa A.
            A *= p2_exp_mod(a, 2 ** p, m)

    # Tira o módulo de A e o retorna.
    return A % m



if __name__ == '__main__':
    print('\n ----- Exponenciação Modular Rápida para Qualquer Número -----\n')
    a, k, m = input('Entre três números  a k m  separados por espaços, para calcular  a^k mod m  .\n > ').split()

    a = int(a)
    k = int(k)
    m = int(m)

    res = exp_mod(a, k, m)
    print(f'\n{a}^{k} mod {m} = {res}')
