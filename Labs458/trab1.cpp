#include "lib.hpp"
#include <iostream>
#include <vector>

using namespace std;

/* 
    Se quiser crie funcoes e variaveis aqui    
    


*/
void ligar(int* grafo, int inicio, int fim){
    int *novo_grafo = (int*) malloc((fim - inicio + 1)* sizeof(int)); //aloca memoria 
    int i = 0, selecionado = 0; //inicializa variavel de posicao do novo grafo e o selecionado que indica qual segmento (x ou y) o proximo elemento de grafo sera buscado
    int x = inicio; // posicao inicial do segmento x
    int y = ( inicio + fim)/2 + 1; //posicao inicial do segmento y

    if(has_edge(grafo[x], grafo[y])){ //inicializando os dois primeiros do novo vetor -> primeiro if o x se conecta com y e o proximo elemento sera buscado na parte x do vetor
       novo_grafo[i] = grafo[x];
       i++;
       novo_grafo[i] = grafo[y];
       selecionado = 1;
    }
    
    else{ // o y se conecta com x e o proximo elemento sera buscado no segmento x do vetor
        novo_grafo[i] = grafo[y];
        i++;
        novo_grafo[i] = grafo[x];
        selecionado = 0;
    }
    x++;
    y++;
    i++;


    while(i <= fim-inicio){
        if(x > (inicio + fim)/2 && selecionado){ // completar com y
            novo_grafo[i] = grafo[y];
            i++;
            y++;
        }
        else if(y > fim && !selecionado){ //completar com x
            novo_grafo[i] = grafo[x];
            i++;
            x++;
        }
        else{
            if(selecionado){ //buscando em x
                if(has_edge(novo_grafo[i-1], grafo[x])){ //o proximo x conecta e a proxima iteracao buscara em y
                    selecionado = 0;
                    novo_grafo[i] = grafo[x];
                }
                else{ // o proximo x n conecta no atual porem conecta no anterior entao ele vai imediatamente para tras e a proxima iteracao buscara novamente em x
                    novo_grafo[i] = novo_grafo[i-1]; 
                    novo_grafo[i-1] = grafo[x];
                }
                x++;
            }
            else{ //buscando em y
                if(has_edge(novo_grafo[i-1], grafo[y])){ //o proximo y conecta e a proxima iteracao buscara em x
                    selecionado = 1;
                    novo_grafo[i] = grafo[y];
                }
                else{// o proximo y n conecta no atual porem conecta no anterior entao ele vai imediatamente para tras e a proxima iteracao buscara novamente em y
                    novo_grafo[i] = novo_grafo[i-1];
                    novo_grafo[i-1] = grafo[y];
                }
                y++;
            }
            i++;
        }
    }//fim do loop vetor novo_grafo eh um caminho hamiltoniano

    for(int j = inicio; j <= fim; j++ ){
        grafo[j] = novo_grafo[j-inicio]; //passa o caminho hamiltoniano de volta para o grafo inicial no segmento correspondente
    }

    free(novo_grafo); //libera memoria do grafo temporario utilizado
    
}



int* Caminho_Hamiltoniano(int* vetor_grafo, int  inicio,int  fim ){

    if(inicio >= fim){ //caso base: apenas um no no grafo
        return vetor_grafo;
    }
    else{ //liga os caminhos hamiltonianos de dois subgrafos que sao formados pela metade do grafo (primeiro vai do inicio ate chao de n e outro vai de teto de n ate o n onde n eh o ultimo no do grafo)
        vetor_grafo = Caminho_Hamiltoniano(vetor_grafo, inicio, (inicio + fim) / 2);
        vetor_grafo = Caminho_Hamiltoniano(vetor_grafo, (inicio + fim) / 2 + 1, fim);
        ligar(vetor_grafo, inicio, fim); 
        return vetor_grafo;
    }
}

int* tirolesa(int N, int* grafo){
    
    for(int i = 0; i < N; i++){
        grafo[i] = i + 1;
    }
    return Caminho_Hamiltoniano(grafo, 0, N-1);
}

// has_edge(int i, int j): retorna true se há tirolesa do monte i para o monte j,
//                         nesse sentido, e false caso contrario.
vector<int> solve(int n) {
    /* Modifique a vontade */
    vector<int> path;
    int* grafo = new int[n];
    grafo = tirolesa(n, grafo);
    for(int i = 0; i < n; i++){
        path.push_back(grafo[i]);
    }
    delete[] grafo;
    return path;
}

/* 
    Nao altere nada da main!!!! 
    Para testar seu codigo veja "lib.h"
*/
int main(int argc, char *argv[]) {

    char *filename = NULL;
    if(argc > 1)
        filename = argv[1];

    int n;
    initialize_has_edge(n, filename);

    vector<int> path = solve(n);
    int result = check_path(path, n);
    cout << result << '\n';
    return result;
}