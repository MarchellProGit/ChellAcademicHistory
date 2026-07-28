package controller;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;

public class Koneksi {
    public Connection con;
    public Statement stm;
    
    public void config(){
        try {
            String url = "jdbc:mysql://localhost:3306/db_gudang";
            String user = "root";
            String pass = "";
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            //String connection
            con = DriverManager.getConnection(url, user, pass);
            //mempersiapkan variabel untuk SQL statement
            stm = (Statement) con.createStatement();
            System.out.println("Koneksi berhasil...");
        } catch (Exception e) {
            System.out.println("Koneksi Gagal" +e);
        }
    }
}
