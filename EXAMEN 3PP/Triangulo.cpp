#include <stdio.h>
#include <math.h> 
#define PI 3.141592653589793
struct Point
{
    float x, y;
    Point() {};
    Point(float _x, float _y)
    {
        x = _x, y = _y;
    }
};
Point RotarPunto(Point &origen, Point &point, int angulo){
	double qx,qy;
	qx = origen.x + cos(angulo * PI / 180) * (point.x - origen.x) - sin(angulo * PI / 180) * (point.y - origen.y);
    qy = origen.y + sin(angulo * PI / 180) * (point.x - origen.x) + cos(angulo * PI / 180) * (point.y - origen.y);
	return Point (qx,qy);
}

double AreaTriangulo(Point &A,Point &B,Point &C){
	double  a1,a,b1,b,c1,c,p,Ax,Area;
	a1 = pow((B.y - A.y),2)+ pow((B.x - A.x),2);
	a = sqrt(a1);
	b1 = pow((C.y - B.y),2)+ pow((C.x - B.x),2);
	b = sqrt(b1);
	c1 = pow((C.y- A.y),2)+ pow((C.x - A.x),2);
	c = sqrt(c1);
	p = (a+b+c)/2.0;
	Ax = p*(p-a)*(p-b)*(p-c);
	Area = sqrt(Ax);
	//printf ("%f\n", Area);
	return Area;
}
double Det(Point &a, Point &b){
        return a.x * b.y - a.y * b.x;
}
Point Interseccion(Point &A,Point &AA,Point &B,Point &BB){
	double  div,x,y;
	Point xx(A.x-AA.x, B.x-BB.x);
	Point yy(A.y-AA.y, B.y-BB.y);
	div = Det(xx,yy);
	Point d(Det(A,AA),Det(B,BB));
	x = Det(d,xx)/div;
	y = Det(d,yy)/div;
	return Point(x,y);
}

int main()
{
    int t;
    double  area;
    scanf("%d", &t);
    while(t--)
    {	
    	area = 0;
        Point A(0, 0);
        Point B(0, 0);
        Point C(0, 0);
        Point r(0, 0);
        scanf("%e %e %e %e %e %e %e %e", &A.x, &A.y,&B.x, &B.y,&C.x, &C.y,&r.x, &r.y);
    	Point A1 =RotarPunto(r, A, 180);
		Point B1 =RotarPunto(r, B, 180);
		Point C1 =RotarPunto(r, C, 180);
		Point T1A = Interseccion(A1,C1,B,C);
		Point T1B = Interseccion(A1,C1,B,A);
		area += AreaTriangulo(T1A,T1B,B);
		Point T2A = Interseccion(B1,C1,A,B);
		Point T2B = Interseccion(B1,C1,A,C);
		area += AreaTriangulo(T2A,T2B,A);
		Point T3A = Interseccion(B1,A1,C,B);
		Point T3B = Interseccion(B1,A1,C,A);
		area += AreaTriangulo(T3A,T3B,C);
		printf ("%.2f\n", area);
    }
    return 0;
}
