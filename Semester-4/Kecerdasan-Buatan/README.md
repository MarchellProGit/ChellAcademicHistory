# 🤖 Semester 4 — Kecerdasan Buatan (Artificial Intelligence)

**Course**: Kecerdasan Buatan (Artificial Intelligence)  
**Primary Tech Stack**: Python (`EasyOCR`, `OpenCV`, `NumPy`, `Pandas`, `Matplotlib`, `Jupyter Notebook`), Genetic Algorithms (`GA`), ID3 Decision Trees, SQL Schemas  
**Author**: Marchell Adi Pratama (`672023081`)  

---

## 📁 Pure Source Code & AI Models Index

### 🔹 `01-Python-Fundamentals/`
* `01_Python_AI_Fundamentals.ipynb`: Introduction to Python syntax, scientific computing, matrix manipulation, and data analysis for AI.

### 🔹 `02-Genetic-Algorithm-TSP/` (Evolutionary Optimization & TSP)
* `Genetic_Algorithm_TSP_Solver.ipynb`: Implementation of Genetic Algorithms (GA) for solving the Travelling Salesperson Problem (TSP) with selection, crossover, and mutation operators.
* `Geographic_Distance_TSP_Model.ipynb`: Distance matrix computation and route optimization model across global city coordinates.
* `cities50.csv`: 50-city coordinate dataset for TSP solver.
* `tsp.csv`: Distance matrix dataset for TSP solver.

### 🔹 `03-Decision-Trees-and-Fuzzy-Logic/`
* `ID3_Decision_Tree_Diagram.drawio`: Source diagram code for ID3 Information Gain classification tree.
* `Decision_Tree_Architecture.drawio`: Source diagram code for Decision tree hierarchy layout.

### 🔹 `04-Database-Schemas/`
* `Jobseeker_Database_Schema.sql`: Relational SQL database schema for job applicant AI matching model.
* `Registration_Database_Schema.sql`: User registration data pipeline SQL schema.

### 🔹 `05-Computer-Vision-OCR/`
* `Easy_OCR_Text_Recognition.py`: Optical Character Recognition (OCR) script using `EasyOCR` and OpenCV (`cv2`) supporting bilingual text extraction (English & Indonesian).

---

## ⚡ How to Run Code & Notebooks

### 1. Running Optical Character Recognition (OCR):
```bash
pip install easyocr opencv-python
python 05-Computer-Vision-OCR/Easy_OCR_Text_Recognition.py
```

### 2. Running Jupyter Notebooks:
```bash
pip install jupyter pandas numpy matplotlib
jupyter notebook 02-Genetic-Algorithm-TSP/Genetic_Algorithm_TSP_Solver.ipynb
```
