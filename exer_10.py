from validation import validate_list_str_num
from exer_06 import mdc_eucli_ext
from exer_09 import tcr

if __name__ == '__main__':
    print('\n ----- Teorema Chinês do Resto com N congruências -----\n')

    while True:

        # Solicita quantas congruências serão tratadas
        n = validate_list_str_num(
            input('Quantas congruências serão fornecidas?\n > ').split(), 1)
        if len(n) == 0:
            continue
        else:
            n = n[0]

        # Prepara lista a segurar entrada
        data = []

        # Flag de controle
        run = True

        # Recebe toda a entrada
        for i in range(1, n + 1):
            args = validate_list_str_num(
                input(f'\nEntre \'a m\' da {i}ª congruência\n > ').split(), 2)
            if len(args) == 0:
                run = False
                break
            data.append({'a': args[0], 'm': args[1]})

        # Verificaçao de coprimos
        i: int
        j: int
        for i in range(0, len(data)):
            for j in range(0, len(data)):
                if i == j: continue
                res, coef = mdc_eucli_ext(data[i]['m'], data[j]['m'])
                if res != 1:
                    run = False
                    break
            if not run:
                break

        if run:
            r, m_prod, full_data = tcr(data)
            print(f'\n  O número tem formato  {r} + {m_prod}*k  para números inteiros k\n')
        else:
            print(f'\nValores {data[i]["m"]} e {data[j]["m"]} não são coprimos.'
                  f' Abortando TCR...\n')

        print()
