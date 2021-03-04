#include<stdio.h>
#include<math.h>
double l, w, eps=1e-6;
int main(){
	while( scanf("%lf %lf",&l,&w)==2 )
		printf("%.3lf\n", sqrt(l*l+w*w-w*l));
		printf("%.3lf 0.000 %.3lf\n", ( l+w - sqrt( l*l+w*w-w*l) )/6.0 + eps,  (l<w ? l/2.0 : w/2.0)+eps );
}
