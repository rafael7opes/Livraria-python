print('Sejam bem-vindos à Livraria do Rafael Lopes!')

lista_livro = [] #Criação da lista que vai guardar os livros. Cada livro será um dicionário!
id_global = 0 #Serve para dar um ID único para cada livro! Toda vez que cadastro um livro, esse valor aumenta em 1

def cadastrar_livro(id): #Função que cadastra um novo livro na lista
    print('\n' + '-' * 15, 'MENU CADASTRAR LIVRO', '-' * 24)
    nome = input('Entre com o nome do livro: ')#Pede os dados do livro para o usuário
    autor = input('Entre com o autor do livro: ')
    editora = input('Entre com a editora do livro: ')

    livro = {  #Cria um dicionário com os dados do livro
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    lista_livro.append(livro.copy()) #Copia o dicionário para dentro da lista de livros
    print('Livro cadastrado com sucesso!')

def consultar_livro(): #Função que permite consultar livros cadastrados
    while True:
        print('\n' + '-' * 15, 'MENU CONSULTAR LIVRO', '-' * 24)
        print('1 - Consultar todos os livros')
        print('2 - Consultar por Id')
        print('3 - Consultar livros por Autor')
        print('4 - Retornar ao menu')
        opcao = input('>>')

        if opcao == '1': #Consulta todos os livros
            for livro in lista_livro:
                print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")

        elif opcao == '2': #Consulta por ID
            id_busca = int(input('Digite o ID do livro: '))
            for livro in lista_livro:
                if livro['id'] == id_busca:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")

        elif opcao == '3': #Consulta por nome do autor
            autor_busca = input('Digite o nome do autor: ')
            for livro in lista_livro:
                if livro['autor'] == autor_busca:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")

        elif opcao == '4': #Volta para o menu principal
            break

        else: #Caso digite uma opção inválida
            print('Opção inválida!')

def remover_livro(): #Função para remover um livro pelo ID
    print('\n' + '-' * 15, 'MENU REMOVER LIVRO', '-' * 24)
    while True:
        #Pede o ID do livro que será removido
        id_remover = int(input('Digite o ID do livro a ser removido: '))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')
                return #Sai da função depois de remover
        print('Id inválido')

#Código do MENU PRINCIPAL (main)                    
while True:
    print('\n' + '-' * 15, 'MENU PRINCIPAL', '-' * 28)
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro')
    print('3 - Remover Livro')
    print('4 - Encerrar Programa')
    opcao = input('>>')

    if opcao == '1': #Chama a função de cadastrar e soma 1 ao ID
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2': #Chama a função para consultar livros
        consultar_livro()
    elif opcao == '3':  #Chama a função para remover livro
        remover_livro()
    elif opcao == '4': #Encerra o programa
        print('Encerrando o programa. Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.')
