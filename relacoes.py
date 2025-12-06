from tabulate import tabulate

def adicionar_aluno_na_turma(turmas, alunos, relacoes):
    ida=int(input("Digite o ID do aluno: "))
    idt=int(input("Digite o ID da turma: "))
    
    aencontrado=False
    tencontrada=False

    for a in alunos:
        if a['id']==ida:
            aencontrado=True
    for t in turmas:
        if t['id']==idt:
            tencontrada=True

    if aencontrado and tencontrada:
        print("Deu crt")
        relacao={
            'id_aluno':ida,
            'id_turma':idt
        }
        relacoes.append(relacao)
        return relacoes
    else:
        return 'Algo deu errado'

def listar_alunos_da_turma(relacoes, alunos):
    idt=int(input("digite o id da turma: "))
    alunosturma=[]
    idas=[]
    for r in relacoes:
        if idt==r['id_turma']:
            idas.append(r['id_aluno'])
    for  a in alunos:
        if a['id'] in idas:
            alunosturma.append(a['nome'])
    return (alunosturma)
    

def remover_aluno_da_turma(relacoes):
    ida=int(input("Digite o ID do aluno: "))
    idt=int(input("Digite o ID da turma: "))

    for r in relacoes:
        if ida==r['id_aluno'] and idt==r['id_turma']:
            relacoes.remove(r)
            return relacoes
    return "houve algum erro"