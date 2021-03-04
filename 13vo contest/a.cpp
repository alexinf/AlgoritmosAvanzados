/*
 * Sai Cheemalapati
 * UVA 259: Software allocation
 *
 */
 
#include<algorithm>
#include<climits>
#include<cstdio>
#include<cstring>
#include<queue>
#include<vector>
 
using namespace std;
 
char A, B;
char input[100], input2[20];
int f, mf, tot;
// 0 is source, 1 - 26 are letters, 27 - 36 are computers, 37 is sink
int res[40][40];
vector<int> vis, pi;
 
void print_letter(int i) {
    for(int j = 1; j < 27; j++) {
        if(res[i][j] == 1) {
            printf("%c", 'A' + j - 1);
            return; 
        }
    }
    printf("_");
}
 
void augment(int min_flow, int v) {
    if(v == 0) {
        f = min_flow;
        return;
    } else if(pi[v] != -1) {
        augment(min(min_flow, res[pi[v]][v]), pi[v]);
        res[pi[v]][v] -= f;
        res[v][pi[v]] += f;
    }
}
 
int main() {
    for(;;) {
        if(gets(input) == 0) break;
        memset(res, 0, sizeof res);
        tot = 0; // initialize total
        do {
            if(strcmp(input, "") == 0) break;
            sscanf(input, "%c%c %s", &A, &B, input2);
            res[0][A - 'A' + 1] = B - '0';
            tot += B - '0';
            for(int i = 0;; i++) {
                if(input2[i] == ';') break;
                res[A - 'A' + 1][27 + input2[i] - '0'] = INT_MAX;
            }
        } while(gets(input));
        for(int i = 27; i < 37; i++) {
            res[i][37] = 1;
        }
 
        mf = 0;
        for(;;) {
            pi.assign(40, -1);
            vis.assign(40, false);
            vis[0] = true;
            queue<int> q;
            q.push(0);
            f = 0;
            while(!q.empty()) {
                int c = q.front();
                if(c == 37) break;
                q.pop();
                for(int v = 0; v < 38; v++) {
                    if(res[c][v] > 0 && !vis[v]) {
                        vis[v] = true;
                        q.push(v);
                        pi[v] = c;
                    }
                }
            }
            augment(INT_MAX, 37);
            if(f == 0) break;
            mf += f;
        }
        if(mf == tot)
            for(int i = 27; i < 37; i++) {
                print_letter(i);
            } 
        else printf("!");
        printf("\n");
    }
}
