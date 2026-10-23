import random
import tsplib95

NOME_ARQUIVO = 'brazil58.tsp'
instancia = tsplib95.load(NOME_ARQUIVO)
lista_cidades = list(instancia.get_nodes())


TAM_POPULACAO = 60
GERACOES = 300
TAXA_CRUZAMENTO = 0.8
TAXA_MUTACAO = 0.15

cache_custos = {}


def calcular_custo_rota(rota):
    """Calcula a distância total da rota de forma inteligente e rápida"""
   
    chave_rota = tuple(rota)
    
  
    if chave_rota in cache_custos:
        return cache_custos[chave_rota]
        
    distancia_total = 0
    num_cidades = len(rota)
    
    for i in range(num_cidades):
        cidade_atual = rota[i]
        proxima_cidade = rota[(i + 1) % num_cidades]
        distancia_total += instancia.get_weight(cidade_atual, proxima_cidade)
        

    cache_custos[chave_rota] = distancia_total
    return distancia_total

def criar_populacao_inicial():
    """Gera rotas aleatórias misturando as cidades"""
    populacao = []
    for _ in range(TAM_POPULACAO):
        rota = lista_cidades.copy()
        random.shuffle(rota)
        populacao.append(rota)
    return populacao

def selecao_torneio(populacao):
    """Escolhe 3 rotas aleatórias e devolve a melhor delas"""
    sorteados = random.sample(populacao, 3)

    melhor_rota = min(sorteados, key=calcular_custo_rota)
    return melhor_rota.copy()

def cruzamento_historico(pai1, pai2):
    """Combina partes do pai1 com o pai2 sem repetir cidades"""
    if random.random() > TAXA_CRUZAMENTO:
        return pai1.copy()
        
    ponto_corte = random.randint(1, len(pai1) - 2)
    filho = pai1[:ponto_corte]
    
  
    cidades_no_filho = set(filho)
    
    for cidade in pai2:
        if cidade not in cidades_no_filho:
            filho.append(cidade)
            
    return filho

def mutacao_troca(rota):
    """Troca duas cidades de lugar aleatoriamente na rota"""
    if random.random() < TAXA_MUTACAO:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]


def executar_trabalho():
    populacao = criar_populacao_inicial()
    
  
    melhor_solucao = min(populacao, key=calcular_custo_rota)
    melhor_custo = calcular_custo_rota(melhor_solucao)
    
    print(f"Custo inicial (aleatório): {melhor_custo}\n")
    
    for geracao in range(GERACOES):
        nova_populacao = []
        
      
        melhor_da_geracao = min(populacao, key=calcular_custo_rota)
        nova_populacao.append(melhor_da_geracao.copy())
        

        while len(nova_populacao) < TAM_POPULACAO:
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)
            
            filho = cruzamento_historico(pai1, pai2)
            mutacao_troca(filho)
            
            nova_populacao.append(filho)
            
        populacao = nova_populacao
        
       
        melhor_da_geracao = min(populacao, key=calcular_custo_rota)
        custo_da_geracao = calcular_custo_rota(melhor_da_geracao)
        
        if custo_da_geracao < melhor_custo:
            melhor_custo = custo_da_geracao
            melhor_solucao = melhor_da_geracao.copy()
            
        if (geracao + 1) % 50 == 0:
            print(f"Geração {geracao + 1}: Melhor custo encontrado = {melhor_custo}")

    
    print("\n" + "="*40)
    print("      RELATÓRIO DO TRABALHO DE IA      ")
    print("="*40)
    print(f"1. Ficheiro de instância escolhido: {NOME_ARQUIVO}")
    print(f"2. Custo total do menor ciclo encontrado: {melhor_custo}")
    print(f"3. Ordem das cidades visitadas:\n{melhor_solucao}")
    print("="*40)

if __name__ == "__main__":
    executar_trabalho()
