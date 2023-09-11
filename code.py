from random import randint


def gerar_ean13():
    codigo = [randint(0, 9) for _ in range(12)]

    pares = sum(codigo[i] for i in range(0, 12, 2))
    impares = sum(codigo[i] for i in range(1, 12, 2))
    verificacao = (pares * 3 + impares) % 10
    if verificacao != 0:
        verificacao = 10 - verificacao

    codigo.append(verificacao)

    ean13 = ''.join(map(str, codigo))

    return ean13
