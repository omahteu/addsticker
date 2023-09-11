from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from main import main
from code import gerar_ean13
from PyQt5.QtCore import QTimer

sa = []


def limpar():
    tela.volume.clear()
    tela.remetente.clear()
    tela.cnpj.clear()
    tela.endereco1.clear()
    tela.cepcidade1.clear()
    tela.destinatario.clear()
    tela.endereco2.clear()
    tela.cepcidade2.clear()
    tela.contato.clear()
    tela.label.setText("Máximo de 40 caracteres")


def adesivos():
    dados = {"volume": tela.volume.text(), 'remete': tela.remetente.text(), 'cnpj': tela.cnpj.text(),
             'endereco1': tela.endereco1.text(), 'cepcidade1': tela.cepcidade1.text(),
             'destinatario': tela.destinatario.text(), 'endereco2': tela.endereco2.text(),
             'cepcidade2': tela.cepcidade2.text(), 'contato': tela.contato.text()}
    if len(dados['volume']) <= 40:
        pass
        if len(dados['remete']) <= 40:
            pass
            if len(dados['cnpj']) <= 40:
                pass
                if len(dados['endereco1']) <= 40:
                    pass
                    if len(dados['cepcidade1']) <= 40:
                        pass
                        if len(dados['destinatario']) <= 40:
                            pass
                            if len(dados['endereco2']) <= 40:
                                pass
                                if len(dados['cepcidade2']) <= 40:
                                    pass
                                    if len(dados['contato']) <= 40:
                                        for x in range(1, int(dados['volume'])+1):
                                            sa.append(f'{x}/{dados["volume"]}')
                                            sa.append(dados['remete'])
                                            sa.append(dados['cnpj'])
                                            sa.append(dados['endereco1'])
                                            sa.append(dados['cepcidade1'])
                                            sa.append(dados['destinatario'])
                                            sa.append(dados['endereco2'])
                                            sa.append(dados['cepcidade2'])
                                            sa.append(dados['contato'])
                                            main(sa, gerar_ean13())
                                            sa.clear()
                                    else:
                                        tela.label.setText("Campo contato destinatário com mais de 40 caracteres.")
                                else:
                                    tela.label.setText("Campo cidade - cep destinatário com mais de 40 caracteres.")
                            else:
                                tela.label.setText("Campo endereço destinatário com mais de 40 caracteres.")
                        else:
                            tela.label.setText("Campo destinatário com mais de 40 caracteres.")
                    else:
                        tela.label.setText(f"Campo cidade - cep remetente com mais de 40 caracteres.")
                else:
                    tela.label.setText(f"Campo endereço remetente com mais de 40 caracteres.")
            else:
                tela.label.setText(f"Campo cnpj com mais de 40 caracteres.")
        else:
            tela.label.setText(f"Campo remetente com mais de 40 caracteres.")
    else:
        tela.label.setText(f"Campo volume com mais de 40 caracteres.")

    QTimer.singleShot(2000, limpar)


app = QApplication([])
tela = loadUi("./main.ui")
tela.gerar.clicked.connect(adesivos)
tela.show()
app.exec()
