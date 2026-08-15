#Base image Python
FROM python:3.10-slim

#Install OpenJDK
RUN apt-get update && apt-get install -y \
default-jre-headless \
curl \
&& rm -rf /var/lib/apt/lists/*

#Set direktori kerja di dalam kontainer
WORKDIR /app

#Download JDBC Driver PostgreSQL menggunakan curl
RUN curl -o /app/postgresql-42.6.0.jar https://jdbc.postgresql.org/download/postgresql-42.6.0.jar

#Copy requirements.txt lalu install library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy skrip main.py
COPY main.py . 

#Jalankan main.py saat kontainer menyala
CMD ["python", "main.py"]