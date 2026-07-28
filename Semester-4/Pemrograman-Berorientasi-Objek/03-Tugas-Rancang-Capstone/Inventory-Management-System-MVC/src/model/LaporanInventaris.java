package model;

import java.sql.Timestamp;

public class LaporanInventaris {
    private int idLaporan;
    private int idBarang;
    private int stokSaatIni;
    private Timestamp tanggalLaporan;

    // Constructor
    public LaporanInventaris(int idLaporan, int idBarang, int stokSaatIni, Timestamp tanggalLaporan) {
        this.idLaporan = idLaporan;
        this.idBarang = idBarang;
        this.stokSaatIni = stokSaatIni;
        this.tanggalLaporan = tanggalLaporan;
    }

    // Getter and Setter
    public int getIdLaporan() {
        return idLaporan;
    }

    public void setIdLaporan(int idLaporan) {
        this.idLaporan = idLaporan;
    }

    public int getIdBarang() {
        return idBarang;
    }

    public void setIdBarang(int idBarang) {
        this.idBarang = idBarang;
    }

    public int getStokSaatIni() {
        return stokSaatIni;
    }

    public void setStokSaatIni(int stokSaatIni) {
        this.stokSaatIni = stokSaatIni;
    }

    public Timestamp getTanggalLaporan() {
        return tanggalLaporan;
    }

    public void setTanggalLaporan(Timestamp tanggalLaporan) {
        this.tanggalLaporan = tanggalLaporan;
    }
}
