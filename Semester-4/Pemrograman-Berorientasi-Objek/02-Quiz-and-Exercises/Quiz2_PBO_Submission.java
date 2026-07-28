package latihanpercabangan;

import java.util.Scanner;

public class asdos {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Masukkan tinggi piramid: ");
        int tinggi = sc.nextInt();

        for (int i = 1; i <= tinggi; i++) {

            for (int j = tinggi - i; j > 0; j--) {
                System.out.print(" ");
            }

            if (i == 1) {
                System.out.println("0");
            } else if (i == 2) {
                System.out.println("0|0");
            } else {
                System.out.print("0");
                for (int k = 1; k <= i - 2; k++) {
                    System.out.print("*");
                }
                System.out.print("|");
                for (int k = 1; k <= i - 2; k++) {
                    System.out.print("*");
                }
                System.out.println("0");
            }
        }
    }
}
