package main;

import warung.Warungmakan;
import warung.Warungroti;
import barang.Barang;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Warungmakan wm = new Warungmakan();
        Warungroti wr = new Warungroti();

        while (true) {
            System.out.println("=== KANTIN MARCHELL ===");
            System.out.println("1. Warung Makanan");
            System.out.println("2. Warung Roti");
            System.out.println("3. Exit");
            System.out.print("Masukkan Pilihan: ");
            int pilihan = sc.nextInt();
            sc.nextLine();

            switch (pilihan) {
                case 1:
                    menuWarungMakan(sc, wm);
                    break;
                case 2:
                    menuWarungRoti(sc, wr);
                    break;
                case 3:
                    System.out.println("\n2024 | Marchell Adi Pratama - 672023081");
                    sc.close();
                    return;
                default:
                    System.out.println("Pilihan tidak valid. Silahkan coba lagi");
            }
        }
    }

    private static void menuWarungMakan(Scanner sc, Warungmakan wm) {
        while (true) {
            System.out.println("\n=== Warung Makanan ===");
            System.out.println("1. Lihat Stok");
            System.out.println("2. Tambah Stok");
            System.out.println("3. Jual Barang");
            System.out.println("4. Isi Ulang Gas");
            System.out.println("5. Hitung Omset");
            System.out.println("6. Exit");
            System.out.print("Masukkan Pilihan: ");
            int pilihan = sc.nextInt();
            sc.nextLine();

            switch (pilihan) {
                case 1:
                    for (Barang b : wm.tampilkanMenu()) {
                        System.out.println(b.getNama() + " Stock: " + b.getStok());
                    }
                    break;
                case 2:
                    for (int i = 0; i < wm.tampilkanMenu().size(); i++) {
                        System.out.println((i + 1) + ". " + wm.tampilkanMenu().get(i).getNama());
                    }
                    System.out.print("Pilih barang yang mau ditambah stok: ");
                    int barangPilihan = sc.nextInt();
                    System.out.println("Stok Terkini: " + wm.tampilkanMenu().get(barangPilihan - 1).getStok());
                    sc.nextLine();
                    System.out.print("Jumlah Penambahan: ");
                    int jumlah = sc.nextInt();
                    System.out.println("Stok Terbaru: " + (wm.tampilkanMenu().get(barangPilihan - 1).getStok() + jumlah));
                    sc.nextLine();
                    wm.tambahStok(wm.tampilkanMenu().get(barangPilihan - 1), jumlah);
                    break;
                case 3:
                    for (int i = 0; i < wm.tampilkanMenu().size(); i++) {
                        System.out.println((i + 1) + ". " + wm.tampilkanMenu().get(i).getNama() + " (Rp. " + wm.tampilkanMenu().get(i).getHarga() + ")");
                    }
                    System.out.print("Pilih barang yang mau dijual: ");
                    barangPilihan = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Jumlah Penjualan: ");
                    jumlah = sc.nextInt();
                    sc.nextLine();
                    if (wm.jualBarang(wm.tampilkanMenu().get(barangPilihan - 1), jumlah)) {
                        System.out.println("Jumlah Transaksi: Rp. " + (wm.tampilkanMenu().get(barangPilihan - 1).getHarga() * jumlah));
                    } else {
                        System.out.println("Stok tidak mencukupi");
                    }
                    break;
                case 4:
                    System.out.println("Gas Saat Ini: " + wm.getGas());
                    System.out.print("Ingin Isi Ulang Gas? (Biaya = 22000) (y/n): ");
                    String isiUlang = sc.nextLine();
                    if (isiUlang.equals("y")) {
                        wm.isiUlangGas();
                        System.out.println("Gas telah diisi ulang");
                    } else {
                        System.out.println("Gas tidak diisi ulang");
                    }
                    break;
                case 5:
                    System.out.println("Omset Dari Warung Makanan: Rp. " + wm.getOmset());
                    break;
                case 6:
                    return;
                default:
                    System.out.println("Pilihan tidak valid. Silahkan coba lagi");
            }
        }
    }

    private static void menuWarungRoti(Scanner sc, Warungroti wr) {
        while (true) {
            System.out.println("\n=== Warung Roti ===");
            System.out.println("1. Lihat Stok");
            System.out.println("2. Tambah Barang");
            System.out.println("3. Jual Menu");
            System.out.println("4. Hitung Omset");
            System.out.println("5. Exit");
            System.out.print("Masukkan Pilihan: ");
            int pilihan = sc.nextInt();
            sc.nextLine();

            switch (pilihan) {
                case 1:
                    for (Barang b : wr.tampilkanMenu()) {
                        System.out.println(b.getNama() + " Stock: " + b.getStok());
                    }
                    break;
                case 2:
                    for (int i = 0; i < wr.tampilkanMenu().size(); i++) {
                        System.out.println((i + 1) + ". " + wr.tampilkanMenu().get(i).getNama());
                    }
                    System.out.print("Pilih barang yang mau ditambah stok: ");
                    int barangPilihan = sc.nextInt();
                    System.out.println("Stok Terkini: " + wr.tampilkanMenu().get(barangPilihan - 1).getStok());
                    sc.nextLine();
                    System.out.print("Jumlah Penambahan: ");
                    int jumlah = sc.nextInt();
                    System.out.println("Stok Terbaru: " + (wr.tampilkanMenu().get(barangPilihan - 1).getStok() + jumlah));
                    sc.nextLine();
                    wr.tambahStok(wr.tampilkanMenu().get(barangPilihan - 1), jumlah);
                    break;
                case 3:
                    for (int i = 0; i < wr.tampilkanMenu().size(); i++) {
                        System.out.println((i + 1) + ". " + wr.tampilkanMenu().get(i).getNama() + " (Rp. " + wr.tampilkanMenu().get(i).getHarga() + ")");
                    }
                    System.out.print("Pilih barang yang mau dijual: ");
                    barangPilihan = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Jumlah Penjualan: ");
                    jumlah = sc.nextInt();
                    sc.nextLine();
                    if (wr.jualBarang(wr.tampilkanMenu().get(barangPilihan - 1), jumlah)) {
                        System.out.println("Jumlah Transaksi: " + (wr.tampilkanMenu().get(barangPilihan - 1).getHarga() * jumlah));
                    } else {
                        System.out.println("Stok tidak mencukupi");
                    }
                    break;
                case 4:
                    System.out.println("Omset Dari Warung Roti: Rp. " + wr.getOmset());
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Pilihan tidak valid. Silahkan coba lagi");
            }
        }
    }
}
