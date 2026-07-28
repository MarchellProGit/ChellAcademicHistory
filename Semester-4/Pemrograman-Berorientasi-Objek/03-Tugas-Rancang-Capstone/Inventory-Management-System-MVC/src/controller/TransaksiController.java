package controller;

import model.TransaksiStok;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Timestamp;
import javax.swing.table.DefaultTableModel;

public class TransaksiController {

    public Statement stm;
    public ResultSet res;
    public String sql;

    DefaultTableModel dtm = new DefaultTableModel();

    public TransaksiController() {
        Koneksi Kn = new Koneksi();
        Kn.config();
        this.stm = Kn.stm;
    }

    public DefaultTableModel buatTabel() {
        dtm.addColumn("ID Transaksi");
        dtm.addColumn("ID Barang");
        dtm.addColumn("Jenis Transaksi");
        dtm.addColumn("Jumlah");
        dtm.addColumn("Tanggal Transaksi");
        dtm.addColumn("Keterangan");
        return dtm;
    }

    public void tampilkanData() {
        try {
            dtm.getDataVector().removeAllElements();
            dtm.fireTableDataChanged();

            this.sql = "SELECT * FROM tb_transaksi_stok";

            res = stm.executeQuery(sql);

            while (res.next()) {
                Object[] obj = new Object[6];
                obj[0] = res.getString("id_transaksi");
                obj[1] = res.getString("id_barang");
                obj[2] = res.getString("jenis_transaksi");
                obj[3] = res.getString("jumlah");
                obj[4] = res.getString("tanggal_transaksi");
                obj[5] = res.getString("keterangan");

                dtm.addRow(obj);
            }
        } catch (Exception e) {
            System.out.println("Gagal Query" + e);
        }
    }

    public boolean tambahData(int id, String jenis, int jum, Timestamp tanggal, String ket) {
        //Hubungkan dengan model
        TransaksiStok ts = new TransaksiStok();
        ts.setIdBarang(id);
        ts.setJenisTransaksi(jenis);
        ts.setJumlah(jum);
        ts.setTanggalTransaksi(tanggal);
        ts.setKeterangan(ket);

        try {
            this.sql = "INSERT INTO tb_transaksi_stok (id_barang, jenis_transaksi, jumlah, tanggal_transaksi, keterangan) "
                    + "VALUES (" + ts.getIdBarang() + ", '" + ts.getJenisTransaksi() + "', " + ts.getJumlah() + ", '" + ts.getTanggalTransaksi() + "', '" + ts.getKeterangan() + "')";

            this.stm.executeUpdate(sql);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public String prosesTambahData(int id, String jenis, int jumlah, Timestamp tanggal, String keterangan) {
        if (jumlah <= 0) {
            return "Jumlah harus lebih dari 0.";
        }
        if (keterangan.isEmpty()) {
            return "Keterangan tidak boleh kosong.";
        }

        boolean success = tambahData(id, jenis, jumlah, tanggal, keterangan);
        if (success) {
            return "Transaksi berhasil ditambahkan.";
        } else {
            return "Gagal menambahkan transaksi. Silakan coba lagi.";
        }
    }

}
