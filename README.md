<p align="center">
  <img src="banner.jpg" alt="Resolução do Caixeiro Viajante" width="100%">
</p>


## 📌 Sobre o Projeto

O objetivo deste projeto é encontrar ou aproximar a rota de menor custo que visite todas as cidades de uma determinada instância e retorne ao ponto de partida (Problema do Caixeiro Viajante - TSP). 

Para a resolução, foi implementado um **Algoritmo Genético (AG)** adaptado para permutações, utilizando técnicas de evolução artificial.

## Instância Utilizada

* **Arquivo:** `brazil58.tsp` (Dados oficiais da TSPLIB)
* **Descrição:** Coordenadas de **58 cidades no Brasil**
* **Melhor custo ótimo conhecido:** 25395

## ⚙️ Características do Algoritmo Genético

Para garantir a agilidade e a convergência do algoritmo, as seguintes técnicas foram programadas do zero:
* **Tamanho da População:** 60 indivíduos (rotas)
* **Critério de Parada:** 300 gerações
* **Seleção:** Método de Torneio (com 3 indivíduos por disputa)
* **Cruzamento:** Mapeamento histórico (Ordered Crossover simplificado) para evitar repetição de cidades
* **Mutação:** Operador Swap (troca de posição de duas cidades com taxa de 15%)
* **Otimização de Performance:** Implementação de **Dicionário de Cache (Memoização)** para evitar o recálculo de rotas idênticas, tornando a execução quase instantânea.

## 🚀 Como Executar o Projeto

1. Instale a biblioteca necessária recomendada pelo professor:
   ```bash
   pip install tsplib95 --break-system-packages
   ```

2. Certifique-se de que o arquivo `brazil58.tsp` está na mesma pasta que o script `main.py`.

3. Execute o programa:
   ```bash
   python main.py
   ```

## 📊 Resultados Obtidos

Ao final das 300 gerações, o algoritmo obteve a seguinte evolução:
* **Custo Inicial (Aleatório):** ~3761
* **Melhor Custo Encontrado:** **1308**

---
Desenvolvido por jp-devl 💻
