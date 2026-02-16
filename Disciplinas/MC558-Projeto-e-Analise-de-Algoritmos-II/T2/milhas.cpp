#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    while (true) {
        string entrada;
        getline(cin, entrada);
        if (entrada == "0")
            break;

        int intercecoes, ruas;
        sscanf(entrada.c_str(), "%d %d", &intercecoes, &ruas);

        vector<vector<double>> w(intercecoes + 1, vector<double>(intercecoes + 1, 0.0));

        for (int i = 0; i < ruas; ++i) {
            int u, v, p;
            cin >> u >> v >> p;
            w[u][v] = p * 1e-2;
            w[v][u] = p * 1e-2;
        }

        for (int k = 1; k <= intercecoes; k++)
            for (int i = 1; i <= intercecoes; i++)
                for (int j = 1; j <= intercecoes; j++)
                    if (w[i][k] > 0 && w[k][j] > 0) 
                        w[i][j] = max(w[i][j], w[i][k] * w[k][j]);

        cout << fixed << setprecision(6) << w[1][intercecoes] * 1e2 << " percent" << endl;
    }

    return 0;

}