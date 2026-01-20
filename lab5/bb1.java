package lab5;

import java.util.Scanner;

public class bb1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Nhập số thứ nhất: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Nhập số thứ hai: ");
        double num2 = scanner.nextDouble();
        
        System.out.println("Tổng: " + (num1 + num2));
        System.out.println("Hiệu: " + (num1 - num2));
        System.out.println("Tích: " + (num1 * num2));
        System.out.println("Thương: " + (num1 / num2));
        
        scanner.close();
    }
}
