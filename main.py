from time import sleep

from PIL.Image import new, open
from PIL.ImageDraw import Draw

from barcode import EAN13
from barcode.writer import ImageWriter

it = ["Volume", "Remetente", "CNPJ", "Endereço", "CEP - Cidade", "Destinatário", "Endereço", "CEP - Cidade", "Contato"]


def main(valores, ean):

    # Criar uma nova imagem
    imagem = new('RGB', (350, 350), 'white')
    desenho = Draw(imagem)

    # Configurações da tabela
    espaco_vertical_tabela = int(350 * 0.8)
    altura_linha = espaco_vertical_tabela // 9
    largura_coluna = 350 // 2

    # Desenhar a tabela e preencher com itens e valores
    for i in range(1, 9 + 1):
        y = i * altura_linha
        desenho.line([(0, y), (350, y)], fill='black')

        if i <= len(it):
            desenho.text((10, y - altura_linha // 2), str(it[i - 1]), fill='black')

        if i <= len(valores):
            x_valor = largura_coluna
            desenho.text((x_valor - 50, y - altura_linha // 2), valores[i - 1], fill='black')

    # Dividir o restante dos 20% do espaço para o código de barras
    codigo_barras_x = 350 * 0.5
    codigo_barras_y = 350 * 0.5

    # Gerar o código de barras
    codigo = EAN13(ean, ImageWriter())

    codigo.save('codigo_de_barras')

    sleep(1.5)

    imagem_a_colar = open('codigo_de_barras.png').resize((200, 50))

    codigo.render()

    # Colocar o código de barras na imagem
    imagem.paste(imagem_a_colar, (int(codigo_barras_x)-100, int(codigo_barras_y)+120))

    # Salvar a imagem
    imagem.save('imagemrc.png')
