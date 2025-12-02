from arvore_binaria import ArvoreBinaria
from grafo import Grafo
import os
import sys


def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa a execução e aguarda o usuário pressionar Enter"""
    input("\nPressione ENTER para continuar...")


def exibir_cabecalho():
    """Exibe o cabeçalho do programa"""
    print("="*60)
    print(" "*10 + "ESTRUTURAS DE DADOS - MENU PRINCIPAL")
    print("="*60)


def menu_principal():
    """Exibe o menu principal"""
    limpar_tela()
    exibir_cabecalho()
    print("\n[1] Árvore Binária de Busca")
    print("[2] Grafos")
    print("[0] Sair do Programa")
    print("-"*60)


def menu_arvore():
    """Exibe o menu de operações da Árvore Binária"""
    limpar_tela()
    print("="*60)
    print(" "*15 + "ÁRVORE BINÁRIA DE BUSCA")
    print("="*60)
    print("\n[1] Criar Nova Árvore")
    print("[2] Inserir Valor")
    print("[3] Buscar Valor")
    print("[4] Encontrar Maior Valor")
    print("[5] Encontrar Menor Valor")
    print("[6] Imprimir Árvore")
    print("[0] Voltar ao Menu Principal")
    print("-"*60)


def menu_grafo():
    """Exibe o menu de operações de Grafos"""
    limpar_tela()
    print("="*60)
    print(" "*23 + "GRAFOS")
    print("="*60)
    print("\n[1] Criar Novo Grafo")
    print("[2] Adicionar Aresta (Não Direcionado)")
    print("[3] Adicionar Arco (Direcionado)")
    print("[4] Buscar Conexão")
    print("[5] Imprimir Grafo")
    print("[0] Voltar ao Menu Principal")
    print("-"*60)


def obter_opcao():
    """Obtém e valida a opção do usuário"""
    try:
        opcao = input("\nEscolha uma opção: ").strip()
        return opcao
    except (ValueError, KeyboardInterrupt):
        return None


def executar_arvore_binaria(arvore=None):
    """
    Executa o módulo de Árvore Binária.
    Se for passada uma instância 'arvore', usa-a; caso contrário cria nova.
    """
    if arvore is None:
        arvore = ArvoreBinaria()
    
    while True:
        menu_arvore()
        opcao = obter_opcao()
        
        if opcao == '1':
            limpar_tela()
            print("\n🌳 CRIAR NOVA ÁRVORE")
            print("-"*60)
            arvore.criar_arvore()
            pausar()
        
        elif opcao == '2':
            limpar_tela()
            print("\n➕ INSERIR VALORES")
            print("-"*60)
            print("Digite vários valores separados por espaço (ex: 10 5 7 20 1)")
            entrada = input("Valores: ").strip()

            try:
                # permite inserir também apenas 1 valor
                if entrada == "":
                    print("\n✗ Nenhum valor fornecido.")
                else:
                    valores = [int(v) for v in entrada.split()]
                    for v in valores:
                        arvore.inserir(v)
            except ValueError:
                print("\n✗ Erro: Digite apenas números inteiros separados por espaço!")

            pausar()
        
        elif opcao == '3':
            limpar_tela()
            print("\n🔍 BUSCAR VALOR")
            print("-"*60)
            try:
                valor = int(input("Digite o valor a ser buscado: "))
                arvore.buscar(valor)
            except ValueError:
                print("\n✗ Erro: Digite um número inteiro válido!")
            pausar()
        
        elif opcao == '4':
            limpar_tela()
            print("\n⬆️ MAIOR VALOR")
            print("-"*60)
            arvore.maior_valor()
            pausar()
        
        elif opcao == '5':
            limpar_tela()
            print("\n⬇️ MENOR VALOR")
            print("-"*60)
            arvore.menor_valor()
            pausar()
        
        elif opcao == '6':
            limpar_tela()
            arvore.imprimir_arvore()
            pausar()
        
        elif opcao == '0':
            print("\n↩️ Voltando ao menu principal...")
            pausar()
            break
        
        else:
            print("\n✗ Opção inválida! Tente novamente.")
            pausar()


def executar_grafo():
    grafo = Grafo()
    
    while True:
        menu_grafo()
        opcao = obter_opcao()
        
        if opcao == '1':
            limpar_tela()
            print("\n🔗 CRIAR NOVO GRAFO")
            print("-"*60)
            print("\n[1] Grafo Não Direcionado (Arestas)")
            print("[2] Grafo Direcionado (Arcos)")
            
            tipo = input("\nEscolha o tipo: ").strip()
            
            if tipo == '1':
                grafo.criar_grafo(direcionado=False)
            elif tipo == '2':
                grafo.criar_grafo(direcionado=True)
            else:
                print("\n✗ Opção inválida!")
            
            pausar()
        
        elif opcao == '2':
            limpar_tela()
            print("\n➕ ADICIONAR ARESTA (NÃO DIRECIONADO)")
            print("-"*60)
            
            v1 = input("Digite o primeiro vértice: ").strip()
            v2 = input("Digite o segundo vértice: ").strip()
            
            try:
                peso = input("Digite o peso (ou Enter para peso 1): ").strip()
                peso = int(peso) if peso else 1
                grafo.adicionar_aresta(v1, v2, peso)
            except ValueError:
                print("\n✗ Erro: Peso inválido!")
            
            pausar()
        
        elif opcao == '3':
            limpar_tela()
            print("\n➕ ADICIONAR ARCO (DIRECIONADO)")
            print("-"*60)
            
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            
            try:
                peso = input("Digite o peso (ou Enter para peso 1): ").strip()
                peso = int(peso) if peso else 1
                grafo.adicionar_arco(origem, destino, peso)
            except ValueError:
                print("\n✗ Erro: Peso inválido!")
            
            pausar()
        
        elif opcao == '4':
            limpar_tela()
            print("\n🔍 BUSCAR CONEXÃO")
            print("-"*60)
            
            v1 = input("Digite o primeiro vértice: ").strip()
            v2 = input("Digite o segundo vértice: ").strip()
            
            grafo.buscar_aresta(v1, v2)
            pausar()
        
        elif opcao == '5':
            limpar_tela()
            grafo.imprimir_grafo()
            pausar()
        
        elif opcao == '0':
            print("\n↩️ Voltando ao menu principal...")
            pausar()
            break
        
        else:
            print("\n✗ Opção inválida! Tente novamente.")
            pausar()


def main():
    """Função principal do programa"""
    while True:
        menu_principal()
        opcao = obter_opcao()
        
        if opcao == '1':
            # Ao entrar na opção Árvore Binária, pedimos os valores imediatamente
            limpar_tela()
            print("\n🌳 ÁRVORE BINÁRIA DE BUSCA - INSERIR VALORES INICIAIS")
            print("-"*60)
            print("Digite vários valores separados por espaço para inserir na árvore")
            print("(ex: 50 30 70 20 40 60 80)")
            print("Ou pressione Enter para começar com uma árvore vazia:")
            entrada = input("\nValores: ").strip()

            arvore_inicial = ArvoreBinaria()
            if entrada:
                try:
                    valores = [int(v) for v in entrada.split()]
                    for v in valores:
                        arvore_inicial.inserir(v)
                    print(f"\n✓ {len(valores)} valor(es) inserido(s) com sucesso!")
                except ValueError:
                    print("\n✗ Erro: Digite apenas números inteiros separados por espaço!")
                pausar()
            else:
                print("\n✓ Árvore vazia criada. Você pode inserir valores no menu.")
                pausar()

            # Abre o menu da árvore com a árvore (possivelmente com valores) já criada
            executar_arvore_binaria(arvore_inicial)
        
        elif opcao == '2':
            executar_grafo()
        
        elif opcao == '0':
            limpar_tela()
            print("\n" + "="*60)
            print(" "*15 + "ENCERRANDO O PROGRAMA")
            print("="*60)
            print("\n✓ Obrigado por usar o programa!")
            print("✓ Até logo!\n")
            sys.exit(0)
        
        else:
            print("\n✗ Opção inválida! Tente novamente.")
            pausar()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Programa interrompido pelo usuário!")
        print("✓ Até logo!\n")
        sys.exit(0)