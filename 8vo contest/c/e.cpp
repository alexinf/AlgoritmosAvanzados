#define ll long long
#define MOD 1000000007
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        sort(a,a+n);
        for(int b=0;b<n;b++)
        {
        	cout<<a[b];
		}
		cout<<"as"<<endl;
        int sum=1;
        int last=-1;
        for(int i=0;i<n;i++)
        {
 
 
            if(sum>=a[i])
            {
                last=i;
            }
            sum+=1;
 
 
 
        }
 
        cout<<last+2<<endl;
 
    }
 
 
}
