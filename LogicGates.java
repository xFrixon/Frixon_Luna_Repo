import java.util.InputMismatchException;
import java.util.Scanner;

public class LogicGates {
    
    public static void main(String[] args) {
        int option1;
        int option2;
        boolean valid=false;
        Scanner read = new Scanner (System.in);
        do {
            try {
                System.out.println("What is the weather like in the first room?");
                System.out.println("0. It's cold");
                System.out.println("1. It's hot");
                option1 = read.nextInt();
                System.out.println("What is the weather like in the second room?");
                System.out.println("0. It's cold");
                System.out.println("1. It's hot");
                option2 = read.nextInt();
                valid = true;
                if (answer(option1, option2) == 1) {
                    System.out.println("The air conditioning has been turned on");
                } else {
                    System.out.println("The air conditioning has been turned off");
                }
            } catch (InputMismatchException exception) {
                System.out.println("Only numbers");
                read.next();
            }
        } while (!valid);
        read.close();
    }
    
    public static int answer (int option1, int option2) {
        int result=0;
        if (option1==1 && option2==1) {
            result=1;
        }
        return result;
    }
}
