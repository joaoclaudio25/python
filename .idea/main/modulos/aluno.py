# modulos/aluno.py
from .pessoa import Pessoa  # Import relativo

class Aluno(Pessoa):
    def __init__(self, nome, login, senha, curso):
        super().__init__(nome, login, senha)
        self.__curso = curso

    def consulta_curso(self):
        return self.__curso
