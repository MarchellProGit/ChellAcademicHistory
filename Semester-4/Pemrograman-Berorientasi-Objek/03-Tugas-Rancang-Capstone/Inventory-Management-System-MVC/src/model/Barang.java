package model;

public class Barang {
    private int idBarang;
    private String namaBarang;
    private String kategoriBarang;
    private int stok;
    private int stokMinimum;
    private double hargaSatuan;

    // Constructor
    public Barang(int idBarang, String namaBarang, String kategoriBarang, int stok, int stokMinimum, double hargaSatuan) {
        this.idBarang = idBarang;
        this.namaBarang = namaBarang;
        this.kategoriBarang = kategoriBarang;
        this.stok = stok;
        this.stokMinimum = stokMinimum;
        this.hargaSatuan = hargaSatuan;
    }

    // Getter and Setter
    public int getIdBarang() {
        return idBarang;
    }

    public void setIdBarang(int idBarang) {
        this.idBarang = idBarang;
    }

    public String getNamaBarang() {
        return namaBarang;
    }

    public void setNamaBarang(String namaBarang) {
        this.namaBarang = namaBarang;
    }

    public String getKategoriBarang() {
        return kategoriBarang;
    }

    public void setKategoriBarang(String kategoriBarang) {
        this.kategoriBarang = kategoriBarang;
    }

    public int getStok() {
        return stok;
    }

    public void setStok(int stok) {
        this.stok = stok;
    }

    public int getStokMinimum() {
        return stokMinimum;
    }

    public void setStokMinimum(int stokMinimum) {
        this.stokMinimum = stokMinimum;
    }

    public double getHargaSatuan() {
        return hargaSatuan;
    }

    public void setHargaSatuan(double hargaSatuan) {
        this.hargaSatuan = hargaSatuan;
    }
}
