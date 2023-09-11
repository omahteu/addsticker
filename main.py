from time import sleep

from PIL.Image import new, open
from PIL.ImageDraw import Draw

from barcode import EAN13
from barcode.writer import ImageWriter

from datetime import datetime as dt

from random import randrange

dta = dt.now().strftime("%m%d_%H%M%S%f")

it = ["Volume", "Remetente", "CNPJ", "Endereço", "CEP - Cidade", "Destinatário", "Endereço", "CEP - Cidade", "Contato"]


def main(valores, ean):
    ix = randrange(0, 2000000)
    imagem = new('RGB', (350, 350), 'white')
    desenho = Draw(imagem)

    espaco_vertical_tabela = int(350 * 0.8)
    altura_linha = espaco_vertical_tabela // 9
    largura_coluna = 350 // 2

    for i in range(1, 9 + 1):
        y = i * altura_linha
        desenho.line([(0, y), (350, y)], fill='black')

        if i <= len(it):
            desenho.text((10, y - altura_linha // 2), str(it[i - 1]), fill='black')

        if i <= len(valores):
            x_valor = largura_coluna
            desenho.text((x_valor - 50, y - altura_linha // 2), valores[i - 1], fill='black')

    codigo_barras_x = 350 * 0.5
    codigo_barras_y = 350 * 0.5

    codigo = EAN13(ean, ImageWriter())

    codigo.save(f'./ean/codigo_de_barras{ix}')

    sleep(1)

    imagem_a_colar = open(f'./ean/codigo_de_barras{ix}.png').resize((200, 50))

    codigo.render()

    imagem.paste(imagem_a_colar, (int(codigo_barras_x)-100, int(codigo_barras_y)+120))

    imagem.save(f'./stickers/stricker{dta}{ix}.png')

    sleep(1)
