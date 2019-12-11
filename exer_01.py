from integer_square_root import isqrt


def is_prime(num):
    """Checa se número é primo."""
    if num < 2:
        return False
    for n in range(2, isqrt(num)+1):
        if num % n == 0:
            return False
    return True


"""Inicia programa"""
if __name__ == '__main__':

    running = True
    print('Verificar se número inteiro é primo.\n Entre \'Q\' ou \'q\' para encerrar.')

    while running:

        val = input('Número: ')

        if val.lower() == 'q':
            running = False

        elif not val.isnumeric():
            print(val, 'não é número inteiro.')

        else:
            res = is_prime(int(val))
            if res:
                print(val, 'é primo.')
            else:
                print(val, 'não é primo.')

    print('Encerrado.')
