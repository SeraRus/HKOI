import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if (scan.hasNextLine()) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            double c = scan.nextInt()*Math.PI/180;
            System.out.println(String.format("%.3f", 0.5*a*b*Math.sin(c)));
        }
    }
}
