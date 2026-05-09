import java.util.Random;
import java.util.Scanner;

public class SimpleArithmeticApp {
    public static void main(String... args) {
        Random randomGenerator = new Random();
        Scanner inputCollector = new Scanner(System.in);

        int count = 0;
        int score = 0;

        do {
            int firstNumber = randomGenerator.nextInt(100);
            int secondNumber = randomGenerator.nextInt(100);

            int result = 0;
            int userResponse = 0;
            int attemptCount = 0;

            while(attemptCount < 2) {
                if(firstNumber > secondNumber) {
                    result = firstNumber - secondNumber;
                    System.out.printf("What is %d - %d? ", firstNumber, secondNumber);
                } else {
                    result = secondNumber - firstNumber;
                    System.out.printf("What is %d - %d? ", secondNumber, firstNumber);
                }
                userResponse = inputCollector.nextInt();

                if(result == userResponse) {
                    System.out.println("Correct!!!");
                    score++;
                    break;
                } else {
                    System.out.println("Wrong. Try again!");
                }

                attemptCount++;
            }

            System.out.println();

            count++;
        } while(count < 10);

        System.out.printf("You got %d out of 10.%n", score);
    }
}