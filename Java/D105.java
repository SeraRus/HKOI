import java.util.ArrayList;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<Integer> d1 = new ArrayList<>();
        ArrayList<Integer> d2 = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            d1.add(scanner.nextInt());
        }

        for (int i = 0; i < 3; i++) {
            d2.add(scanner.nextInt());
        }

        if (compareDates(d1, d2) > 0) {
            System.out.println("After");
        } else if (compareDates(d1, d2) < 0) {
            System.out.println("Before");
        } else {
            System.out.println("Same");
        }
    }

    public static int compareDates(ArrayList<Integer> d1, ArrayList<Integer> d2) {
        for (int i = 0; i < 3; i++) {
            if (d1.get(i) > d2.get(i)) {
                return 1;
            } else if (d1.get(i) < d2.get(i)) {
                return -1;
            }
        }
        return 0;
    }
}
