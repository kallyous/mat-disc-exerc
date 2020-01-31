import sys
from time import time
from integer_square_root import isqrt
from search import binary_search_find_or_get_next

start_time = 0.0
time_limit = 5.0

output_file_name = 'primes_list.txt'

primes = [2, 3]

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('\nInformar tempo a rodar o programa, em segundos.\nEx:\n    $ python3 exer_02.py 60\n')
        exit(1)

    time_limit = sys.argv[1]
    time_limit = float(time_limit)

    print('Iniciando...')
    print(f'Calculando primos por', time_limit, 'segundos.')
    print(f'Os números primos encontrados serão salvos em', output_file_name)

    delta_time = 0.0
    start_time = time()

    curr_num = 2
    while time_limit > delta_time:
        prime = True
        """Pega raíz inteira mais próxima pela direita da raiz de curr_num.
            A relevância dessa implementação de isqrt() ter complexidade O(log(n))."""
        int_root_over = isqrt(curr_num) + 1
        """Usando busca binária, também de complexidade O(log(n)), achamos o índice onde int_root_over está ou o
            índice do maior mais próximo, caso não conste na lista."""
        iro_index = binary_search_find_or_get_next(primes, -1, len(primes), int_root_over)
        """Vamos efetuar comparações apenas até o valor em iro_index."""
        for p in primes[:iro_index]:
            if curr_num % p == 0:
                prime = False
                break
        if prime:
            primes.append(curr_num)
        curr_num = curr_num + 1
        delta_time = time() - start_time

    for i in range(0, len(primes)):
        primes[i] = str(primes[i])

    primes_found_str = ' '.join(primes)

    with open(output_file_name, 'w') as file:
        file.write(primes_found_str)

    print('Encerrado.')
    print(f'Encontrados', len(primes), 'em', time_limit, 'segundos.')
