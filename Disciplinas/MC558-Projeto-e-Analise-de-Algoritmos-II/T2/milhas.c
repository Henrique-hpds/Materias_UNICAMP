#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    while (true) {
        int intercecoes, ruas;
        scanf("%d", &intercecoes);
        if (intercecoes == 0)
            break;
        scanf("%d", &ruas);

        double **w = (double **)malloc((intercecoes + 1) * sizeof(double *));
        for (int i = 0; i <= intercecoes; i++) {
            w[i] = (double *)malloc((intercecoes + 1) * sizeof(double));
            for (int j = 0; j <= intercecoes; j++)
                w[i][j] = 0.0;
        }

        for (int r = 0; r < ruas; r++) {
            int i, j;
            double p;
            scanf("%d %d %lf", &i, &j, &p);
            w[i][j] = p * 1e-2;
            w[j][i] = p * 1e-2;
        }

        for (int k = 1; k <= intercecoes; k++)
            for (int i = 1; i <= intercecoes; i++)
                for (int j = 1; j <= intercecoes; j++)
                    if (w[i][j] < w[i][k] * w[k][j])
                        w[i][j] = w[i][k] * w[k][j];

        printf("%.6f percent\n", w[1][intercecoes] * 1e2);

        for (int i = 0; i <= intercecoes; i++)
            free(w[i]);
        free(w);
    }

    return 0;
}