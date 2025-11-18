from tabulate import tabulate

def adicionar_aluno_na_turma(turmas, alunos, relacoes):
    ida=int(input("Digite o ID do aluno: "))
    idt=int(input("Digite o ID da turma: "))
    
    if ida in alunos['id'] and idt in turmas['id']:
        print("Deu crt")

        relacao={
            'id_aluno':ida,
            'id_turma':idt
        }
        relacoes.append(relacao)
        return relacoes

    else:
        return 'Algo deu errado'

def listar_alunos_da_turma(relacoes, alunos, turmas):
    alunosturma=[]
    idt=int(input("Digite o ID da turma: "))

    for r in relacoes:
        if r['id_turma']==idt:
            alunosturma.append(r['id_aluno'])
    return (tabulate(alunosturma))

def remover_aluno_da_turma(relacoes):
    ida=int(input("Digite o ID do aluno: "))
    idt=int(input("Digite o ID da turma: "))

    for r in relacoes:
        if ida==r['id_turma'] and idt==r['id_turma']:
            relacoes.remove(r)
            return relacoes
    return "houve algum erro"