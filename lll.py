from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from os import mkdir

var = datetime.now()
var2 = var.strftime('%d_%m_%Y_%H_%M')

# Função para escrever texto na imagem e ajustar para quebrar linhas
def write_text(text, position, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_width, _ = draw.textsize(test_line, font=font)

        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    current_height = position[1]
    for line in lines:
        draw.text((position[0], current_height), line, font=font, fill=(0, 0, 0))
        line_width, line_height = draw.textsize(line, font=font)
        current_height += line_height


# Texto inserido pelo usuário
volume = input("Volume: ")
remetente = input("Remetente: ")
cnpj = input("CNPJ: ")
endereco = input("Endereço: ")
cidade = input("Cidade: ")
destinatario = input("Destinatário: ")
endereco_destinatario = input("Endereço do Destinatário: ")
cidade_destinatario = input("Cidade do Destinatário: ")
contato = input("Contato: ")


for i in range(1, int(volume)+1):
    # Tamanho da imagem
    width, height = 290, 290

    # Criar uma nova imagem
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Fontes
    font = ImageFont.truetype("./Roboto-Light.ttf", 10)

    # Margens e posição inicial para o texto
    margin = 10
    current_position = (margin, margin)

    # Escrever as informações na imagem
    #font = ImageFont.truetype("./Roboto-Light.ttf", 10)
    write_text(f"Volume {i} / {volume} ", current_position, width - 2 * margin)
    current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)
    font = ImageFont.truetype("./Roboto-Light.ttf", 15)

    # REMETENTE
    write_text("Remetente: " + remetente, current_position, width - 2 * margin)
    current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    # CNPJ
    write_text("CNPJ: " + cnpj, current_position, width - 2 * margin)
    current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    if len(endereco) > 17:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Endereço: " + endereco, current_position, width - 2 * 2)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 20)
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
    else:
        write_text("Endereço: " + endereco, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    if len(cidade) > 17:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Cidade/ES: " + cidade, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)
    else:
        write_text("Cidade/ES: " + cidade, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    # DESTINATÁRIO
    if 17 < len(destinatario) < 29:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Destinatário: " + destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 20)
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
    elif len(destinatario) > 30:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Destinatário: " + destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 35)
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
    else:
        write_text("Destinatário: " + destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    # ENDEREÇO DESTINATÁRIO
    if 17 < len(endereco_destinatario) > 29:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Endereço: " + endereco_destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 20)
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
    elif len(endereco_destinatario) > 30:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Endereço: " + endereco_destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 35)
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
    else:
        write_text("Endereço: " + endereco_destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    # CIDADE DESTINATÁRIO
    if len(cidade_destinatario) > 17:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Cidade/ES: " + cidade_destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)
    else:
        write_text("Cidade/ES: " + cidade_destinatario, current_position, width - 2 * margin)
        current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

    # CONTATO
    if len(contato) > 17:
        font = ImageFont.truetype("./Roboto-Light.ttf", 15)
        write_text("Contato: " + contato, current_position, width - 2 * margin)
    else:
        write_text("Contato: " + contato, current_position, width - 2 * margin)

    # Salvar a imagem
    #mkdir(f"./{var2}")
    try:
        image.save(f"./{var2}/stcker{i}.png")
    except FileNotFoundError:
        mkdir(f"./{var2}")
        image.save(f"./{var2}/stcker{i}.png")

    print("Imagem criada com sucesso!")
