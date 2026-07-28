package config;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    // Konstanta untuk konfigurasi database
    private static final String DB_URL = "jdbc:mysql://localhost:3306/db_gudang"; // Ganti dengan nama database Anda
    private static final String DB_USER = "root"; // Ganti dengan username MySQL Anda
    private static final String DB_PASSWORD = ""; // Ganti dengan password MySQL Anda

    // Objek koneksi tunggal (Singleton)
    private static Connection connection;

    /**
     * Metode untuk mendapatkan koneksi ke database.
     * @return Connection - Objek koneksi ke database
     */
    public static Connection getConnection() {
        if (connection == null) {
            try {
                // Register driver JDBC
                Class.forName("com.mysql.cj.jdbc.Driver");
                // Membuat koneksi
                connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
                System.out.println("Koneksi ke database berhasil!");
            } catch (ClassNotFoundException e) {
                System.err.println("Driver JDBC tidak ditemukan: " + e.getMessage());
            } catch (SQLException e) {
                System.err.println("Gagal terhubung ke database: " + e.getMessage());
            }
        }
        return connection;
    }

    /**
     * Metode untuk menutup koneksi.
     */
    public static void closeConnection() {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("Koneksi ke database ditutup!");
            } catch (SQLException e) {
                System.err.println("Gagal menutup koneksi database: " + e.getMessage());
            }
        }
    }
}
