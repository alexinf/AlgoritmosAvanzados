#include <iostream>
#include <vector>
using namespace std;
int main()
{
	bool ch=false;
	vector <int> a;
	int n,max=0,temp=0,tte;
	cin >> n;
	while (n > 0)
	{
		max = 0; temp = 0; ch = false;
		a.resize(n);
		for (int i = 0; i < n; i++)
		{
			cin >> tte;
			cout << tte << endl;
			if (!ch)
			{
				if (tte>0)
					temp = tte;
				if (temp>max)
					max = temp;
				ch = true;
			}
			else
			{
				temp = temp + tte;
				if (temp < 0)
				{
					temp = 0;
					ch = false;
				}
				else
				{
					if (temp>max)
						max = temp;
				}
			}
		}
		
		if (max > 0)
			cout <<"The maximum winning streak is "<< max <<"."<< endl;
		else

			cout << "Losing streak." << endl;
		cin >> n;
	}
}
