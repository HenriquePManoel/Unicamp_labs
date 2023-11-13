class Grafo:
    #representando o grafo por uma lista de nos e um dict representando a lista de adj dos nos com dicts
    def __init__(self, Nos):
        self.nos = Nos
        self.lista_adj = {}

        for no in self.nos:
            self.lista_adj[no] = {}

    def add_aresta(self,v,e,cor): #constroe arestas
        self.lista_adj[v][e] = cor
        self.lista_adj[e][v] = cor

    def visitar_aresta(self, v, e): #retira (visita) arestas
        self.lista_adj[v].pop(e)
        self.lista_adj[e].pop(v)

    def lista_adj(self):  #retorna a lista de adj
        return self.lista_adj


    def print_lista_adj(self): #printa lista de adj (usado para debug)
        for no in self.nos:
            print(no, ":", self.lista_adj[no])


    

def Trilha_maximal_alternada(no_inicial,grafo,cor): #constroe uma trilha alternada onde a cor da aresta nao pode se repetir
                                                    #comecando pela cor dada no parametro
    trilha = []
    v = no_inicial
    trilha.append([v,cor])
    
    i = 0
    while True: #loop tem que parar caso o loop for chegue ao final sem break (nao encontrou aresta para ir a partir do no atual)
        if i == len(grafo.lista_adj[v]):
            break

        for no in grafo.lista_adj[v]:
            if grafo.lista_adj[v][no] != cor: #(adiciona no a trilha e salva a cor da aresta que foi usada para tal no)
                cor = grafo.lista_adj[v][no]
                grafo.visitar_aresta(v, no)
                v = no
                trilha.append([no, cor])
                i = 0
                break
            else:
                i += 1

    return trilha

def printa_trilha(trilha):
    for i in trilha:
        print(i[0], end=' ')


def inserir_na_trilha(trilha_original, insercao): #insere trilha menor em uma maior a partir da primeira ocasio do primeiro item da trilha menor na trilha maior
    for i in range(len(trilha_original)):
        if(trilha_original[i][0] == insercao[0][0]):
            index = i
            break
    for i in range(len(insercao) - 1):
        trilha_original.insert(index + i + 1, insercao[i + 1])


def Trilha_Euleriana_Alternada(grafo):
    trilha_euleriana = Trilha_maximal_alternada(0, grafo, -1) #primiera trilha maximal
    possivel = (trilha_euleriana[0][0] == trilha_euleriana[-1][0]) #verifica se a trilha esta correta
    
    if(possivel): #adiciona outras trilhas
        while True:
            r = -1
            for no in grafo.lista_adj: #acha um no que tem arestas para ir
                if(len(grafo.lista_adj[no]) != 0):
                    r = no
            

            cor = -1 #cor padrao
            if(r != -1):
                for i in range(len(trilha_euleriana)): #acha a cor da aresta que o chegou naquele no
                    if(trilha_euleriana[i][0] == r):
                        cor = trilha_euleriana[i][1]
                        break
                trilha_secundaria = Trilha_maximal_alternada(r, grafo, cor) #acha a trilha maximal e verfica se ela eh possivel
                if(trilha_secundaria[0][0] != trilha_secundaria[-1][0] or len(trilha_secundaria) < 2):
                    possivel = False
                    break
                else: #insere a trilha maximal secundaria na trilha euleriana que esta sendo formada
                    inserir_na_trilha(trilha_euleriana, trilha_secundaria)
            else:
                break
    if(not possivel):
        print("Não possui trilha Euleriana alternante")
    else:
        printa_trilha(trilha_euleriana)

    return

nos = []
entrada = input().split(" ")

for i in range(int(entrada[0])):
    nos.append(i)

grafo = Grafo(nos)

for i in range(int(entrada[1])):
    linha = input().split(" ") 
    grafo.add_aresta(int(linha[0]), int(linha[1]), int(linha[2]))


Trilha_Euleriana_Alternada(grafo)






    