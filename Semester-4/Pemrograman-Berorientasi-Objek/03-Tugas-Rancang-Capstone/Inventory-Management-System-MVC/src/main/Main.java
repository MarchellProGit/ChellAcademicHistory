import view.MainView;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // Set Look and Feel agar aplikasi tampil lebih modern (opsional)
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            System.err.println("Tidak dapat mengatur Look and Feel: " + e.getMessage());
        }

        // Menjalankan tampilan utama aplikasi
        SwingUtilities.invokeLater(() -> {
            MainView mainView = new MainView();
            mainView.setVisible(true);
        });
    }
}
