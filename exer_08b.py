from exer_06 import mdc_eucli_ext

if __name__ == '__main__':
    print('\n ----- Resolução de  ax ≅ b mod m  com  mdc(a,m) = d, com  d|b  ou com a m coprimos. -----')
    while True:
        opt = input('\nEntre \'a b m\', nesta ordem, separados por espaço\n > ')
        args = opt.split()
        if len(args) < 3:
            print('Argumentos insuficientes.')
            continue
        elif not (args[0].isnumeric() and args[1].isnumeric() and args[2].isnumeric()):
            print('Argumentos inválidos.')
            continue

        a = int(args[0])
        b = int(args[1])
        m = int(args[2])

        print(f'  {a}x ≅ {b} mod {m}')

        d, coef = mdc_eucli_ext(a, m)

        print(f'\nMDC de  {a}  e  {m}  é  {d}\n')

        if d == 1:
            i = len(coef) - 2
            x = b * coef[i]['m']
            print(f'  {a}  e  {m}  são coprimos')
            print(f'  O inverso de  {a} mod {m}  é  {coef[i]["m"]}')
            print(f'  A solução geral de  {a}x ≅ {b} mod {m}  será  {x % m} + {m}k'
                  f'  com k sendo um algum número inteiro.')
            print(f'  {x % m}  é a única solução entre  0  e  {m}')
        elif b % d == 0:
            print(f'  {a}  e  {m}  não são coprimos, mas  {d}  divide {b}')

            A = a // d
            B = b // d
            M = m // d
            print(f'  Resolvendo para {A}x ≅ {B} mod {M}...')

            nd, ncoef = mdc_eucli_ext(A, M)
            print(f'  Encontrado mdc({A},{M}) = {nd}')

            ncoef_i = len(ncoef) - 2
            ns = ncoef[ncoef_i]['m']

            if ns < 0:
                print(f'  Normalizando {ns}')
                while ns < 0:
                    ns = ns + M
                print(f'  Normalizado para {ns}')

            sol = []
            for i in range(0, d):
                sol.append(ns + i * M)

            print('  SOLUÇÂO:', sol)

        else:
            print(f'  mdc({a},{m}) = {d}  e {b} não é divisível por {d} .',
                  f'A congruêcia linear  {a}x ≅ {b} mod {m}  não possui solução.')
            # i = len(coef) - 2
            # x = b * coef[i]['m']
            # print(f'  {d}  divide  {b}')
            # print(f'  O inverso de  {a} mod {m}  é  {coef[i]["m"]}')
            # print(f'  A solução geral de  {a}x ≅ {b} mod {m}  será  {x % m} + {m}k'
            #       f'  com k sendo um algum número inteiro.')
            # print(f'  {x % m}  é a única solução entre  0  e  {m}')
