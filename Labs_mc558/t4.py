class No:
    def __init__(self, id):
        self.id = id
    
    

class Union_find:
#classe que define e controlaa um union find de um grafo

    def __init__(self, nos):
        #inicializa (basicamente faz o make-set)
        self.pai = [i.id for i in nos]
        self.rank = [0 for i in nos]

    def find_set(self, no):
        #find set path comprehension
        if no != self.pai[no]:
            self.pai[no] = self.find_set(self.pai[no])
        return self.pai[no]
    
    def link(self, x, y):
        #link por rank
        if self.rank[x] > self.rank[y]:
            self.pai[y] = x
        else:
            self.pai[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    
    def union(self, x, y):
        #union por rank
        self.link(self.find_set(x), self.find_set(y))


class Aresta:
    #classe que define uma aresta (mas facil fazer assim pra esse lab)
    def __init__(self, no_1, no_2, peso):
        self.no1 = no_1
        self.no2 = no_2
        self.peso = peso
        





def kruskal(arestas, k, n, union_find):
    #ordena as arestas
    arestas_crescente = sorted(arestas, key=lambda x: x.peso)
    peso_total = 0
    numero_de_componentes = n
    for i in arestas_crescente:
        #quando alcaca os componentes desejados para a iteracao
        if(numero_de_componentes == k):
            break

        if(union_find.find_set(i.no1.id) != union_find.find_set(i.no2.id)):
            #ao juntar adiciona o peso da aresta usada para adicionar no peso total da rede e diminui um componentente
            #obs = ao juntar dois componentes o nmro de componentes resultantes eh decrescido em um
            peso_total += i.peso
            union_find.union(i.no1.id, i.no2.id)
            numero_de_componentes -= 1

    return peso_total
            

entrada = input().split(" ")
nos = []
for i in range(int(entrada[0])):
    no = No(i)
    nos.append(no)

union_find = Union_find(nos)

arestas = []

for i in range(int(entrada[1])):
    linha = input().split(" ") 
    arestas.append(Aresta(nos[int(linha[0])], nos[int(linha[1])], int(linha[2])))

print(kruskal(arestas, int(entrada[2]), int(entrada[0]), union_find))