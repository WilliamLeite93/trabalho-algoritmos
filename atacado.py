from collections import defaultdict, deque

dados_mercado = {
  "nome_mercado": "Macro Atacado",
  "conexoes": [
    {"origem": "Entrada", "destino": "Corredor_1_Frente", "passos": 5},
    {"origem": "Saida_Caixas", "destino": "Corredor_6_Frente", "passos": 5},
    {"origem": "Corredor_6_Frente", "destino": "Frios", "passos": 8},
    {"origem": "Corredor_6_Fundo", "destino": "Acougue", "passos": 8},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_1_Frente", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_2_Frente", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_3_Frente", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_4_Frente", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_5_Frente", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_6_Frente", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_1_Fundo", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_2_Fundo", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_3_Fundo", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_4_Fundo", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_5_Fundo", "passos": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_6_Fundo", "passos": 15},
    {"origem": "Corredor_1_Fundo", "destino": "Via_Fundos_Dir", "passos": 20},
    {"origem": "Corredor_2_Fundo", "destino": "Via_Fundos_Dir", "passos": 15},
    {"origem": "Corredor_3_Fundo", "destino": "Via_Fundos_Centro", "passos": 15},
    {"origem": "Corredor_4_Fundo", "destino": "Via_Fundos_Centro", "passos": 15},
    {"origem": "Corredor_5_Fundo", "destino": "Via_Fundos_Esq", "passos": 15},
    {"origem": "Corredor_6_Fundo", "destino": "Via_Fundos_Esq", "passos": 20},
    {"origem": "Via_Fundos_Esq", "destino": "Hortifruti", "passos": 5},
    {"origem": "Via_Fundos_Centro", "destino": "Congelados", "passos": 5},
    {"origem": "Via_Fundos_Dir", "destino": "Via_Fundos_Centro", "passos": 25},
    {"origem": "Via_Fundos_Centro", "destino": "Via_Fundos_Esq", "passos": 25}
  ],
  "produtos_por_secao": {
    "Corredor_1_Frente": ["Arroz", "Feijão", "Óleo"],
    "Corredor_1_Fundo": ["Açúcar", "Farinha", "Sal"],
    "Corredor_2_Frente": ["Macarrão", "Molho de Tomate", "Enlatados"],
    "Corredor_2_Fundo": ["Biscoito", "Salgadinho", "Chocolates"],
    "Corredor_3_Frente": ["Café", "Leite em Pó", "Achocolatado"],
    "Corredor_3_Fundo": ["Chá", "Cereais", "Mel"],
    "Corredor_4_Frente": ["Sabão em Pó", "Amaciante", "Detergente"],
    "Corredor_4_Fundo": ["Desinfetante", "Esponja", "Vassoura"],
    "Corredor_5_Frente": ["Shampoo", "Sabonete", "Desodorante"],
    "Corredor_5_Fundo": ["Creme Dental", "Papel Higiênico", "Fraldas"],
    "Corredor_6_Frente": ["Ração Cão", "Ração Gato", "Petshop"],
    "Corredor_6_Fundo": ["Bazar", "Lâmpadas", "Ferramentas"],
    "Via_Fundos_Dir": ["Cerveja", "Refrigerante", "Suco", "Água"],
    "Congelados": ["Pizza Congelada", "Hambúrguer", "Sorvete", "Batata Frita Congelada"],
    "Hortifruti": ["Banana", "Batata", "Tomate", "Cebola"],
    "Acougue": ["Carne Moída", "Frango", "Costela", "Linguiça"],
    "Frios": ["Queijo", "Presunto", "Iogurte", "Manteiga"],
    "Saida_Caixas": ["Chiclete", "Pilha"]
  }
}

prod_secao = {}
for secao, produtos in dados_mercado["produtos_por_secao"].items():
    for produto in produtos:
        prod_secao[produto] = secao

grafo = defaultdict(dict)
for conexao in dados_mercado["conexoes"]:
    origem = conexao["origem"]
    destino = conexao["destino"]
    passos = conexao["passos"]
    grafo[origem][destino] = passos
    grafo[destino][origem] = passos

def busca_bfs(grafo, origem, destino):
    fila = deque([(origem, [origem])])
    visitados = set([origem])
    while fila:
        no_atual, caminho = fila.popleft()
        if no_atual == destino:
            passos_total = sum(grafo[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))
            return passos_total, caminho
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    return 0, []

def busca_dfs(grafo, origem, destino):
    pilha = [(origem, [origem])]
    visitados = set()
    while pilha:
        no_atual, caminho = pilha.pop()
        if no_atual == destino:
            passos_total = sum(grafo[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))
            return passos_total, caminho
        if no_atual not in visitados:
            visitados.add(no_atual)
            for vizinho in grafo[no_atual]:
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))
    return 0, []

def rota_bfs_lista(lista_compras, grafo, prod_secao):
    """BFS: respeita a ordem da lista, conecta cada seção à próxima."""
    secoes = list(dict.fromkeys(
        prod_secao[item] for item in lista_compras if item in prod_secao
    ))
    paradas = ["Entrada"] + secoes
    passos_total = 0
    rota_completa = ["Entrada"]
    for i in range(len(paradas) - 1):
        p, caminho = busca_bfs(grafo, paradas[i], paradas[i+1])
        passos_total += p
        rota_completa.extend(caminho[1:])
    return passos_total, rota_completa

def rota_dfs_lista(lista_compras, grafo, prod_secao):
    """DFS: respeita a ordem da lista, conecta cada seção à próxima."""
    secoes = list(dict.fromkeys(
        prod_secao[item] for item in lista_compras if item in prod_secao
    ))
    paradas = ["Entrada"] + secoes
    passos_total = 0
    rota_completa = ["Entrada"]
    for i in range(len(paradas) - 1):
        p, caminho = busca_dfs(grafo, paradas[i], paradas[i+1])
        passos_total += p
        rota_completa.extend(caminho[1:])
    return passos_total, rota_completa


def rota_gulosa_lista(lista_compras, grafo, prod_secao):
    """Gulosa: a cada passo escolhe a seção mais próxima entre as pendentes."""
    secoes_pendentes = list(dict.fromkeys(
        prod_secao[item] for item in lista_compras if item in prod_secao
    ))
    if not secoes_pendentes:
        return 0, []
    local_atual = "Entrada"
    passos_total = 0
    rota_completa = ["Entrada"]
    while secoes_pendentes:
        menor_passos = float('inf')
        proxima_secao = None
        melhor_caminho = []
        for secao in secoes_pendentes:
            p, caminho = busca_bfs(grafo, local_atual, secao)
            if p < menor_passos:
                menor_passos = p
                proxima_secao = secao
                melhor_caminho = caminho
        passos_total += menor_passos
        rota_completa.extend(melhor_caminho[1:])
        local_atual = proxima_secao
        secoes_pendentes.remove(proxima_secao)
    return passos_total, rota_completa

minha_lista_de_compras = ["Molho de Tomate", "Farinha", "Sorvete", "Tomate", "Cerveja"]

print("Lista de compras:", minha_lista_de_compras)
print("=" * 90)

passos_bfs, rota_bfs = rota_bfs_lista(minha_lista_de_compras, grafo, prod_secao)
print(f"Passos BFS: {passos_bfs} passos")
print(f"Rota BFS:   {rota_bfs}")
print("-" * 90)

passos_dfs, rota_dfs = rota_dfs_lista(minha_lista_de_compras, grafo, prod_secao)
print(f"Passos DFS: {passos_dfs} passos")
print(f"Rota DFS:   {rota_dfs}")
print("-" * 90)

passos_gulosa, rota_gulosa = rota_gulosa_lista(minha_lista_de_compras, grafo, prod_secao)
print(f"Passos Gulosa: {passos_gulosa} passos")
print(f"Rota Gulosa:   {rota_gulosa}")
print("=" * 90)