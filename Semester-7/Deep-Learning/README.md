# 🧠 Deep Learning (Semester 7)
> **Author**: Marchell Adi Pratama

---

## 📌 Domain Overview & Technical Specifications

This directory contains deep neural network architectures including Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Long Short-Term Memory (LSTM) time-series forecasting models implemented using `PyTorch`, `TensorFlow`, and `Keras`.

### 📂 Pipeline Architecture

```text
Semester-7/Deep-Learning/
├── data/
│   ├── dataset_lengkap_lstm.csv                         # Multi-variate Time Series LSTM Dataset
│   ├── data_kurs_2020_2025.csv                          # Currency Exchange Rate Historical Data
│   ├── data_libur_indonesia.csv                         # National Holiday Calendar Features
│   └── POWER_Point_Daily.csv                            # Daily Power Output Metrics
└── notebooks/
    ├── MNIST_Convolutional_Neural_Network.ipynb         # 2D ConvNet Image Classifier (Conv2D + MaxPool2D)
    ├── Train_CNN.ipynb                                  # Custom CNN Model Training & Hyperparameter Tuning
    ├── Simple_RNN_Weather_Temperature_Forecasting.ipynb # Sequence-to-Sequence Temperature RNN
    ├── LSTM_Model_Evaluation.ipynb                     # Multi-layer LSTM Financial Time-Series Model
    └── Scratch_vs_Transfer_Learning.ipynb               # Benchmark: Custom CNN vs MobileNetV2 / ResNet50
```

---

## 📊 Deep Learning Models & Datasets

| Model / Notebook | Architecture Type | Input Features / Dataset | Accuracy / Loss Metric |
| :--- | :--- | :--- | :--- |
| `MNIST_Convolutional_Neural_Network.ipynb` | 2D CNN (Conv2D + ReLU + MaxPool) | 28x28 Grayscale MNIST | Test Accuracy > 98.5% |
| `Simple_RNN_Weather_Temperature_Forecasting.ipynb` | Recurrent Neural Network | Historical 100-day Temperature | Mean Squared Error (MSE) |
| `LSTM_Model_Evaluation.ipynb` | Stacked LSTM Network | `data_kurs_2020_2025.csv` | Mean Absolute Percentage Error (MAPE) |
| `Scratch_vs_Transfer_Learning.ipynb` | MobileNetV2 vs Custom CNN | RGB Image Dataset | Fine-tuning Training Curves |

---

## 🛠️ Execution Quickstart

```bash
jupyter notebook Semester-7/Deep-Learning/notebooks/
```
