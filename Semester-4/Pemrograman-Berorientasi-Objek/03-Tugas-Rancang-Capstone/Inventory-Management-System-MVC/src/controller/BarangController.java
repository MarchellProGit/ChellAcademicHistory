package controller;

import model.Barang;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.table.DefaultTableModel;

public class BarangController {
    public Statement stm;
    public ResultSet res;
    public String sql;
    
    //Untuk mendesain table dengan kolom2 tertentu
    DefaultTableModel dtm = new DefaultTableModel();
    
    //Kontruktor
    public BarangController(){
        Koneksi kn = new Koneksi();
        kn.config();
        this.stm = kn.stm;
    }
    
    public DefaultTableModel Tabel(){
        dtm.addColumn("ID");
        dtm.addColumn("NAMA BARANG");
        dtm.addColumn("KATEGORI");
        dtm.addColumn("STOK");
        dtm.addColumn("STOK MINIMUM");
        dtm.addColumn("HARGA");
        return dtm;
    }
    
    //SELECT
    public void tampilkanData(){
        try {
            //persiapan table - dgn cara clear area dtm
            dtm.getDataVector().removeAllElements();
            dtm.fireTableDataChanged();
            
            //Query
            this.sql = "SELECT * FROM tb_barang";
            
            //jalankan Query
            res = stm.executeQuery(sql);
            
            //unboxing data ke dalam array/Objek
            //Objek adalah struktur
            while(res.next()){
                Object[] obj = new Object[6];
                //namanya harus sama dengan yang di db
                obj[0] = res.getString("id_barang");
                obj[1] = res.getString("nama_barang");
                obj[2] = res.getString("kategori_barang");
                obj[3] = res.getString("stok");
                obj[4] = res.getString("stok_minimum");
                obj[5] = res.getString("harga_satuan");
                
                //masukkan objek ke dtm
                dtm.addRow(obj);
            }
        } catch (Exception e) {
            System.out.println("Gagal Query" +e);
        }
    }
    
    //INSERT
    public boolean tambahData(String a, String b, int c, int d, double e){
        //Hubungkan dengan model
        Barang br = new Barang();
        br.setNamaBarang(a);
        br.setKategoriBarang(b);
        br.setStok(c);
        br.setStokMinimum(d);
        br.setHargaSatuan(e);
        
        try {
            this.sql="INSERT INTO tb_barang (nama_barang, kategori_barang, stok, stok_minimum, harga_satuan) VALUES('"+br.getNamaBarang()+"',"
                    + "'"+br.getKategoriBarang()+"',"
                    + ""+br.getStok()+","
                    + ""+br.getStokMinimum()+","
                    + ""+br.getHargaSatuan()+")";
            
            this.stm.executeUpdate(sql);
            return true;
        } catch (Exception e1) {
            return false;
        }
    }
    
    //UPDATE
    public boolean ubahData(int z, String a, String b, int c, int d, double e){
        //Hubungkan dengan model
        Barang br = new Barang();
        br.setIdBarang(z);
        br.setNamaBarang(a);
        br.setKategoriBarang(b);
        br.setStok(c);
        br.setStokMinimum(d);
        br.setHargaSatuan(e);
        
        try {
            this.sql="UPDATE tb_barang SET "
                    + "nama_barang ='"+br.getNamaBarang()+"',"
                    + "kategori_barang ='"+br.getKategoriBarang()+"',"
                    + "stok ="+br.getStok()+","
                    + "stok_minimum ="+br.getStokMinimum()+","
                    + "harga_satuan ="+br.getHargaSatuan()+""
                    + "WHERE id_barang ="+br.getIdBarang()+"";;
            
            this.stm.executeUpdate(sql);
            return true;
        } catch (Exception e1) {
            return false;
        }
    }
    
    //DELETE
    public boolean hapusData(int a){
        Barang br = new Barang();
        br.setIdBarang(a);
        try {
            this.sql="DELETE FROM tb_barang WHERE id_barang="+br.getIdBarang()+"";
            this.stm.executeUpdate(sql);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
