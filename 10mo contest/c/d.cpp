#include<bits/stdc++.h>
using namespace std;


int main(){

	int tc, n; cin>>tc;  vector<pair<int, int>>result;

	for(int t=1; t<=tc; t++){

		cin>>n; int h[n]; 
		
		for(int i=0;i<n;i++)cin>>h[i];   
		
		int w[n]; 
		
		for(int i=0;i<n;i++)cin>>w[i];

		int LIS[n]; 
		for(int i=0;i<n;i++)LIS[i] = w[i]; 

		for(int i=1; i<n; i++){
			for(int j=0; j<i; j++){
				if(h[j]<h[i])LIS[i] = max(LIS[i], LIS[j]+w[i]);
			}
		}


		int DIS[n]; for(int i=0;i<n;i++)DIS[i] = w[i]; //LIS[0] = 1;

		for(int i=1; i<n; i++){
			for(int j=0; j<i; j++){
				if(h[j]>h[i])DIS[i] = max(DIS[i], DIS[j]+w[i]);
			}
		}

		int inc = -1;
		for(int i=0;i<n;i++)inc = max(inc, LIS[i]);

		nt dec = -1;
		for(int i=0;i<n;i++)dec = max(dec, DIS[i]);


		if(inc >=  dec)
			printf("Case %d. Increasing (%d). Decreasing (%d).\n", t, inc, dec);
		else
			printf("Case %d. Decreasing (%d). Increasing (%d).\n", t, dec, inc);

}

}

