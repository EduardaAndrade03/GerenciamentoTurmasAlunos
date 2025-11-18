from tabulate import tabulate
import random

def criar_turma(turmas):
    nomet=(input("Digite qual é a turma: "))
    id = random.randint(1,21)
    turma ={
        'id':id,
        'nome':nomet
    }
    turmas.append(turma)
    return turmas

def listar_turmas(turmas):
    return (tabulate(turmas, headers='keys'))

def buscar_turma_por_id(turmas, id_busca):
    for t in turmas:
        if t['id']==id_busca:
            return (tabulate(t))
    return "houve algum erro"