package model;

import java.sql.Timestamp;

public class TransaksiStok {
    private int idTransaksi;
    private int idBarang;
    private String jenisTransaksi; // "masuk" atau "keluar"
    private int jumlah;
    private Timestamp tanggalTransaksi;
    private String keterangan;

    // Constructor
    public TransaksiStok(int idTransaksi, int idBarang, String jenisTransaksi, int jumlah, Timestamp tanggalTransaksi, String keterangan) {
        this.idTransaksi = idTransaksi;
        this.idBarang = idBarang;
        this.jenisTransaksi = jenisTransaksi;
        this.jumlah = jumlah;
        this.tanggalTransaksi = tanggalTransaksi;
        this.keterangan = keterangan;
    }

    // Getter and Setter
    public int getIdTransaksi() {
        return idTransaksi;
    }

    public void setIdTransaksi(int idTransaksi) {
        this.idTransaksi = idTransaksi;
    }

    public int getIdBarang() {
        return idBarang;
    }

    public void setIdBarang(int idBarang) {
        this.idBarang = idBarang;
    }

    public String getJenisTransaksi() {
        return jenisTransaksi;
    }

    public void setJenisTransaksi(String jenisTransaksi) {
        this.jenisTransaksi = jenisTransaksi;
    }

    public int getJumlah() {
        return jumlah;
    }

    public void setJumlah(int jumlah) {
        this.jumlah = jumlah;
    }

    public Timestamp getTanggalTransaksi() {
        return tanggalTransaksi;
    }

    public void setTanggalTransaksi(Timestamp tanggalTransaksi) {
        this.tanggalTransaksi = tanggalTransaksi;
    }

    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
}
