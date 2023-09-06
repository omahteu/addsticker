from random import randint


def gerar_ean13():
    codigo = [randint(0, 9) for _ in range(12)]

    soma_pares = sum(codigo[i] for i in range(0, 12, 2))
    soma_impares = sum(codigo[i] for i in range(1, 12, 2))
    digito_verificacao = (soma_pares * 3 + soma_impares) % 10
    if digito_verificacao != 0:
        digito_verificacao = 10 - digito_verificacao

    codigo.append(digito_verificacao)

    codigo_ean13 = ''.join(map(str, codigo))

    return codigo_ean13
