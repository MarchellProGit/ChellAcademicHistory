# 📝 Pemrosesan Bahasa Alami / NLP (Semester 9)
> **Author**: Marchell Adi Pratama

---

## 📌 Domain Overview & Technical Specifications

This directory contains Natural Language Processing (NLP) text processing pipelines, Indonesian Sastrawi stemming routines, TF-IDF feature matrices, and visual text mining workflows in Orange3.

### 📂 Pipeline Architecture

```text
Semester-9/Pemrosesan-Bahasa-Alami/
├── data/
│   ├── corpus.csv                                       # Text Analysis Corpus Dataset
│   ├── jampidsus.csv                                    # Legal & News Text Corpus
│   └── run_results.csv                                  # Model Output Predictions
├── workflows/
│   ├── Orange_Text_Mining_Workflow_1.ows                # Visual Workflow: Corpus Tokenization & Word Cloud
│   └── Orange_Text_Mining_Workflow_2.ows                # Visual Workflow: Topic Modeling (LDA)
└── notebooks/
    ├── NLP_Twitter_Scraping_Sastrawi_Preprocessing.ipynb # Apify Twitter Scraper & Sastrawi Stemming
    └── BBC_News_NLP_Text_Classification.ipynb           # TF-IDF Feature Matrix & Naive Bayes Classifier
```

---

## 🛠️ Execution Quickstart

```bash
jupyter notebook Semester-9/Pemrosesan-Bahasa-Alami/notebooks/
```
