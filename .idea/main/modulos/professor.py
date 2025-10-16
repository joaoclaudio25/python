# modulos/professor.py
from .pessoa import Pessoa  # Import relativo

class Professor(Pessoa):
    def __init__(self, nome, login, senha, titulacao):
        super().__init__(nome, login, senha)
        self.__titulacao = titulacao

    def consulta_titulacao(self):
        return self.__titulacao
