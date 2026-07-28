package model;

import java.sql.Timestamp;

public class Notifikasi {
    private int idNotifikasi;
    private int idBarang;
    private String pesan;
    private String status; // "belum_dibaca" atau "dibaca"
    private Timestamp tanggalNotifikasi;

    // Constructor
    public Notifikasi(int idNotifikasi, int idBarang, String pesan, String status, Timestamp tanggalNotifikasi) {
        this.idNotifikasi = idNotifikasi;
        this.idBarang = idBarang;
        this.pesan = pesan;
        this.status = status;
        this.tanggalNotifikasi = tanggalNotifikasi;
    }

    // Getter and Setter
    public int getIdNotifikasi() {
        return idNotifikasi;
    }

    public void setIdNotifikasi(int idNotifikasi) {
        this.idNotifikasi = idNotifikasi;
    }

    public int getIdBarang() {
        return idBarang;
    }

    public void setIdBarang(int idBarang) {
        this.idBarang = idBarang;
    }

    public String getPesan() {
        return pesan;
    }

    public void setPesan(String pesan) {
        this.pesan = pesan;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Timestamp getTanggalNotifikasi() {
        return tanggalNotifikasi;
    }

    public void setTanggalNotifikasi(Timestamp tanggalNotifikasi) {
        this.tanggalNotifikasi = tanggalNotifikasi;
    }
}
