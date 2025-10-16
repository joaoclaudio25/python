# main.py
from modulos.pessoa import Pessoa
from modulos.aluno import Aluno
from modulos.professor import Professor

# Instâncias
pessoa1 = Pessoa('Maria', 'mary', 'm123')
print(pessoa1.consulta_nome())

aluna1 = Aluno('Viviane', 'vivi', 'v123', 'Informática')
print(aluna1.consulta_nome())
print(aluna1.consulta_curso())

prof1 = Professor('Tatiana', 'tati', 't123', 'Doutorado')
print(prof1.consulta_nome() + prof1.consulta_titulacao())
