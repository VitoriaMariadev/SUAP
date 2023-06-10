from menus import*
from funcoes import*

dicionario_aluno = pegar_dicionario('alunos')
dicionario_professor = pegar_dicionario('professores')
dicionario_turma = pegar_dicionario('turmas')

while True:
    escolha = menu_principal()
    
    if escolha == '1':
        while True:
            escolha = menu_do_coordenador()

            if escolha == '1':
                adicionar_turma = True
                if len(dicionario_professor) == 0:
                    print('\n---Sem professores cadastrados não é possível criar uma turma---')
                    continue              
                while adicionar_turma:
                    lista_aluno = []
                    dicionario_professor_turma = {}
                    nome = input('\n>>> Digite o nome da turma que deseja adicionar ou [s] para sair: ').title()

                    if nome in 'sS':
                        break

                    if nome in dicionario_turma:
                        print('\n---Turma já existente---')
                        continue

                    procurar_professor = True
                    while procurar_professor:
                        nome_usuario = input('\n>>> Digite o nome do professor que deseja colocar ou [s] para sair: ')

                        if nome_usuario in 'sS':
                            break

                        matricula = pesquisar_usuario(dicionario_professor, nome_usuario, 'adicionar')

                        if matricula == False:
                            continue
                        
                        dicionario_professor_turma[matricula] = dicionario_professor[matricula]

                        while True:
                            nome_usuario = input('\n>>> Digite o nome do aluno que deseja colocar ou [s] para sair: ')

                            if nome_usuario in 'sS':
                                break
                            matricula = pesquisar_usuario(dicionario_aluno, nome_usuario, 'adicionar')

                            if matricula == False:
                                continue
                            
                            dicionario_aluno_turma = {}
                            dicionario_aluno_turma[matricula] = dicionario_aluno[matricula]
                            lista_aluno.append(dicionario_aluno_turma)
                            escolha = input('\n>>> Deseja adicionar outro alunos? [s]im ou [n]ão: ')
                            if escolha in 'sS':
                                continue

                            cadastrar_turmas(dicionario_turma, nome, dicionario_professor_turma, lista_aluno, 'turmas')
                            adicionar_turma = False
                            procurar_professor = False
                            break


            elif escolha == '2':
                if len(dicionario_turma) == 0:
                    print('\n---Não possui turmas cadastradas---')
                else:
                    print('Editar Turma')

            elif escolha == '3':
                if len(dicionario_turma) == 0:
                    print('\n---Não possui turmas cadastradas---')
                else:
                    print('ver Turma')

            elif escolha == '4':
                if len(dicionario_turma) == 0:
                    print('\n---Não possui turmas cadastradas---')
                else:
                    print('apagar Turma')

            elif escolha == '0':
                break

            else:
                print('\n---Escolha Inválida---')
    elif escolha == '2':
        while True:
            escolha = menu_de_professores()

            if escolha == '1':
                while True:
                    nome = input('\n>>> Digite um nome para cadastrar: ')
                    if cadastrar(dicionario_professor, nome, 'professores'):
                        print('\n---Cadastro Efetuado---')
                        break
                    
            elif escolha == '2':
                if len(dicionario_professor) == 0:
                    print('\n---Não possui professores cadastradas---')
                else:
                    atualizar_loop = True
                    while atualizar_loop:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        if nome in 'sS':
                            break
                        else:
                            matricula = pesquisar_usuario(dicionario_professor, nome, 'atualizar')
                            while True:
                                nome = input('\n>>> Digite o novo nome que deseja colocar: ')
                                if tratamento_nome(nome):
                                    tratamento_atualizando_professor(dicionario_turma, dicionario_professor, matricula, nome, 'turmas')
                                    atualizar(dicionario_professor, nome, matricula, 'professores')
                                    atualizar_loop = False
                                    break
                                    
                                print('\n---O nome deve ser composto e não pode conter números---')  
                                continue

            elif escolha == '3':
                if len(dicionario_professor) == 0:
                    print('\n---Não possui professores cadastradas---')
                else:
                    ver_usuario(dicionario_professor, 'Professores')

            elif escolha == '4':
                if len(dicionario_professor) == 0:
                    print('\n---Não possui professores cadastradas---')
                else:
                    while True:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        if nome in 'sS':
                            break
                        else:
                            matricula = pesquisar_usuario(dicionario_professor, nome, 'apagar')
                            apagar(dicionario_professor, matricula, 'professores' )
                            tratamento_apagando_professor(dicionario_turma, matricula, 'turmas')
                            break
            
            elif escolha == '5':
                if len(dicionario_professor) == 0:
                    print('\n---Não possui professores cadastradas---')
                else:
                    while True:
                        nome = input('\n>>> Digite o nome do professor que deseja ver as turmas ou [s] para sair: ')
                        if nome in 'sS':
                            break
                        matricula = pesquisar_usuario(dicionario_professor, nome, 'ver')

                        if matricula == False:
                            continue   

                        checar_professor(dicionario_turma, matricula)

            elif escolha == '6':
                if len(dicionario_professor) == 0:
                    print('\n---Não possui professores cadastradas---')
                else:
                    print('ver alunos')
            
            elif escolha == '0':
                break

    elif escolha == '3':
        while True:
            escolha = menu_de_alunos()

            if escolha == '1':
                while True:
                    nome = input('\n>>> Digite um nome para cadastrar: ')
                    resultado = cadastrar(dicionario_aluno, nome, 'alunos')
                    if cadastrar(dicionario_aluno, nome, 'alunos'):
                        print('\n---Cadastro Efetuado---')
                        break
            
            elif escolha == '2':
                if len(dicionario_aluno) == 0:
                    print('\n---Não possui alunos cadastradas---')
                else:
                    while True:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        if nome in 'sS':
                            break

                        if tratamento_nome(nome):
                            atualizar(dicionario_aluno, pesquisar_usuario(dicionario_aluno, nome, 'atualizar'), 'alunos' )
                            break
                        print('\n--- O nome deve ser composto e não pode conter números---')

            elif escolha == '3':
                if len(dicionario_aluno) == 0:
                    print('\n---Não possui alunos cadastradas---')
                else:
                    ver_usuario(dicionario_aluno, 'Alunos')
            
            elif escolha == '4':
                if len(dicionario_aluno) == 0:
                    print('\n---Não possui alunos cadastradas---')
                else:
                    while True:
                        nome = input('\n>>> Digite o nome que deseja pesquisar ou [s] para sair: ')
                        if nome in 'sS':
                            break
                        else:
                            matricula = pesquisar_usuario(dicionario_aluno, nome, 'apagar')

                            if matricula == False:
                                continue
                            apagar(dicionario_aluno, matricula, 'alunos' )
                            tratamento_apagar_aluno(dicionario_turma, matricula, 'turmas')
                            break

            elif escolha == '0':
                break
    
    elif escolha == '0':
        print('\n---Programa encerrado---')
        break

    else:
        print('\n---Escolha Inválida---')