class No:

    def __init__(self, id):  #no com id e cor que indica o estado dele num algoritmo de ordem topologica
        self.id = id
        self.cor = 0

class Grafo:
    #representando o grafo por uma lista de nos e um dict representando a lista de adj dos nos com dicts
    def __init__(self, Nos):
        self.nos = Nos
        self.lista_adj = {}

        for no in self.nos:
            self.lista_adj[no.id] = {}

    def add_aresta(self,v,e,cor): #adiciona aresta (facil ou dificiul) entre dois nos
        self.lista_adj[v][e] = cor

    def print_lista_adj(self): #printa lista de adj (usado para debug)
        for no in self.nos:
            print(no.id, ":", self.lista_adj[no.id])   




def Visit(grafo, no, tempo, d, f,pai, ordem_topologica):#visit de um bfs

    tempo = tempo + 1
    d[no.id] = tempo  #adicona na chave do no o tempo do mesmo
    for u in grafo.lista_adj[no.id]: #passa pelos nos adjacentes verifica cor defini o pai e chama recursivamente
        if grafo.nos[u].cor == 0:
            pai[u] = no
            Visit(grafo, grafo.nos[u], tempo, d, f, pai,ordem_topologica)
    no.cor = 2 #finaliza e grava tempo de fim
    f[no.id] = tempo
    tempo = tempo + 1
    ordem_topologica.insert(0, no.id) #coloca no comeco de uma lista para montar ordem topologica



def Ordem_Topologica(grafo): 
    pai = {} #inicializa dicts e lista necessarias para montar a ordem topologica usando um bfs
    d = {}
    f = {}
    ordem_topologica = []

    for no in grafo.nos:
        pai[no.id] = None
    
    tempo = 0

    #visita nos do grafo

    for no in grafo.nos:
        if no.cor == 0:
            Visit(grafo, no, tempo, d, f, pai, ordem_topologica)
    return ordem_topologica


def Calculo_caminhos(grafo, ordem, inicio, fim): #dada ordem topologica e grafo calcula caminhos por programacao dinamica

    qtd_caminhos = [0 for i in range(len(ordem))] #inicializa caminhos faceis
    qtd_caminhos[inicio] = 1 #primeiro no deve ter valor inicalizado como 1
    qtd_caminhos_dificeis = [0 for i in range(len(ordem))] #inicializa caminhos dificeis
    
    #salvando indexs de no inicial e final na lista de ordem topologica
    index_inicio = ordem.index(inicio)
    index_fim = ordem.index(fim)

    #percorre os vertices da ordem topologica
    for no_index in range(len(ordem)):
        if no_index >= index_inicio and no_index <= index_fim:
            #percorre os nos adjacentes
            for no_adj in grafo.lista_adj[ordem[no_index]]:

                #se um caminho eh facil entao basta somar aos caminhos faceis do no atual com todos os caminhos do anterior
                if grafo.lista_adj[ordem[no_index]][no_adj] == 0:
                    qtd_caminhos[no_adj] = qtd_caminhos[no_adj] + qtd_caminhos_dificeis[ordem[no_index]] + qtd_caminhos[ordem[no_index]]
                #se o caminho for dificiul soma-se somente os caminhos faceis do no anterior ao atual
                else:
                    qtd_caminhos_dificeis[no_adj] = qtd_caminhos_dificeis[no_adj] + qtd_caminhos[ordem[no_index]]
    #retorna todos caminhos possiveis ate o no finaal
    return qtd_caminhos[fim] + qtd_caminhos_dificeis[fim] 




entrada = input().split(" ")
nos = []
for i in range(int(entrada[0])):
    no = No(i)
    nos.append(no)

grafo = Grafo(nos)


for i in range(int(entrada[1])):
    linha = input().split(" ") 
    grafo.add_aresta(int(linha[0]), int(linha[1]), int(linha[2]))


ordem = Ordem_Topologica(grafo)


print(Calculo_caminhos(grafo, ordem, int(entrada[2]), int(entrada[3])))