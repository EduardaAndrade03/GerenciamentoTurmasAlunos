from tabulate import tabulate

def cadastrar_aluno(alunos):
    id=int(input("Digite o ID do aluno: "))
    nomea=(input("Digite o nome do aluno: "))
    aluno={
        'id':id,
        'nome':nomea
    }
    alunos.append(aluno)
    return alunos

def listar_alunos(alunos):
    return (tabulate(alunos, headers='keys'))

def buscar_aluno_por_id(alunos, id_busca):
    for a in alunos:
        if a['id']==id_busca:
            return tabulate(a)