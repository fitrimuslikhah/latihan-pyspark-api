# Latihan PySpark ETL API & Docker

Project sederhana membangun *ETL (Extract, Trasform, Load)* pipeline menggunakan **Pyspark**, **PostgreSQL**, dan **Docker Compose**

## Tech Stack
- **Python / Pyspark** (Data processing & Transformation)
- **PosgreSQL 15** (Data warehouse/Target DB)
- **Docker & Docker Compose** (Container)
- **JSONPlaceholder API** (Data Source)
- **BI Tools** (Looker Studio & Google Sheets)

## Architecture Pipeline
- **Extraction** (Mengambil data dari JSONPlaceholder API)
- **Transformation** (Membersihkan data menggunakan Apache PySpark)
- **Load** (Memasukkan data yang telah diproses ke dalam **PostgreSQL** sebagai datawarehouse) 
- **Visualization** (Menghubungkan PostgreSQL ke Looker Studio untuk analisis visual)

## Dashboard Preview
https://datastudio.google.com/s/uI7r8mIMKJU

## Cara Menjalankan Project
```bash
git clone https://github.com/fitrimuslikhah/latihan-pyspark-api.git
cd latihan-pyspark-api
