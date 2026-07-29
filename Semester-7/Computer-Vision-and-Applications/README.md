# 👁️ Computer Vision & Applications / CVA (Semester 7)
> **Author**: Marchell Adi Pratama

---

## 📌 Domain Overview & Technical Specifications

This module houses real-time computer vision pipelines, image processing routines, frequency domain filtering, and object detection systems targeting Indonesian Sign Language (BISINDO) utilizing `OpenCV`, `YOLOv8/v11`, and `PyTorch`.

### 📂 Pipeline Architecture

```text
Semester-7/Computer-Vision-and-Applications/
├── models/
│   ├── yolo11s.pt                                       # Pre-trained YOLOv11 Small Weights
│   └── yolov8_bisindo_results/
│       └── detect/bisindo_yolov8_model/weights/
│           ├── best.pt                                  # Top Performing BISINDO Gesture Weights
│           └── last.pt                                  # Final Epoch Checkpoint
└── notebooks/
    ├── Sign_Language_YOLO_Computer_Vision_Pipeline.ipynb# Real-time BISINDO Detection Pipeline
    ├── Training_Yolo_640.ipynb                          # YOLO Training Routine (640x640 Resolution)
    ├── FFT.ipynb                                        # Fast Fourier Transform Frequency Filtering
    ├── OpenCV_Image_Processing_Augmentation.ipynb       # Spatial Morphologies & Contrast Enhancement
    ├── Image_Dataset_Extraction_Pipeline.ipynb          # Automated Dataset Normalization
    └── Kaggle_YOLO_Dataset_Downloader.ipynb             # Bounding Box Annotator & Downloader
```

---

## 📊 Model Performance & Computer Vision Modules

| Module / Weight | Algorithm / Model | Task / Purpose | Performance Metrics |
| :--- | :--- | :--- | :--- |
| `best.pt` | YOLOv8 Custom Head | BISINDO Hand Gesture Detection | mAP50 = 0.942, Precision = 0.96 |
| `FFT.ipynb` | 2D Fourier Transform | High-Pass & Low-Pass Frequency Filtering | Frequency Spectrum Reconstruction |
| `OpenCV_Image_Processing_Augmentation.ipynb` | Morphological Operations | Erosion, Dilation, Otsu Thresholding | Edge Mask Generation |

---

## 🛠️ Execution Quickstart

```bash
jupyter notebook Semester-7/Computer-Vision-and-Applications/notebooks/
```
