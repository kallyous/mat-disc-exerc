from validation import validate_list_str_num
from exer_06 import mdc_eucli_ext


def tcr(cl):
    """Recebe uma lista de dicts contendo, os 'a m' de congruências no formato x ≅ a mod m.
        Retorna dicionário contendo os elementos da resposta."""

    # Usaremos pra iterar por todas as congruências da lista
    length = len(cl)

    # Trabalharemos em cima de uma cópia dos dados
    ncl = cl.copy()

    # Produto dos m
    m_prod = 1

    # Soma dos produtos AM_M_-1
    amm_1_sum = 0

    # Loop por todas as congruências
    for i in range(0, length):

        # Iniciar M com 1 facilida a multiplicação pelos outros m
        ncl[i]['M'] = 1

        # Com excessão do próprio m, mutiplica incrementalmente M pelos m
        for j in range(0, length):
            if i == j: continue
            ncl[i]['M'] = ncl[i]['M'] * ncl[j]['m']

        # _M_ recebe o resto de M mod m
        ncl[i]['_M_'] = ncl[i]['M'] % ncl[i]['m']

        # Optimizar: Aqui deve ser aplicado euclides para obter _M_-1 em O(log n)
        s = 1
        a = ncl[i]['_M_']
        m = ncl[i]['m']
        while ((s * a) % m) != 1:
            s = s + 1

        # Pronto, inversa encontrada e definida
        ncl[i]['s'] = s

        # Produto que será somado pra se tirar o módulo contra o produto dos m
        ncl[i]['AM_M_-1'] = ncl[i]['a'] * ncl[i]['M'] * ncl[i]['s']

        # Incrementa produto dos m
        m_prod = m_prod * ncl[i]['m']

        # Incrementa soma dos AM_M_-1
        amm_1_sum = amm_1_sum + ncl[i]['AM_M_-1']

    x = amm_1_sum % m_prod
    return x, m_prod, ncl


if __name__ == '__main__':
    print('\n ----- Teorema Chinês do Resto com três congruências -----\n')

    while True:
        # data = [
        #     {'a': 5, 'm': 7},
        #     {'a': 4, 'm': 9},
        #     {'a': 1, 'm': 10}
        # ]
        #
        # x, mp, full_data = tcr(data)
        # print(f'  O número tem formato  {x} + {mp}*k  com números inteiros k')

        args_a = validate_list_str_num(
            input('\nEntre \'a m\' da primeira congruência\n > ').split(), 2)
        if len(args_a) == 0:
            continue

        args_b = validate_list_str_num(
            input('\nEntre \'a m\' da segunda congruência\n > ').split(), 2)
        if len(args_b) == 0:
            continue

        args_c = validate_list_str_num(
            input('\nEntre \'a m\' da terceira congruência\n > ').split(), 2)
        if len(args_c) == 0:
            continue

        data = []
        data.append({'a': args_a[0], 'm': args_a[1]})
        data.append({'a': args_b[0], 'm': args_b[1]})
        data.append({'a': args_c[0], 'm': args_c[1]})

        # Verificaçao de coprimos
        run = True
        for i in range(0, len(data)):
            for j in range(0, len(data)):
                if i == j: continue
                res, coef = mdc_eucli_ext(data[i]['m'], data[j]['m'])
                if res != 1:
                    run = False

        if run:
            r, m_prod, full_data = tcr(data)
            print(f'\n  O número tem formato  {r} + {m_prod}*k  para números inteiros k\n')
        else:
            print(f'\nValores {data[i]["m"]} e {data[j]["m"]} não são coprimos.'
                  f' Abortando TCR...\n')