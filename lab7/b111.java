package lab7;

import java.util.Scanner;

public class b111 {
    public static void main(String[] args) {
        System.out.println("Test file for lab7 ne 1234567890");
        System.err.println("Error output for lab7 ne 1234567890");
        
        // Calculator feature
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("\n=== Simple Calculator ===");
        System.out.println("Available operations:");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");
        System.out.println("5. Exit");
        
        while (true) {
            System.out.print("\nEnter your choice (1-5): ");
            int choice = scanner.nextInt();
            
            if (choice == 5) {
                System.out.println("Exiting calculator...");
                break;
            }
            
            if (choice < 1 || choice > 5) {
                System.out.println("Invalid choice. Please try again.");
                continue;
            }
            
            System.out.print("Enter first number: ");
            double num1 = scanner.nextDouble();
            
            System.out.print("Enter second number: ");
            double num2 = scanner.nextDouble();
            
            double result = 0;
            String operator = "";
            
            switch (choice) {
                case 1:
                    result = num1 + num2;
                    operator = "+";
                    break;
                case 2:
                    result = num1 - num2;
                    operator = "-";
                    break;
                case 3:
                    result = num1 * num2;
                    operator = "*";
                    break;
                case 4:
                    if (num2 == 0) {
                        System.out.println("Error: Division by zero!");
                        continue;
                    }
                    result = num1 / num2;
                    operator = "/";
                    break;
            }
            
            System.out.printf("Result: %.2f %s %.2f = %.2f\n", num1, operator, num2, result);
        }
        
        scanner.close();
    }
}