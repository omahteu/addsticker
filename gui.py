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


def adesivos():
    volume = tela.volume.text()
    remete = tela.remetente.text()
    cnpj = tela.cnpj.text()
    endereco1 = tela.endereco1.text()
    cepcidade1 = tela.cepcidade1.text()
    destinatario = tela.destinatario.text()
    endereco2 = tela.endereco2.text()
    cepcidade2 = tela.cepcidade2.text()
    contato = tela.contato.text()

    sa.append(volume)
    sa.append(remete)
    sa.append(cnpj)
    sa.append(endereco1)
    sa.append(cepcidade1)
    sa.append(destinatario)
    sa.append(endereco2)
    sa.append(cepcidade2)
    sa.append(contato)

    main(sa, gerar_ean13())

    QTimer.singleShot(2000, limpar)


app = QApplication([])
tela = loadUi("./main.ui")
tela.gerar.clicked.connect(adesivos)

tela.show()
app.exec()
