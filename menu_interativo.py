def menu():
    """Sistema de cadastro de livros"""
    # Lista para armazenar todos os livros
    # Cada livro será um dicionário com 'titulo' e 'autor'
    livros = []
    
    opcao = None  # Variável para controlar o menu
    
    while opcao != 0:  # Continua até o usuário escolher sair (0)
        print('''
        === MENU PRINCIPAL ===
        [1] - Cadastrar Livro
        [2] - Listar Livros
        [3] - Buscar Livro
        [0] - Sair
        ''')
        
        try:
            opcao = int(input('Qual é sua opção? '))
        except ValueError:
            print('Por favor, digite um número válido!')
            continue
        
        # Opção 1: Cadastrar livro
        if opcao == 1:
            print('\n--- CADASTRAR LIVRO ---')
            titulo = input('Título do livro: ').strip()
            autor = input('Autor do livro: ').strip()
            
            if titulo and autor:  # Verifica se não está vazio
                # Cria um dicionário para o livro
                livro = {
                    'titulo': titulo,
                    'autor': autor
                }
                livros.append(livro)  # Adiciona à lista
                print(f'Livro "{titulo}" cadastrado com sucesso!')
            else:
                print('Erro: Título e autor não podem estar vazios!')
        
        # Opção 2: Listar livros
        elif opcao == 2:
            print('\n--- LISTA DE LIVROS ---')
            if len(livros) == 0:
                print('Nenhum livro cadastrado ainda.')
            else:
                for i, livro in enumerate(livros, 1):
                    print(f'{i}. Título: {livro["titulo"]} | Autor: {livro["autor"]}')
        
        # Opção 3: Buscar livro
        elif opcao == 3:
            print('\n--- BUSCAR LIVRO ---')
            if len(livros) == 0:
                print('Nenhum livro cadastrado para buscar.')
            else:
                termo = input('Digite o título (ou parte) para buscar: ').strip().lower()
                encontrados = []
                
                for livro in livros:
                    if termo in livro['titulo'].lower():
                        encontrados.append(livro)
                
                if encontrados:
                    print(f'\n{len(encontrados)} livro(s) encontrado(s):')
                    for i, livro in enumerate(encontrados, 1):
                        print(f'{i}. Título: {livro["titulo"]} | Autor: {livro["autor"]}')
                else:
                    print('Nenhum livro encontrado com esse título.')
        
        # Opção 0: Sair
        elif opcao == 0:
            print('\nVocê saiu do programa. Até mais!')
            break
        
        # Opção inválida
        else:
            print('\nOpção inválida! Digite 0, 1, 2 ou 3.')

# Para executar o programa
if __name__ == "__main__":
    menu()