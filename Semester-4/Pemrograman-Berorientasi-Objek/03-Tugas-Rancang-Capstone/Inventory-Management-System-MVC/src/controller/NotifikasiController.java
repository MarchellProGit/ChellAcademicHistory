package controller;

import model.Notifikasi;
import config.DatabaseConnection;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class NotifikasiController {
    public List<Notifikasi> getAllNotifikasi() {
        List<Notifikasi> notifikasiList = new ArrayList<>();
        try (Connection conn = DatabaseConnection.getConnection()) {
            String query = "SELECT * FROM tb_notifikasi";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                notifikasiList.add(new Notifikasi(
                    rs.getInt("id_notifikasi"),
                    rs.getInt("id_barang"),
                    rs.getString("pesan"),
                    rs.getString("status"),
                    rs.getTimestamp("tanggal_notifikasi")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return notifikasiList;
    }
}
