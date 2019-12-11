from math import sqrt, ceil
from exer_01 import is_prime


# def find_prime_factors(num):
#     factors = []
#     for i in range(2, ceil(sqrt(num))):
#         if num % i == 0:
#             if is_prime(i):
#                 factors.append(i)
#
#     if len(factors) == 0:
#         factors.append(num)
#
#     return factors

def find_prime_factors(num):
    factors = {}
    quotient = num
    divider = 2

    while quotient > 1:
        if quotient % divider == 0:
            if is_prime(divider):
                if divider not in factors:
                    factors[divider] = 0
                factors[divider] = factors[divider] + 1
                quotient = quotient / divider
            else:
                divider = divider + 1
        else:
            divider = divider + 1

    if len(factors) == 0:
        factors[num] = 1

    return factors


if __name__ == '__main__':

    while True:

        print('\nEntre um número para obter seus fatores primos.')
        print('Entre qualquer outra coisa para sair.')
        opt = input('Valor: ')

        if opt.isnumeric():
            num = int(opt)
            num_factors = find_prime_factors(num)
            answer = ''
            for factor in num_factors:
                answer = answer + f' * {factor}^{num_factors[factor]}'
            print('\nFatores primos de', str(num) + ':', answer.strip(' * '))
        else:
            break
