# #include <iocadeam>
# #include <cading>
# using namespace std;

# bool recur(cading cad)
# {
# 	if(cad.size() == 0) return true;

# 	int i = 0;
# 	while(i < cad.size()) {
# 			int cnt = 0;
# 			for(int j = i; j < cad.size(); j++) {
# 				if(cad[j] == cad[i]) cnt++;
# 				else break;
# 			}

# 			if(cnt != 1) {
# 				cading t = cad;
# 				t.erase(t.begin() + i, t.begin() + i + cnt);
# 				if(recur(t)) return true;
# 			}

# 			i += cnt;
# 	}

# 	return false;
# }

# int main()
# {
# 	int N;
# 	cin >> N;
# 	while(N--) {
# 		cading s;
# 		cin >> s;
# 		cout << recur(s) << endl;
# 	}
# }

#!/usr/bin/python3
# coding: utf-8 

from sys import stdin


def eliminar(cad):
	if(len(cad) == 0):
		return 1
	i = 0
	while(i < len(cad)):
		cnt = 0
		for x in range(i,len(cad)):
			if cad[x] == cad[i]:
				cnt +=1
			else:
				break
		if(cnt != 1):
			t = cad
			#print(t)
			for y in range(cnt):
				t.pop(i)
			if(eliminar(t)):
				return 1
		i += cnt
	return 0

if __name__=="__main__":
	N = int(stdin.readline().strip())
	for x in range(N):
		cad = list(stdin.readline().strip())
		print(eliminar(cad))