# modulos/pessoa.py
class Pessoa:
    def __init__(self, nome, login, senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    def consulta_nome(self):
        return self.__nome
