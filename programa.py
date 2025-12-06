from turmas import *
from alunos import *
from relacoes import *

turmas=[]
alunos=[]
relacoes=[]

print('''
    1 - Criar turma
    2 - Cadastrar aluno
    3 - Adicionar aluno à turma
    4 - Listar turmas
    5 - Listar alunos
    6 - Listar alunos de uma turma
    7 - Remover aluno da turma
    0 - Sair
        ''')

while True:
    
    op=int(input("Digite sua escolha: "))


    if op==1:
        print()
        criar_turma(turmas)
        print()

    elif op==2:
        print()
        cadastrar_aluno(alunos)
        print()

    elif op==3:
        print()
        adicionar_aluno_na_turma(turmas, alunos, relacoes)
        print()

    elif op==4:
        print()
        print(listar_turmas(turmas))
        print()

    elif op==5:
        print()
        print(listar_alunos(alunos))
        print()

    elif op==6:
        print()
        print(listar_alunos_da_turma(relacoes, alunos))
        print()
    
    elif op==7:
        print()
        remover_aluno_da_turma(relacoes)
        print()

    elif op==0:
        print("Saindo...")
        break

    else:
        print("escolhe direito")
