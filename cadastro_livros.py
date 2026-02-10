'''
Docstring for cadastro_livros
Funcionalidades obrigatórias
Cadastrar livros (título e autor)
Listar todos os livros cadastrados
Buscar livros pelo título
Menu simples:
1 – Cadastrar livro
2 – Listar livros
3 – Buscar livro
0 – Sair
Conceitos praticados
Entrada de dados (input)
Listas
Dicionários ou classes
Estruturas de repetição (while)
Condicionais (if / elif / else)
'''

def menu():
    menu = 0 
while menu !=3:
    print('''
          Menu Princípal
    [1] - Cadastrar Livro. 
    [2] - Listar Livros.
    [3] - Buscar Livro.
    [0] - Sair.
    ''')
    menu = int(input('Qual é sua opção? '))
    if menu == 1:
        livro = list(input('Qual livro deseja cadastrar? '))
        autor = list(input('Qual o autor do livro? '))
    elif menu == 2:
        lista = input('Deseja listar os livros cadastrados?')
        print(livro, autor)
    elif menu == 3:
        busca = input('Qual livro deseja buscar?')
    elif menu == 0:
        quit(print('Você saiu do programa. '))
    else:
        print('Opção inválida.')
print('Você saiu do programa.')

    

    


