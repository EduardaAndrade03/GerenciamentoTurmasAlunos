from turmas import *
from alunos import *

turmas=[]
alunos=[]

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

    elif op==4:
        print()
        print(listar_alunos(alunos))
        print()

    elif op==5:
        print()
        print(listar_turmas(turmas))
        print()

    elif op==5:
        print("Saindo...")
        break

    else:
        print("escolhe direito")
