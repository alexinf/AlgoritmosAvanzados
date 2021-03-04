#include <bits/stdc++.h>
using namespace std;

void solve(){
	int n, m , k; cin>> n >> m >> k;
	int a = min(m,n/k);
	int b = (m-a+k-2)/(k-1);
	cout<<a<<endl;
	cout<<b<<endl;
	cout<<a-b<<endl;
}

int main (){
	int t; cin >> t;
	while(t--) solve();
}
