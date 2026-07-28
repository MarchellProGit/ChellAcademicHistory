package warung;

import barang.Barang;
import java.util.ArrayList;

public class Warungmakan implements Warunginterface {

    private ArrayList<Barang> menu;
    private int omset;
    private int gas;

    public Warungmakan() {
        menu = new ArrayList<>();
        menu.add(new Barang("Indomie Goreng", 100, 6000));
        menu.add(new Barang("Indomie Rebus", 200, 7000));
        menu.add(new Barang("Indomie Telur", 50, 10000));
        menu.add(new Barang("Indomie Kornet", 30, 12000));
        gas = 15;
    }

    @Override
    public boolean tambahStok(Barang barang, int jumlah) {
        for (Barang b : menu) {
            if (b.getNama().equals(b.getNama())) {
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
                    gas -= jumlah;
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

    public int getGas() {
        return gas;
    }

    public void isiUlangGas() {
        gas = 15;
        omset -= 22000;
    }
}
