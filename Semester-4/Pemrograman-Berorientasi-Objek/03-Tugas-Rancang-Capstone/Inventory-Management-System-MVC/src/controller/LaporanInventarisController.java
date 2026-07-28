package controller;

import model.LaporanInventaris;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.swing.table.DefaultTableModel;


public class LaporanInventarisController {
    public Statement stm;
    public ResultSet res;
    public String sql;
    
    DefaultTableModel dtm = new DefaultTableModel();

    public LaporanInventarisController() {
        Koneksi Kn = new Koneksi();
        Kn.config();
        this.stm=Kn.stm;
    }
    
    public DefaultTableModel buatTabel(){
        dtm.addColumn("ID Laporan");
        dtm.addColumn("ID Barang");
        dtm.addColumn("Stok Saat Ini");
        dtm.addColumn("Tanggal Laporan");
        return dtm;
    }
    
    public void tampilkanData(){
        try {
            dtm.getDataVector().removeAllElements();
            dtm.fireTableDataChanged();

            this.sql="SELECT * FROM tb_laporan_inventaris";

            res = stm.executeQuery(sql);
            
            while (res.next()){
                Object[] obj = new Object[4];
                obj[0] = res.getString("id_laporan");
                obj[1] = res.getString("id_barang");
                obj[2] = res.getString("stok_saat_ini");
                obj[3] = res.getString("tanggal_laporan");
                
                dtm.addRow(obj);
            }
        } catch (Exception e) {
            System.out.println("Gagal Query"+e);
        }
    }
}
