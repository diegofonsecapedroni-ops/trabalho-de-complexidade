class Grafo:
    
    def __init__(self):
        self.vertices = {}
        self.direcionado = False
    
    def criar_grafo(self, direcionado=False):
        """Cria um novo grafo"""
        self.vertices = {}
        self.direcionado = direcionado
        tipo = "direcionado" if direcionado else "não direcionado"
        print(f"\n✓ Grafo {tipo} criado com sucesso!")
    
    def adicionar_vertice(self, vertice):
        """Adiciona um vértice ao grafo"""
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            return True
        return False
    
    def adicionar_aresta(self, v1, v2, peso=1):
        """Adiciona uma aresta (grafo não direcionado)"""
        # Adiciona os vértices se não existirem
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)
        
        # Adiciona a aresta (não direcionada - vai nos dois sentidos)
        if v2 not in [aresta[0] for aresta in self.vertices[v1]]:
            self.vertices[v1].append((v2, peso))
        
        if v1 not in [aresta[0] for aresta in self.vertices[v2]]:
            self.vertices[v2].append((v1, peso))
        
        print(f"\n✓ Aresta adicionada: {v1} ↔ {v2} (peso: {peso})")
    
    def adicionar_arco(self, origem, destino, peso=1):
        """Adiciona um arco (grafo direcionado)"""
        # Adiciona os vértices se não existirem
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        # Adiciona o arco (direcionado - vai só em um sentido)
        if destino not in [aresta[0] for aresta in self.vertices[origem]]:
            self.vertices[origem].append((destino, peso))
        
        print(f"\n✓ Arco adicionado: {origem} → {destino} (peso: {peso})")
    
    def buscar_aresta(self, v1, v2):
        """Busca se existe uma aresta/arco entre dois vértices"""
        if v1 not in self.vertices:
            print(f"\n✗ Vértice {v1} não existe no grafo!")
            return False
        
        if v2 not in self.vertices:
            print(f"\n✗ Vértice {v2} não existe no grafo!")
            return False
        
        # Verifica se v2 está nas adjacências de v1
        existe_v1_v2 = any(aresta[0] == v2 for aresta in self.vertices[v1])
        
        if self.direcionado:
            # Para grafo direcionado, verifica apenas uma direção
            if existe_v1_v2:
                peso = next(aresta[1] for aresta in self.vertices[v1] if aresta[0] == v2)
                print(f"\n✓ Arco encontrado: {v1} → {v2} (peso: {peso})")
                return True
            else:
                print(f"\n✗ Arco {v1} → {v2} não encontrado!")
                return False
        else:
            # Para grafo não direcionado, verifica ambas as direções
            existe_v2_v1 = any(aresta[0] == v1 for aresta in self.vertices[v2])
            
            if existe_v1_v2 and existe_v2_v1:
                peso = next(aresta[1] for aresta in self.vertices[v1] if aresta[0] == v2)
                print(f"\n✓ Aresta encontrada: {v1} ↔ {v2} (peso: {peso})")
                return True
            else:
                print(f"\n✗ Aresta {v1} ↔ {v2} não encontrada!")
                return False
    
    def imprimir_grafo(self):
        """Imprime o grafo com lista de adjacências"""
        if not self.vertices:
            print("\n✗ O grafo está vazio!")
            return
        
        print("\n" + "="*50)
        print("IMPRESSÃO DO GRAFO")
        print("="*50)
        
        tipo = "Direcionado" if self.direcionado else "Não Direcionado"
        print(f"\nTipo: {tipo}")
        print(f"Vértices: {len(self.vertices)}")
        
        # Conta as arestas/arcos
        total_conexoes = sum(len(adj) for adj in self.vertices.values())
        if not self.direcionado:
            total_conexoes = total_conexoes // 2  # Cada aresta é contada duas vezes
        
        conexao_tipo = "Arcos" if self.direcionado else "Arestas"
        print(f"{conexao_tipo}: {total_conexoes}")
        
        print("\n📊 Lista de Adjacências:")
        print("-" * 50)
        
        for vertice in sorted(self.vertices.keys()):
            adjacencias = self.vertices[vertice]
            
            if not adjacencias:
                print(f"{vertice}: (sem conexões)")
            else:
                conexoes = []
                for adj, peso in adjacencias:
                    if self.direcionado:
                        conexoes.append(f"{adj}(peso:{peso})")
                    else:
                        conexoes.append(f"{adj}(peso:{peso})")
                
                simbolo = "→" if self.direcionado else "↔"
                print(f"{vertice} {simbolo} {', '.join(conexoes)}")
        
        print("\n📊 Matriz de Adjacências:")
        print("-" * 50)
        self._imprimir_matriz()
        print()
    
    def _imprimir_matriz(self):
        """Imprime a matriz de adjacências do grafo"""
        if not self.vertices:
            return
        
        vertices_lista = sorted(self.vertices.keys())
        
        # Cabeçalho
        print("     ", end="")
        for v in vertices_lista:
            print(f"{str(v):>4}", end="")
        print()
        
        print("   +" + "-" * (len(vertices_lista) * 4))
        
        # Linhas da matriz
        for v1 in vertices_lista:
            print(f"{str(v1):>3}|", end="")
            for v2 in vertices_lista:
                # Verifica se existe conexão
                peso = 0
                for adj, p in self.vertices[v1]:
                    if adj == v2:
                        peso = p
                        break
                
                if peso > 0:
                    print(f"{peso:>4}", end="")
                else:
                    print(f"{'·':>4}", end="")
            print()

        """Retorna estatísticas do grafo"""    
    def obter_estatisticas(self):

        if not self.vertices:
            return None
        
        graus = {}
        for vertice in self.vertices:
            graus[vertice] = len(self.vertices[vertice])
        
        return {
            'vertices': len(self.vertices),
            'graus': graus,
            'grau_maximo': max(graus.values()) if graus else 0,
            'grau_minimo': min(graus.values()) if graus else 0
        }