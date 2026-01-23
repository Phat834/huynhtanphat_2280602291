package lab7;

import java.util.Scanner;

public class b112 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Number Guessing Game ===");
        System.out.println("I'm thinking of a number between 1 and 100");
        
        // Generate a random number between 1 and 100
        int secretNumber = (int) (Math.random() * 100) + 1;
        int attempts = 0;
        boolean hasGuessed = false;
        
        while (!hasGuessed) {
            System.out.print("\nEnter your guess: ");
            int guess = scanner.nextInt();
            attempts++;
            
            if (guess < 1 || guess > 100) {
                System.out.println("Please enter a number between 1 and 100!");
                continue;
            }
            
            if (guess < secretNumber) {
                System.out.println("Too low! Try a higher number.");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try a lower number.");
            } else {
                hasGuessed = true;
                System.out.println("\nCongratulations! You guessed the number " + secretNumber + " in " + attempts + " attempts!");
                
                // Provide feedback based on performance
                if (attempts <= 5) {
                    System.out.println("Excellent! You're a mind reader!");
                } else if (attempts <= 10) {
                    System.out.println("Great job! You have a good intuition.");
                } else if (attempts <= 15) {
                    System.out.println("Not bad! With a little more practice you'll be great.");
                } else {
                    System.out.println("Better luck next time! The number was " + secretNumber);
                }
            }
        }
        
        scanner.close();
    }
}
