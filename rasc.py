import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from os import mkdir

var = datetime.now()
var2 = var.strftime('%d_%m_%Y_%H_%M')




# Função para criar uma imagem com os dados fornecidos
# def create_image(volume, remetente, cnpj_remetente, endereco_remetente, cidade_remetente, destinatario,
#                  endereco_destinatario, cidade_destinatario, contato):
#     # Definir as dimensões da imagem
#     width, height = 800, 600
#     background_color = (255, 255, 255)
#
#     # Criar uma imagem em branco
#     img = Image.new("RGB", (width, height), background_color)
#     draw = ImageDraw.Draw(img)
#
#     # Carregar uma fonte (certifique-se de ter o arquivo de fonte na mesma pasta do script)
#     font = ImageFont.load_default()
#
#     # Escrever os dados na imagem
#     y_position = 50
#     line_height = 25
#
#     data = [
#         f"Volume: {volume}",
#         f"Remetente: {remetente}",
#         f"CNPJ Remetente: {cnpj_remetente}",
#         f"Endereço Remetente: {endereco_remetente}",
#         f"Cidade Remetente: {cidade_remetente}",
#         f"Destinatário: {destinatario}",
#         f"Endereço Destinatário: {endereco_destinatario}",
#         f"Cidade Destinatário: {cidade_destinatario}",
#         f"Contato: {contato}"
#     ]
#
#     for line in data:
#         draw.text((50, y_position), line, fill=(0, 0, 0), font=font)
#         y_position += line_height
#
#     return img


def main():
    st.title("Gerador de Adesivos")

    # Coletar os dados do usuário
    volume = st.text_input("Volume:")
    remetente = st.text_input("Remetente:")
    cnpj = st.text_input("CNPJ Remetente:")
    endereco = st.text_input("Endereço Remetente:")
    cidade = st.text_input("Cidade Remetente:")
    destinatario = st.text_input("Destinatário:")
    endereco_destinatario = st.text_input("Endereço Destinatário:")
    cidade_destinatario = st.text_input("Cidade Destinatário:")
    contato = st.text_input("Contato:")

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

    if st.button("Gerar Imagem"):
        for i in range(1, int(volume) + 1):
            # Tamanho da imagem
            width, height = 350, 350

            # Criar uma nova imagem
            image = Image.new("RGB", (width, height), "white")
            draw = ImageDraw.Draw(image)

            # Fontes
            font = ImageFont.truetype("./Roboto-Light.ttf", 18)

            # Margens e posição inicial para o texto
            margin = 10
            current_position = (margin, margin)

            # Escrever as informações na imagem
            write_text(f"Volume {i} / {volume} ", current_position, width - 2 * margin)
            current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            # REMETENTE
            write_text("Remetente: " + remetente, current_position, width - 2 * margin)
            current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            # CNPJ
            write_text("CNPJ: " + cnpj, current_position, width - 2 * margin)
            current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            if len(endereco) > 17:
                write_text("Endereço: " + endereco, current_position, width - 2 * 2)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 20)
            else:
                write_text("Endereço: " + endereco, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            if len(cidade) > 17:
                write_text("Cidade/ES: " + cidade, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)
            else:
                write_text("Cidade/ES: " + cidade, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            # DESTINATÁRIO
            if 17 < len(destinatario) < 29:
                write_text("Destinatário: " + destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 20)
            elif len(destinatario) > 30:
                write_text("Destinatário: " + destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 35)
            else:
                write_text("Destinatário: " + destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            # ENDEREÇO DESTINATÁRIO
            if 17 < len(endereco_destinatario) > 29:
                write_text("Endereço: " + endereco_destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 20)
            elif len(endereco_destinatario) > 30:
                write_text("Endereço: " + endereco_destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 35)
            else:
                write_text("Endereço: " + endereco_destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            # CIDADE DESTINATÁRIO
            if len(cidade_destinatario) > 17:
                write_text("Cidade/ES: " + cidade_destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)
            else:
                write_text("Cidade/ES: " + cidade_destinatario, current_position, width - 2 * margin)
                current_position = (current_position[0], current_position[1] + font.getsize("Sample")[1] + 5)

            # CONTATO
            if len(contato) > 17:
                write_text("Contato: " + contato, current_position, width - 2 * margin)
            else:
                write_text("Contato: " + contato, current_position, width - 2 * margin)

            # Salvar a imagem
            try:
                image.save(f"./{var2}/stcker{i}.png")
            except FileNotFoundError:
                mkdir(f"./{var2}")
                image.save(f"./{var2}/stcker{i}.png")

            print("Imagem criada com sucesso!")


if __name__ == "__main__":
    main()
