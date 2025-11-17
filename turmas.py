# crir_turm(turms)
# Pede nome da turma e adiciona:
# { "id": 1,
# "nome": "1o Ano A" }
# ID gerado automaticamente (use a função random)

from tabulate import tabulate
import random

def criar_turma(turmas):
    nomet=(input("Digite qual é a turma"))
    id = random.randint(1,21)
    turma ={
        'id':id,
        'nome':nomet
    }
    turmas.append(turma)
    return turmas

def listar_turmas(turmas):
    return (print(tabulate(turmas)))

def buscar_turma_por_id(turmas, id_busca):
    for t in turmas:
        if t['id']==id_busca:
            return (tabulate(t))
    return "houve algum erro"