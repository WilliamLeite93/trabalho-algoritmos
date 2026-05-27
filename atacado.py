from collections import defaultdict, deque

dados_mercado = {
  "nome_mercado": "Macro Atacado",
  "conexoes": [
    {"origem": "Entrada", "destino": "Corredor_1_Frente", "distancia": 5},
    {"origem": "Saida_Caixas", "destino": "Corredor_6_Frente", "distancia": 5},
    {"origem": "Corredor_6_Frente", "destino": "Frios", "distancia": 8},
    {"origem": "Corredor_6_Fundo", "destino": "Acougue", "distancia": 8},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_1_Frente", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_2_Frente", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_3_Frente", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_4_Frente", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_5_Frente", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_6_Frente", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_1_Fundo", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_2_Fundo", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_3_Fundo", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_4_Fundo", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_5_Fundo", "distancia": 15},
    {"origem": "Via_Central_Horizontal", "destino": "Corredor_6_Fundo", "distancia": 15},
    {"origem": "Corredor_1_Fundo", "destino": "Via_Fundos_Dir", "distancia": 20},
    {"origem": "Corredor_2_Fundo", "destino": "Via_Fundos_Dir", "distancia": 15},
    {"origem": "Corredor_3_Fundo", "destino": "Via_Fundos_Centro", "distancia": 15},
    {"origem": "Corredor_4_Fundo", "destino": "Via_Fundos_Centro", "distancia": 15},
    {"origem": "Corredor_5_Fundo", "destino": "Via_Fundos_Esq", "distancia": 15},
    {"origem": "Corredor_6_Fundo", "destino": "Via_Fundos_Esq", "distancia": 20},
    {"origem": "Via_Fundos_Esq", "destino": "Hortifruti", "distancia": 5},
    {"origem": "Via_Fundos_Centro", "destino": "Congelados", "distancia": 5},
    {"origem": "Via_Fundos_Dir", "destino": "Via_Fundos_Centro", "distancia": 25},
    {"origem": "Via_Fundos_Centro", "destino": "Via_Fundos_Esq", "distancia": 25}
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
    distancia = conexao["distancia"]

    grafo[origem][destino] = distancia
    grafo[destino][origem] = distancia

def busca_bfs(grafo, origem, destino):
    fila = deque([(origem, [origem])])
    visitados = set([origem])

    while fila:
        no_atual, caminho = fila.popleft()
        if no_atual == destino:
            distancia_total = 0
            for i in range(len(caminho) - 1):
                distancia_total += grafo[caminho[i]][caminho[i + 1]]
            return distancia_total, caminho
        
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    return 0, []
    
distancia, rota = busca_bfs(grafo, "Entrada", "Congelados")
print(f"Distância do caminho: {distancia}")
print(f"Rota percorrida: {rota}")
print("-" * 90)


def busca_dfs(grafo, origem, destino):
  pilha = [(origem, [origem])]
  visitados = set()

  while pilha:
      no_atual, caminho = pilha.pop()
      if no_atual == destino:
          distancia_total = 0
          for i in range(len(caminho) - 1):
            distancia_total += grafo[caminho[i]][caminho[i + 1]]
          return distancia_total, caminho
      if no_atual not in visitados:
          visitados.add(no_atual)
          for vizinho in grafo[no_atual]:
              if vizinho not in visitados:
                  pilha.append((vizinho, caminho + [vizinho]))
  return 0, []

distancia_dfs, rota_dfs = busca_dfs(grafo, "Entrada", "Acougue")
print(f"Distância DFS: {distancia_dfs}")
print(f"Rota DFS: {rota_dfs}")
print("-" * 90)


def calcular_rota_gulosa(lista_compras, grafo, prod_secao):
    secoes_alvo = set()
    for item in lista_compras:
        if item in prod_secao:
            secoes_alvo.add(prod_secao[item])
        else:
            print(f"Aviso: O item '{item}' não existe no mercado.")
            
    secoes_pendentes = list(secoes_alvo)
    
    if not secoes_pendentes:
        return 0, []

    local_atual = "Entrada"
    distancia_total_compras = 0
    rota_completa = ["Entrada"] 

    while secoes_pendentes:
        menor_distancia = float('inf')
        proxima_secao_escolhida = None
        melhor_caminho_parcial = []

        for secao_destino in secoes_pendentes:
            distancia_perna, caminho_perna = busca_bfs(grafo, local_atual, secao_destino)
            
            if distancia_perna < menor_distancia:
                menor_distancia = distancia_perna
                proxima_secao_escolhida = secao_destino
                melhor_caminho_parcial = caminho_perna
                
        distancia_total_compras += menor_distancia
        rota_completa.extend(melhor_caminho_parcial[1:])
        
        local_atual = proxima_secao_escolhida
        secoes_pendentes.remove(proxima_secao_escolhida)

    dist_caixa, caminho_caixa = busca_bfs(grafo, local_atual, "Saida_Caixas")
    distancia_total_compras += dist_caixa
    rota_completa.extend(caminho_caixa[1:])

    return distancia_total_compras, rota_completa


minha_lista_de_compras = ["Arroz", "Cerveja", "Carne Moída", "Sabão em Pó", "Banana"]

print("Lista de compras:", minha_lista_de_compras)

distancia_final, rota_final = calcular_rota_gulosa(minha_lista_de_compras, grafo, prod_secao)

print(f"Distancia total percorrida: {distancia_final} metros")
print(f"Rota passo a passo: {rota_final} ")


