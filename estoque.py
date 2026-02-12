def estoque():
    produtos_lista = []  # ← Lista única para todos produtos
    proximo_id = 1
    
    opcao = None
    while opcao != 0:
        
        print('''\n=== MENU DE ESTOQUE ===
[1] - Cadastrar produto
[2] - Listar produtos
[3] - Buscar produto
[0] - Sair
        ''')
        
        try:
            opcao = input('Qual é a opção? ').strip()
            opcao = int(opcao)
        except ValueError:
            print('Digite uma opção válida!')
            continue
        
        # CADASTRAR
        if opcao == 1:
            print('\n--- Cadastrar novo produto ---')
            
            nome = input('Nome do produto: ').strip().lower()
            if not nome:
                print('Nome não pode estar vazio!')
                continue
                
            try:
                preco = float(input('Preço: R$ '))
            except ValueError:
                print('Preço inválido!')
                continue
                
            quantidade = input('Quantidade: ').strip()
            if not quantidade:
                quantidade = 0
            else:
                try:
                    quantidade = int(quantidade)
                except ValueError:
                    quantidade = 0
            
            produto = {
                'id': proximo_id,
                'nome': nome,
                'preco': preco,
                'quantidade': quantidade
            }
            
            produtos_lista.append(produto)
            print(f'Produto "{nome}" cadastrado com ID {proximo_id}!')
            proximo_id += 1
        
        # LISTAR
        elif opcao == 2:
            print('\n--- PRODUTOS EM ESTOQUE ---')
            
            if not produtos_lista:
                print('Nenhum produto cadastrado.')
            else:
                for prod in produtos_lista:
                    print(f"ID: {prod['id']} | {prod['nome']} | R$ {prod['preco']:.2f} | Qtd: {prod['quantidade']}")
                print('-' * 40)
        
        # BUSCAR
        elif opcao == 3:
            print('\n--- Buscar produto ---')
            # Implementar depois
        
        elif opcao == 0:
            print('Saindo do sistema...')
        else:
            print('Opção inválida!')

# Chamar função
estoque()