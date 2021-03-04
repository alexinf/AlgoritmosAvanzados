#include<iostream>
#include<string>
using namespace std;

void solve(string str)
{
    int count[130] = {0}; //????ASCII ?????
    int maxCount = 0; //???????ASCII

    for(int i = 0 ; i < str.length() ; i++)
    {
        count[str[i]]++;
        maxCount++;
    }

    //???????? ?1~maxCount????
    for(int j = 1 ; j <= maxCount ; j++)
    {
        //?ASCII CODE??????????
        for(int i = 128  ; i >= 32 ; i--)
        {
            if(count[i] == j)
                cout << i << " " << j << endl;
        }
    }

}
int main()
{
    string str;
    bool flag = false;
    while(getline(cin , str))
    {
        if(flag)
            cout << endl;

        solve(str);
        flag = true;
    }
    return 0;
}
