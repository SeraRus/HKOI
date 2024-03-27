import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if (scan.hasNext()) {
            String a = scan.next();
            if ( a.charAt(0) == '2' || a.charAt(0) == '3') {
                System.out.println("Fixed");
            } else {
                System.out.println("Mobile");
            }
        }
    }
}
