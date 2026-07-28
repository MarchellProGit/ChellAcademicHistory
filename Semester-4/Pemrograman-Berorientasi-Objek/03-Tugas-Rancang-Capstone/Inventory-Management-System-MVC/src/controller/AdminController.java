package controller;

import model.Admin;
import config.DatabaseConnection;
import java.sql.Connection;

import java.sql.ResultSet;
import java.sql.Statement;

public class AdminController {
    public Statement stm;
    public ResultSet res;
    public String sql;
    
    //konstruktor
    public AdminController() {
        // Mendapatkan koneksi menggunakan DatabaseConnection
        try {
            Connection con = DatabaseConnection.getConnection();
            this.stm = con.createStatement();
        } catch (Exception e) {
            System.out.println("Gagal membuat statement: " + e.getMessage());
        }
    }
    
    public boolean cekLogin(String a, String b) {
        Admin ad = new Admin();
        ad.setUsername(a);
        ad.setPassword(b);
        boolean status = false;

        try {
            // Query untuk mengecek apakah username dan password ada di database
            this.sql = "SELECT * FROM tb_admin WHERE username='" + ad.getUsername() + "' AND password='" + ad.getPassword() + "'";
            
            // Menjalankan query SELECT menggunakan executeQuery
            res = stm.executeQuery(sql);
            
            if (res.next()) {
                status = true;  // Login berhasil
            }
        } catch (Exception e) {
            System.out.println("Gagal Query: " + e);
        }
        return status;
    }
}
