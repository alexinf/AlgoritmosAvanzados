import java.util.Scanner;
import java.util.ArrayList;

public class Main
{
    public static void main(String[] arg){
        Scanner read = new Scanner(System.in);
        int n = read.nextInt();
        int ct , report, time_ct, time_report, lessons;
        int time_used = 0;
        
        ArrayList<Integer> animate = new ArrayList();
        
        for(int i = 0; i < n ; i++){
            ct = read.nextInt();
            report = read.nextInt();
            time_ct = read.nextInt();
            time_report = read.nextInt();
            lessons = read.nextInt();
            time_used += ct*time_ct + report*time_report + lessons + 10;
            if (time_used < 24){
                animate.add(0);
            }
            else{
                animate.add(1);
            }
            time_used = 0;
        }
        for(int i =0; i < animate.size(); i++){
            if(animate.get(i) == 1){
                System.out.println("Hotash");
            }
            else{
                System.out.println("Khushi");
            }
        }
        
    }
}