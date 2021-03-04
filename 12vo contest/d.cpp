#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 + 1010;
char s[maxn];
int num;
int sa[maxn], t[maxn], t2[maxn], c[maxn], n, maxl;
void build_sa(int m) {
    int i, *x = t, *y = t2;
    for (int i = 0; i < m; i++) c[i] = 0;
    for (int i = 0; i < n; i++) c[x[i] = s[i]]++;
    for (int i = 1; i < m; i++) c[i] += c[i-1];
    for (int i = n - 1; i >= 0; i--) sa[--c[x[i]]] = i;
    for (int k = 1; k <= n; k <<= 1) {
        int p = 0;
        for (int i = n - k; i < n; i++) y[p++] = i;
        for (int i = 0; i < n; i++) if (sa[i] >= k) y[p++] = sa[i]-k;
        for (int i = 0; i < m; i++) c[i] = 0;
        for (int i = 0; i < n; i++) c[x[y[i]]]++;
        for (int i = 0; i < m; i++) c[i] += c[i-1];
        for (int i = n-1; i >= 0; i--)sa[--c[x[y[i]]]] = y[i];
        swap(x, y);
        p = 1; x[sa[0]] = 0;
        for (int i = 1; i < n; i++) x[sa[i]] = y[sa[i-1]]== y[sa[i]] && y[sa[i-1]+k]== y[sa[i]+k] ? p-1 : p++;
        if (p >= n) break;
        m = p;
    }
}
int ran[maxn], height[maxn];
void getHeight() {
    int i, j, k = 0;
    for (i = 0; i < n; i++) ran[sa[i]] = i;
    for (i = 0; i < n; i++) {
        if (k) k--;
        int j = sa[ran[i]-1];
        while (i + k < n && j + k < n && s[i+k] == s[j+k]) k++;
        height[ran[i]] = k;
    }
}
char temp[1010];
int belong[maxn];
bool vis[110];
bool judge(int p) {
    memset(vis, 0, sizeof(vis));
    int cnt = 1;
    vis[belong[sa[0]]] = 1;
    for (int i = 1; i < n; i++) {
        if (height[i] < p) {
            memset(vis, 0, sizeof(vis));
            cnt = 1;
            vis[belong[sa[i]]] = 1;
        }
        else if (!vis[belong[sa[i]]]) {
            vis[belong[sa[i]]] = 1;
            cnt++;
        }
        if (cnt > num/2) return true;
    }
    return false;
}
vector<int> block[maxn];
string res;
vector<string> ans;
void output(int p) {
    for (int i = 0; i < n; i++) block[i].clear();
    memset(vis, 0, sizeof(vis));
    int cnt = 0;
    block[cnt].push_back(sa[0]);
    vis[belong[sa[0]]] = 1;
    for (int i = 1; i < n; i++) {
        if (height[i] < p) {
            cnt++;
            memset(vis, 0, sizeof(vis));
        }
        if (!vis[belong[sa[i]]]) {
            vis[belong[sa[i]]] = 1;
            block[cnt].push_back(sa[i]);
        }
    }
    ans.clear();
    for (int i = 0; i <= cnt; i++) {
        if (block[i].size() > num/2) {
 
            res.clear();
            for (int j = 0; j < p; j++) {
                res.push_back(s[block[i][0]+j]);
            }
            ans.push_back(res);
        }
    }
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++) cout << ans[i] << endl;
 
}
void solve() {
    bool ok = false;
    int l = 1, r = maxl;
    while (l <= r) {
        int mid = (l + r)>>1;
        if (judge(mid)) { l = mid + 1; ok = true; }
        else r = mid - 1;
    }
    if (ok) output(r);
    else puts("?");
}
int main() {
    int ks = 0;
    while (~scanf("%d", &num) && num) {
        if (num == 1) {
            scanf("%s", temp);
            if (ks++) puts("");
            puts(temp);
            continue;
        }
        n = maxl = 0;
        int cut = 1;
        for (int i = 0; i < num; i++) {
            scanf("%s", temp);
            int len = strlen(temp);
            maxl = max(maxl, len);
            for (int j = 0; j < len; j++) {
                belong[n] = i;
                s[n++] = temp[j];
            }
            belong[n] = i; s[n++] = cut++;
        }
        s[n] = '\0';
        build_sa(128);
        getHeight();
        if (ks++) puts("");
        solve();
    }
    return 0;
}
