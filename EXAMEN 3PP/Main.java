
import java.util.*;

public class Main {

     class  Punto{
        public double x;
        public double y;
        public Punto(double x, double y){
            this.x = x;
            this.y = y;
        }
        public String toString(){
            return "x: "+ this.x  + ", y: "+ this.y;
        }
    }

    class Linea{
        public Punto a;
        public Punto b;
        public Linea(Punto a,Punto b){
            this.a = a;
            this.b = b;
        }
        public String toString(){
            return "a: "+ this.a  + ", b: "+ this.b;
        }
    }

    public Punto rotate(Punto origen, Punto point, double angle){
         double ox, oy, px, py, qx, qy;
         ox = origen.x;
         oy = origen.y;
         px = point.x;
         py = point.y;
         qx = ox + Math.cos(angle) * (px - ox) - Math.sin(angle) * (py - oy);
         qy = oy + Math.sin(angle) * (px - ox) + Math.cos(angle) * (py - oy);
         return new Punto(qx, qy);
    }

    public double det(Punto a, Punto b){
        return a.x * b.y - a.y * b.x;
    }

    public Punto interception(Linea line1, Linea line2){
        Punto xdiff, ydiff, d;
        double div, x, y;
        xdiff = new Punto(line1.a.x - line1.b.x, line2.a.x - line2.b.x);
        ydiff = new Punto(line1.a.y - line1.b.y, line2.a.y - line2.b.y);

        div = this.det(xdiff, ydiff);
        d = new Punto(det(line1.a, line1.b), det(line2.a, line2.b));
        x = det(d, xdiff)/div;
        y = det(d, ydiff)/div;
        return new Punto(x, y);
    }

    public double areaPoligono (Punto[] coordenadas){
        int n = coordenadas.length-1;
        double[] x = new double[n];
        double[] y = new double[n];
        double sum;

        for (int i =0;i<n; i++){

            x[i] = coordenadas[i].x;
            y[i] = coordenadas[i].y;
        }
        sum = x[0]*y[n-1] - x[n-1]*y[0];
        for (int i =0;i<n-1; i++){
            sum += x[i+1]*y[i] - x[i]*y[i+1];
        }
        return sum/2;
    }


    public void resolver(){
        Scanner tect = new Scanner(System.in);
        int n = tect.nextInt();
        double x,y, areaTriangulo, areaPoligono, areaFinal;
        Punto[] triangulo = new Punto[4];
        Punto[] poligono = new Punto[7];

        Punto A, B, C, A1, B1, C1, centro, I_C1_B, I_B_A1, I_A1_C, I_C_B1, I_B1_A, I_A_C1;

        for(int i=0; i<n; i++){
            x = Double.parseDouble(tect.next());
            y = Double.parseDouble(tect.next());
            A = new Punto(x,y);

            x = Double.parseDouble(tect.next());
            y = Double.parseDouble(tect.next());
            B = new Punto(x,y);

            x = Double.parseDouble(tect.next());
            y = Double.parseDouble(tect.next());
            C = new Punto(x,y);

            x = Double.parseDouble(tect.next());
            y = Double.parseDouble(tect.next());
            centro = new Punto(x,y);

            A1 = this.rotate(centro, A,Math.toRadians(180) );
            B1 = this.rotate(centro, B,Math.toRadians(180) );
            C1 = this.rotate(centro, C,Math.toRadians(180) );

            I_C1_B = interception(new Linea(A,B), new Linea(C1, A1));
            I_B_A1 = interception(new Linea(B,C), new Linea(C1, A1));
            I_A1_C = interception(new Linea(B1,A1), new Linea(B, C));
            I_C_B1 = interception(new Linea(A,C), new Linea(B1, A1));
            I_B1_A = interception(new Linea(C1,B1), new Linea(A, C));
            I_A_C1 = interception(new Linea(C1,B1), new Linea(A, B));

            triangulo[0] = A;
            triangulo[1] = B;
            triangulo[2] = C;
            triangulo[3] = A;

            poligono[0] = I_C1_B;
            poligono[1] = I_B_A1;
            poligono[2] = I_A1_C;
            poligono[3] = I_C_B1;
            poligono[4] = I_B1_A;
            poligono[5] = I_A_C1;
            poligono[6] = I_C1_B;

            areaTriangulo = this.areaPoligono(triangulo);
            areaPoligono = this.areaPoligono(poligono);

            areaFinal = areaTriangulo - areaPoligono;
            String salida = String.format("%.2f", areaFinal);
            salida = salida.replace(",",".");
            System.out.println(salida);
        }
    }

    public static void main(String[] args) {
        Main m = new Main();
        m.resolver();
    }
}
