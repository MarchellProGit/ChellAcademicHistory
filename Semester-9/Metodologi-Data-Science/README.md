# Metodologi Data Science (Semester 9)
> **Author**: Marchell Adi Pratama

---

## Domain Overview & Technical Specifications

An end-to-end CRISP-DM (Cross-Industry Standard Process for Data Science) predictive system featuring an XGBoost classifier, Streamlit web interactive dashboard, and FastAPI backend service.

### Pipeline Architecture

```text
Semester-9/Metodologi-Data-Science/
 anak-data-nih-bosh/
 app.py # Streamlit Interactive Web Application
 Air_Quality_Weather_Project.py # XGBoost Model Training & CRISP-DM Evaluation
 requirements.txt # Python Dependency Specification
 data/raw/
 worldwide_weather_2025.csv # Global Weather Dataset
 global_air_quality_dataset.csv # AQI Features Dataset
 results/
 xgb_weather_model.pkl # Serialized XGBoost Model
 weather_scaler.pkl # StandardScaler Pipeline Artifact
```

---

## Execution Quickstart

```bash
cd Semester-9/Metodologi-Data-Science/anak-data-nih-bosh
pip install -r requirements.txt
streamlit run app.py
```
