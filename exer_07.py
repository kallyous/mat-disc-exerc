from exer_06 import mdc_eucli_ext


if __name__ == '__main__':
    print('\n ----- Inverso de  a mod b  -----')
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

        if res != 1:
            print(f'  {a} mod {b}  não tem inverso.')
        else:
            i = len(coef) - 2
            print(f'Um inverso de  {a} mod {b}  é  {coef[i]["m"]}')
