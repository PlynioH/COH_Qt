from Cadastrar_leito import Ui_CadastrarLeito
from Cadastrar_paciente import Ui_CadastrarPaciente
from Taxa_ocupacao import Ui_TaxaOcupacao
from Pagina_principal import Ui_pagPrincipalWindow
from os import SEEK_CUR
import sys
from Login import Ui_MainWindow
from Cadastrar_usuario import Ui_cadUsuarioWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
import requests
import json

class PaginaPrincipal(QMainWindow):
    def toTaxaOcupacao(self):
        self.ctoButton = TaxaOcupacao()
        self.ctoButton.show()
        self.close()
    
    def toCadastrarPaciente(self):
        self.cadasterButton = CadastrarPaciente()
        self.cadasterButton.show()
        self.close()
    
    def toCadastrarLeito(self):
        self.cadLeitoButton = CadastrarLeito()
        self.cadLeitoButton.show()
        self.close()
    
    def toLogin(self):
        self.backLogin = LoginScreen()
        self.backLogin.show()
        self.close()
    
    def Deletar(self):
        x = {"cpf": self.ui.cpf.text(),'quarto': self.ui.quarto.text()}
        r = requests.post('https://cohproject.herokuapp.com/deletar', json = x)
        self.ui.cpf.hide()
        self.ui.nome.hide()
        self.ui.delete_2.hide()
        self.ui.quarto.hide()
    
    def Buscar(self):
        x = {"cpf": self.ui.lineEdit.text()}
        r = requests.post('https://cohproject.herokuapp.com/buscar', json = x)
        self.ui.nome.setText(r.json()['nome'])
        self.ui.cpf.setText(r.json()['cpf'])
        self.ui.quarto.setText(r.json()['quarto'])
        self.ui.delete_2.show()
        self.ui.nome.show()
        self.ui.cpf.show()
        self.ui.quarto.show()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_pagPrincipalWindow()
        self.ui.setupUi(self)
        self.ui.nome.hide()
        self.ui.cpf.hide()
        self.ui.quarto.hide()
        self.ui.delete_2.hide()
        self.show()
        self.ui.delete_2.clicked.connect(lambda: self.Deletar())
        self.ui.endButton.clicked.connect(lambda: self.toLogin())
        self.ui.ctoButton.clicked.connect(lambda: self.toTaxaOcupacao())
        self.ui.cadasterButton.clicked.connect(lambda: self.toCadastrarPaciente())
        self.ui.cadLeitoButton.clicked.connect(lambda: self.toCadastrarLeito())
        self.ui.findButton.clicked.connect(lambda: self.Buscar())
        
        
class CadastrarPaciente(QMainWindow):
    def toPaginaPrincipal(self):
        self.voltarButton = PaginaPrincipal()
        self.voltarButton.show()
        self.close()
        
    def cadastrar(self):
        x = {"quarto": self.ui.nomeQuarto.text(),"nome": self.ui.nameEdit.text() ,"idade": self.ui.ageEdit.text() ,"sexo": self.ui.sexEdit.text(),"tiposanguineo": self.ui.typeSanEdit.text(),"alergiamedicamento": self.ui.alergMedEdit.text() ,"gravidade": self.ui.gravitityEdit.text() ,"telefone": self.ui.phoneNumberEdit.text(),"cpf": self.ui.cpfEdit.text() ,"rg":  self.ui.rgEdit.text() ,"nomemedico": self.ui.medicNameEdit.text() ,"nomepai":  self.ui.dadNameEdit.text() ,"nomemae": self.ui.momNameEdit.text()}
        requests.post('https://cohproject.herokuapp.com/cadastro/paciente', json = x)
        self.toPaginaPrincipal()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CadastrarPaciente()
        self.ui.setupUi(self)
        self.show()
        self.ui.voltarButton.clicked.connect(lambda: self.toPaginaPrincipal())
        self.ui.cadasterButton.clicked.connect(lambda: self.cadastrar())

class CadastrarLeito(QMainWindow):
    def toPaginaPrincipal(self):
        self.goBackButton = PaginaPrincipal()
        self.goBackButton.show()
        self.close()
        
    def cadastrar(self):
        x = {"numeroleito": self.ui.leitoEdit.text(),"numeroequipamento": self.ui.equipEdit.text(),"quarto": self.ui.roomEdit.text() ,"ocupacao": "Livre"}
        requests.post('https://cohproject.herokuapp.com/cadastro/leito', json = x)
        self.toPaginaPrincipal()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CadastrarLeito()
        self.ui.setupUi(self)
        self.show()
        self.ui.goBackButton.clicked.connect(lambda: self.toPaginaPrincipal())
        self.ui.cadasterButton.clicked.connect(lambda: self.cadastrar())
        
class TaxaOcupacao(QMainWindow):
    def toPaginaPrincipal(self):
        self.entrarButton = PaginaPrincipal()
        self.entrarButton.show()
        self.close()
        
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_TaxaOcupacao()
        self.ui.setupUi(self)
        r = requests.get('https://cohproject.herokuapp.com/taxaocupacao')
        r = r.json()
        self.ui.numLeitoEdit.setText(r['nleito'])
        self.ui.numEquipEdit.setText(r['nequipamento'])
        self.ui.numPacientesEdit.setText(r['npaciente'])
        self.ui.numOcupEdit.setText(r['porcentagemocup'])
        self.ui.situacaoEdit.setText(r['situacao'])
        #numEquipEdit, numPacientesEdit, numOcupEdit, situacaoEdit
        self.show()
        self.ui.goBackButton.clicked.connect(lambda: self.toPaginaPrincipal())

class CadastroUsuario(QMainWindow):
    def toLogin(self):
        self.backLogin = LoginScreen()
        self.backLogin.show()
        self.close()
    
    def cadastrar(self):
        x = { "nome": self.ui.nomeEdit.text(), "cpf": self.ui.cpfEdit.text(), "email": self.ui.emailEdit.text(), "numregistro": self.ui.registerEdit.text(), "localtrab": self.ui.trabLocalEdit.text(), "user": self.ui.userEdit.text(), "senha": self.ui.senhaEdit.text()}
        requests.post('https://cohproject.herokuapp.com/cadastro/user', json = x)
        self.toLogin()
    
    def toLogin(self):
        self.goBackButton = LoginScreen()
        self.goBackButton.show()
        self.close()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_cadUsuarioWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.goBackButton.clicked.connect(lambda: self.toLogin())
        self.ui.cadasterButton.clicked.connect(lambda: self.cadastrar())

class LoginScreen(QMainWindow):
    def toCadastroUsuario(self):
        self.cadastrouser = CadastroUsuario()
        self.cadastrouser.show()
        self.close()
    
    def toPaginaPrincipal(self):
        x = {"user": self.ui.login.text(), "pass": self.ui.senha.text()}
        r = requests.post('https://cohproject.herokuapp.com/login', json = x)
        if(r.json()['status']):  
            self.entrarButton = PaginaPrincipal()
            self.entrarButton.show()
            self.close()
        
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.newUserButton.clicked.connect(lambda: self.toCadastroUsuario())
        self.ui.entrarButton.clicked.connect(lambda: self.toPaginaPrincipal())
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginScreen()
    sys.exit(app.exec_())