from exer_06 import mdc_eucli_ext

if __name__ == '__main__':
    print('\n ----- Resolução de  ax ≅ b mod m  com  mdc(a,m) = 1  (a m coprimos) -----')
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

        res, coef = mdc_eucli_ext(a, m)

        print(f'\nMDC de  {a}  e  {m}  é  {res}\n')

        if res != 1:
            print(f'  {a} {m}  não são coprimos.')
        else:
            i = len(coef) - 2
            x = b * coef[i]['m']
            print(f'  {a}  e  {m}  são coprimos')
            print(f'  O inverso de  {a} mod {m} = 1  é  {coef[i]["m"]}')
            print(
                f'  A solução geral de  {a}x ≅ {b} mod {m}  será  {x % m} + {m}k  com k sendo um algum número inteiro.')
            print(f'  {x % m}  é a única solução entre  0  e  {m}')
