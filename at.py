# Definir o estoque inicial como string
estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
produtos = []

# Função para tranformar a string do estoque inicial em uma lista de dicionario
def carregar_estoque_inicial(estoque_str):
    items = estoque_str.split("#")  
    # Separar produto por marcação #
    for item in items:
        descricao, id, qnt, custo, preco_venda = item.split(";") 
        produto = {
            "descricao": descricao,
            "codigo": int(id),
            "quantidade": int(qnt),
            "custo": float(custo),
            "preco_venda": float(preco_venda)
        }
        produtos.append(produto)
    return produtos

# Função para cadastrar um novo produto
def cadastrar_produto(produtos):
    print("***Cadastro de Novo Produto***")
    descricao = input("Descrição: ")
    id = int(input("Código (único): "))

    # Verificar se o código já existe
    for produto in produtos:
        if produto["codigo"] == id:
            print("Erro: Código já existente. Tente novamente.")
            return

    quantidade = int(input("Quantidade em estoque: "))
    custo = float(input("Custo do item: "))
    preco_venda = float(input("Preço de venda por item: "))
    
    novo_produto = {
        "descricao": descricao,
        "codigo": id,
        "quantidade": quantidade,
        "custo": custo,
        "preco_venda": preco_venda
    }
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso!")

# Função para listar todos os produto 
def listar_produtos(produtos):
    print("\n***Lista de Produtos Cadastrados***")

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    for produto in produtos:
        print(f"Descrição: {produto['descricao']}")
        print(f"Código: {produto['codigo']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Custo: R${produto['custo']:.2f}")
        print(f"Preço de Venda: R${produto['preco_venda']:.2f}")
        print("-" * 30)  # Linha separadora entre produtos

# Função para ordenar  os produto 
def ordenar_produtos_por_quantidade(produtos, ordem="crescente"):
    print("\n***Produtos Ordenados por Quantidade***")

    if not produtos:  # Verifica se a lista está vazia
        print("Não há produtos cadastrados.")
        return

    # Ordena a lista com base na quantidade
    produtos_ordenados = sorted(
        produtos,
        key=lambda x: x['quantidade'],  # Ordena por 'quantidade'
        reverse=(ordem == "decrescente")  # Define a ordem com base na escolha
    )

    # Exibe a lista ordenada
    for produto in produtos_ordenados:
        print(f"Descrição: {produto['descricao']}")
        print(f"Código: {produto['codigo']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Custo: R${produto['custo']:.2f}")
        print(f"Preço de Venda: R${produto['preco_venda']:.2f}")
        print("-" * 30)  

# Função para buscar os produto por codigo
def buscar_produtos(produtos, codigo):
    print(f"\n***Busca de Produto por Código: {codigo}***")
    encontrados = [produto for produto in produtos if produto["codigo"] == codigo]
    
    if not encontrados:  # Se a lista estiver vazia
        print("Nenhum produto encontrado com esse código.")
    else:
        for produto in encontrados:
            print(f"Descrição: {produto['descricao']}")
            print(f"Código: {produto['codigo']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Custo: R${produto['custo']:.2f}")
            print(f"Preço de Venda: R${produto['preco_venda']:.2f}")
            print("-" * 30)

# Função para remover os produto por codigo
def remover_produto(produtos, codigo):
    print(f"\n***Remoção de Produto por Código: {codigo}***")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print(f"Produto '{produto['descricao']}' com código {codigo} foi removido com sucesso.")
            return
    print("Nenhum produto encontrado com esse código. Nenhuma ação realizada.")

# Função para consultar os produto esgotados
def consultar_produtos_esgotados(produtos):
    print("\n***Consulta de Produtos Esgotados***")
    produtos_esgotados = [produto for produto in produtos if produto["quantidade"] == 0]
    
    if not produtos_esgotados:
        print("Nenhum produto esgotado no momento.")
    else:
        for produto in produtos_esgotados:
            print(f"Descrição: {produto['descricao']}")
            print(f"Código: {produto['codigo']}")
            print(f"Custo: R${produto['custo']:.2f}")
            print(f"Preço de Venda: R${produto['preco_venda']:.2f}")
            print("-" * 30)

# Função para filtrar os produto com baixa qnt
def filtrar_produtos_baixa_quantidade(produtos, limite_minimo):
    print(f"\n ***Produtos com Quantidade Abaixo de {limite_minimo}***")
    produtos_filtrados = [produto for produto in produtos if produto["quantidade"] < limite_minimo]
    
    if not produtos_filtrados:  # Se não houver produtos filtrados
        print("Nenhum produto encontrado com quantidade abaixo do limite.")
    else:
        for produto in produtos_filtrados:
            print(f"Descrição: {produto['descricao']}")
            print(f"Código: {produto['codigo']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Custo: R${produto['custo']:.2f}")
            print(f"Preço de Venda: R${produto['preco_venda']:.2f}")
            print("-" * 30)

# Função para update os preço de venda
def atualizar_preco_venda(produtos, codigo, novo_preco):
    print(f"\n***Atualização de Preço para o Produto com Código: {codigo}***")
    
    for produto in produtos:
        if produto["codigo"] == codigo:  # Verifica se o codigo é corresponde ao produto
            produto["preco_venda"] = novo_preco  # Atuliza o preço de venda
            print(f"Preço atualizado com sucesso!")
            print(f"Novo preço de venda do produto '{produto['descricao']}': R${produto['preco_venda']:.2f}")
            return 

    print("Nenhum produto encontrado com esse código.")  # Se o codigo não for encontrado

estoque = carregar_estoque_inicial(estoque_inicial)

while True:
    print("\n ***Sistema de Gerenciamento de Estoque***")
    print("1. Listar Produto")
    print("2. Cadastrar Novo Produto")
    print("3. Ordenar Produtos por Quantidade")
    print("4. Buscar Produto por Código")
    print("5. Remover Produto")
    print("6. Consultar Produtos Esgotados")
    print("7. Filtrar Produtos com Baixa Quantidade")
    print("9. Atualizar Preço de Venda")
    print("10. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":

        listar_produtos(estoque)
    elif opcao == "2":

        cadastrar_produto(estoque)
    elif opcao == "3":

        print("\nEscolha a ordem de exibição:")
        print("1. Crescente")
        print("2. Decrescente")

        ordem_opcao = input("Opção: ")
        if ordem_opcao == "1":
            ordenar_produtos_por_quantidade(estoque, ordem="crescente")
        elif ordem_opcao == "2":
            ordenar_produtos_por_quantidade(estoque, ordem="decrescente")
        else:
            print("Opção inválida.")
    elif opcao == "4":

        try:
            codigo = int(input("Digite o código do produto: "))
            buscar_produtos(produtos=estoque, codigo=codigo)
        except ValueError:
            print("Código inválido. Digite um número inteiro.")
    elif opcao == "5":

        try:
            codigo = int(input("Digite o código do produto a ser removido: "))
            remover_produto(produtos=estoque, codigo=codigo)
        except ValueError:
            print("Código inválido. Digite um número inteiro.")

    elif opcao == "6":
        consultar_produtos_esgotados(estoque)

    elif opcao == "7":
        try:
            limite_minimo = int(input("Digite o limite mínimo de quantidade: "))
            filtrar_produtos_baixa_quantidade(produtos=estoque, limite_minimo=limite_minimo)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")    

    elif opcao == "9":
        try:
            codigo = int(input("Digite o codigo do produto: "))
            novo_preco = float(input("Digite o novo preço de venda: "))
            atualizar_preco_venda(produtos=estoque, codigo=codigo, novo_preco=novo_preco)
        except ValueError:
            print("Valor inválido. Digite valores numéricos para código e preço.")    
            
    elif opcao == "10":
        print("Saindo. Vlwww!")
        break
    else:
        print("Opção inválida. Tente novamente.")
    