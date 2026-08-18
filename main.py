import requests
import json
import sys
import os 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

#===================================
# Tahap 1
#===================================

#URL API berisi dummy data
url = "https://jsonplaceholder.typicode.com/users"

#Mengambil data
print("mengambil api untuk mengambil data")

#Menembak API pakai library requests
response = requests.get(url)

if response.status_code == 200:
    data_api = response.json()
    print("Berhasil mengambil data dari API")
else:
    print("Gagal mengambil data dari API")
    sys.exit()

#Ubah respons teks dari API menjadi format JSON
data_api = response.json()
print("Berhasil mengambil data dari API")

print("---Contoh data JSON pertama dari API---")
print(json.dumps(data_api[0], indent=2))

#====================================
# Push Data JSON ke Pyspark
#====================================

print ("Memulai SparkSession")

#Inisialisai SparkSession
spark = SparkSession.builder \
    .appName("latihan_Pyspark_to_PostgreSQL") \
    .config("spark.jars", "/app/postgresql-42.6.0.jar") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

#Membaca schema secara otomatis menggunakan RDD JSON
json_rdd = spark.sparkContext.parallelize([json.dumps(item) for item in data_api])
df = spark.read.json(json_rdd)

#Menampilkan struktur table 
print("skema table otomatis")
df.printSchema()

#Menampilkan 5 baris Dataframe
print("data pertama di Pyspark")
df.show(5)

#Ambil kolom id, name, username, dan email
df_clean = df.select(
    "id", 
    "name", 
    "username", 
    "email", 
        df["address.city"].alias ("city")
)

print("Hasil transformasi")
df_clean.show(5)

# Simpan data ke database PostgreSQL
print("Mengirim data ke database PostgreSQL")

db_url = "jdbc:postgresql://host.docker.internal:5432/datawarehouse"
db_properties = {
    "user": "spark_user",
    "password": "spark_password",
    "driver": "org.postgresql.Driver"
}

df_clean.write \
    .jdbc(url=db_url, table="users_clean", mode="overwrite", properties=db_properties)

print("Data berhasil diunggah ke PostgreSQL")

print("Mematikan SparkSession")
spark.stop()

sys.exit(0)




