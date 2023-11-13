def printa_grafo(grafo): # funcao para printar grafo segundo template desejado
    for i in grafo:
        print(*i, sep=' ')


def sequencia_grafica(arr):

    arr.sort(reverse = True)
    arr_final = [[arr[i], i] for i in range(len(arr))] #cria vetor que armazena as posicoes iniciais de cada grau

    aux_arr = [[arr_final[i+1][0], arr_final[i+1][1]] for i in range(len(arr_final) - 1)] # retira o primeiro elemento do vetor


    grafo = [[] for i in range(len(arr_final))] #inicializa  o grafo


    while(len(arr_final) > 1):

        for i in range(arr_final[0][0]): #subtrai 1 dos k primeiro elementos de aux_arr

            if i < len(aux_arr) and aux_arr[i][0] > 0:  #verifica se o vertice eh valido -> se ele existe ou se eh possivel conectar
                grafo[arr_final[0][1]].append(aux_arr[i][1]+1) #cria arestas entre o vertice autal do metodo e o da iteracao
                grafo[aux_arr[i][1]].append(arr_final[0][1]+1)
                aux_arr[i][0] -= 1 #diminue um do grau do vertice da iteracao
            else: 
                print("Não é sequência gráfica!") #se o vertice nao eh valido nao ha uma sequencia grafica
                return
        arr_final = aux_arr #atualiza array e ordena novamente
        arr_final.sort(reverse=True)
        aux_arr = [[arr_final[i+1][0], arr_final[i+1][1]] for i in range(len(arr_final) - 1)] #atualiza array auxiliar

    if arr_final[0][0] != 0: #se o ultimo vertice nao tem grau 0 entao ele nao pode fazer par com ninguem e a sequencia nao eh grafica
        print("Não é sequência gráfica!")
    else:
        printa_grafo(grafo) #se chegou ate aqui e esta tudo certo o grafo criado eh uma sequencia grfica valida
    return

#input do numero de vertices nao utiizado por nao necessitar do mesmo em python
n = int(input()) 

#leitura da sequencia de graus inicial
arr = input().split() 
arr = [int(i) for i in arr]
sequencia_grafica(arr) 

