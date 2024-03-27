import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if (scan.hasNext()) {
            double a = Float.parseFloat(scan.next().substring(1));
            System.out.println('$' + String.format("%.1f", (a+0.05)/2));
        }
    }
}
