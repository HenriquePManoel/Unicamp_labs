#include <stdio.h>
#include <stdlib.h>

typedef struct pizza {
    int s, t, r;
} pizza;

//retorna o maximo entre tres numeros
int max(int x, int y, int z){
    if(x >= y && x >= z){
        return x;
    }
    else if (y >= z){
        return y;
    }
    return z;
}

//troca duas pizzas em um vetor de pizzas
void troca(pizza* x, pizza* y){
    pizza temp = *x;
    *x = *y;
    *y = temp;
}

//particao porem utiliza vetor de pizzas com parametro de razao de t e r de maneira decrescente
int partitionPizza(pizza *pizzas, int comeco, int fim){
    float pivo = (float) pizzas[fim].t/ (float )pizzas[fim].r;
    int i = comeco - 1;
    for(int j = comeco; j < fim; j++){
        if((float)pizzas[j].t/(float)pizzas[j].r < pivo){
            i++;
            troca(&pizzas[i], &pizzas[j]);
        }

    }
    troca(&pizzas[i + 1], &pizzas[fim]);
    return i + 1;
}

//quicksort porem utilizando vetor de pizzas
void quicksortSortPizza(pizza *pizzas, int comeco, int fim){
    if(comeco < fim){
        int novo = partitionPizza(pizzas, comeco, fim);

        quicksortSortPizza(pizzas, comeco, novo - 1);
        quicksortSortPizza(pizzas, novo + 1, fim);
    }

}

int solve(pizza *pizzas, int N, int T) {
    //ordena em ordem decrescente vetor de pizzas pela razao de t e r para solucao gulosa
    quicksortSortPizza(pizzas, 0, N-1);
    int resultado;
    //montando a matriz para solucionar utilizando programacao dinamica
    int (**dp) = (int**) malloc((N+1)*sizeof(int*));


    for(int i = 0; i <= N; i++)
        (dp[i]) = (int*) malloc((T+1)*sizeof(int));


    //inicializando 0 pizzas com 0
    for(int i = 0; i <= N; i++)
        dp[i][0] = 0;

    //inicializando tempo 0 com 0
    for(int i = 0; i <= T; i++)
        dp[0][i] = 0;

    /*preenche a matriz maximizando o sabor pegando uma das tres opcoes:
    ou o maximo n utiliza a pizza em questao: pega o valor da linha anterior
    ou utiliza a pizza em questo terminando do tempo exato de preparo: soma sabor com a resposta da linha anterior e coluna sem o tempo de preparo
    ou utiliza a pizza em questao porem ha mais tempo do que o necessarioo para preparar a pizza que sera adicionada*/
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= T; j++){
            if(j >= pizzas[i-1].t)
                dp[i][j] = max(dp[i-1][j], pizzas[i-1].s - pizzas[i-1].r * (j) + dp[i-1][j-pizzas[i-1].t], dp[i][j-1]);
            else
                dp[i][j] = dp[i-1][j];
        }
    }
    
    resultado = dp[N][T];

    //libera memoria alocada da matriz

    for(int i = 0; i <= N; i++)
        free(dp[i]);
    free(dp);

    return resultado;
}

int main() {

    int N, T;
    scanf("%d %d", &N, &T);

    pizza pizzas[N];
    for(int i = 0; i < N; ++i)
        scanf("%d %d %d", &pizzas[i].s, &pizzas[i].t, &pizzas[i].r);
    
    printf("%d\n", solve(pizzas, N, T));
    return 0;
}