import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if (scan.hasNextLine()) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = scan.nextInt();

            double delta = b*b-4*a*c;
            double x, y;

            if (delta < 0) {
                System.out.println("None");
            } else if (delta == 0) {
                x = (-b + Math.sqrt(delta)) / (2*a);
                System.out.println(String.format("%.3f", x));
            } else {
                x = (-b + Math.sqrt(delta)) / (2*a);
                y = (-b - Math.sqrt(delta)) / (2*a);
                if (x < y) {
                    System.out.println(String.format("%.3f", x) + " " + String.format("%.3f", y));
                } else {
                    System.out.println(String.format("%.3f", y) + " " + String.format("%.3f", x));
                }
            }
        }
    }
}
