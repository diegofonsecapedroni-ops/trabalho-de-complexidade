class No:
    """Classe que representa um nó da árvore binária"""
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    """Classe que implementa uma Árvore Binária de Busca"""
    
    def __init__(self):
        self.raiz = None
    
    def criar_arvore(self):
        """Cria uma nova árvore vazia"""
        self.raiz = None
        print("\n✓ Árvore criada com sucesso!")
    
    def inserir(self, valor):
        """Insere um novo valor na árvore"""
        if self.raiz is None:
            self.raiz = No(valor)
            print(f"\n✓ Valor {valor} inserido como raiz da árvore!")
        else:
            self._inserir_recursivo(self.raiz, valor)
            print(f"\n✓ Valor {valor} inserido na árvore!")
    
    def _inserir_recursivo(self, no_atual, valor):
        """Método auxiliar para inserir recursivamente"""
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)
    
    def buscar(self, valor):
        """Busca um valor na árvore"""
        if self.raiz is None:
            print("\n✗ A árvore está vazia!")
            return False
        
        encontrado = self._buscar_recursivo(self.raiz, valor)
        if encontrado:
            print(f"\n✓ Valor {valor} encontrado na árvore!")
        else:
            print(f"\n✗ Valor {valor} não encontrado na árvore!")
        return encontrado
    
    def _buscar_recursivo(self, no_atual, valor):
        """Método auxiliar para buscar recursivamente"""
        if no_atual is None:
            return False
        
        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)
    
    def maior_valor(self):
        """Retorna o maior valor da árvore"""
        if self.raiz is None:
            print("\n✗ A árvore está vazia!")
            return None
        
        no_atual = self.raiz
        while no_atual.direita is not None:
            no_atual = no_atual.direita
        
        print(f"\n✓ Maior valor da árvore: {no_atual.valor}")
        return no_atual.valor
    
    def menor_valor(self):
        """Retorna o menor valor da árvore"""
        if self.raiz is None:
            print("\n✗ A árvore está vazia!")
            return None
        
        no_atual = self.raiz
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        
        print(f"\n✓ Menor valor da árvore: {no_atual.valor}")
        return no_atual.valor
    
    def imprimir_arvore(self):
        """Imprime a árvore em diferentes ordens"""
        if self.raiz is None:
            print("\n✗ A árvore está vazia!")
            return
        
        print("\n" + "="*50)
        print("IMPRESSÃO DA ÁRVORE")
        print("="*50)
        
        print("\n📊 Em Ordem (Crescente):")
        self._em_ordem(self.raiz)
        
        print("\n\n📊 Pré-Ordem:")
        self._pre_ordem(self.raiz)
        
        print("\n\n📊 Pós-Ordem:")
        self._pos_ordem(self.raiz)
        
        print("\n\n📊 Estrutura Visual:")
        self._imprimir_estrutura(self.raiz, "", True)
        print()
    
    def _em_ordem(self, no):
        """Percurso em ordem (esquerda, raiz, direita)"""
        if no is not None:
            self._em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self._em_ordem(no.direita)
    
    def _pre_ordem(self, no):
        """Percurso pré-ordem (raiz, esquerda, direita)"""
        if no is not None:
            print(no.valor, end=" ")
            self._pre_ordem(no.esquerda)
            self._pre_ordem(no.direita)
    
    def _pos_ordem(self, no):
        """Percurso pós-ordem (esquerda, direita, raiz)"""
        if no is not None:
            self._pos_ordem(no.esquerda)
            self._pos_ordem(no.direita)
            print(no.valor, end=" ")
    
    def _imprimir_estrutura(self, no, prefixo, is_esquerda):
        """Imprime a estrutura visual da árvore"""
        if no is not None:
            print(prefixo, end="")
            print("├──" if is_esquerda else "└──", end="")
            print(no.valor)
            
            if no.esquerda is not None or no.direita is not None:
                if no.esquerda is not None:
                    self._imprimir_estrutura(
                        no.esquerda, 
                        prefixo + ("│   " if is_esquerda else "    "), 
                        True
                    )
                else:
                    print(prefixo + ("│   " if is_esquerda else "    ") + "├──(vazio)")
                
                if no.direita is not None:
                    self._imprimir_estrutura(
                        no.direita, 
                        prefixo + ("│   " if is_esquerda else "    "), 
                        False
                    )
                else:
                    print(prefixo + ("│   " if is_esquerda else "    ") + "└──(vazio)")