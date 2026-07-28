package warung;

import barang.Barang;
import java.util.ArrayList;

public class Warungroti implements Warunginterface {

    private ArrayList<Barang> menu;
    private int omset;

    public Warungroti() {
        menu = new ArrayList<>();
        menu.add(new Barang("Sari Roti", 40, 3500));
        menu.add(new Barang("Roti Tawar", 80, 1500));
        menu.add(new Barang("Croissant", 50, 8000));
    }

    @Override
    public boolean tambahStok(Barang barang, int jumlah) {
        for (Barang b : menu) {
            if (b.getNama().equals(barang.getNama())) {
                b.setStok(b.getStok() + jumlah);
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean jualBarang(Barang barang, int jumlah) {
        for (Barang b : menu) {
            if (b.getNama().equals(barang.getNama())) {
                if (b.getStok() >= jumlah) {
                    b.setStok(b.getStok() - jumlah);
                    omset += b.getHarga() * jumlah;
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public ArrayList<Barang> tampilkanMenu() {
        return menu;
    }

    public int getOmset() {
        return omset;
    }
}
