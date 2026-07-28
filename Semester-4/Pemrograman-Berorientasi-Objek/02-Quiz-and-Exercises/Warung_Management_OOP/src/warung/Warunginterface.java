package warung;

import barang.Barang;
import java.util.ArrayList;

public interface Warunginterface {

    boolean tambahStok(Barang barang, int jumlah);

    boolean jualBarang(Barang barang, int jumlah);

    ArrayList<Barang> tampilkanMenu();
}
