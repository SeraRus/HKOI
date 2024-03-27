import java.util.Scanner;

public class program{
    public static void main(String[] args) {
        int a = 0, b = 0;
        Scanner scan = new Scanner(System.in);
        if (scan.hasNext()) {
            a = scan.nextInt();
            b = scan.nextInt();
        }
        System.out.println(a+b);
    }
}
