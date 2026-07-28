# 🔌 Semester 4 — Dasar Pemrograman Jaringan (DPJ)

**Course**: Dasar Pemrograman Jaringan (Fundamentals of Network Programming)  
**Primary Tech Stack**: Python (`Sockets`, `HTTP`, `TCP/IP`), JSON, XML, YAML, HTML5 Client Interface  
**Author**: Marchell Adi Pratama (`672023081`)  

---

## 📁 Coursework & Network Engineering Index

### 🔹 `01-Network-Data-Serialization/`
Network payload serialization, data parsing, and multi-format data interchange drills:
* `JSON_Data_Format.json`: JSON payload parsing & structure.
* `XML_Data_Format.xml`: XML schema definition & tag parsing.
* `YAML_Data_Format.yaml`: YAML configuration parsing.
* `Network_Serialization_Task.json`: Multi-format network packet data serialization.

### 🔹 `02-Python-Network-Server-Engine/`
* `main.py`: Core TCP/IP socket server listener & request dispatcher engine.
* `app.py`: Application route handling & HTTP payload response controller.
* `config.py`: Socket server host/port configuration & network parameters.

### 🔹 `03-Web-Server-Client-Interface/`
* `index.html`: Client-side dashboard interface connected to Python socket server backend.

---

## ⚡ How to Run Network Server Engine

Start Python Socket/HTTP Network Server:

```bash
python 02-Python-Network-Server-Engine/main.py
```
Server listens on configured host/port (default: `http://localhost:8080`).
