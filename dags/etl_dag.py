from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 8, 17),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG (
    dag_id='pyspark_etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL pyspark mengambil data API dan simpan ke PostgreSQL',
    schedule=None,
    catchup=False,
) as dag:

    # Task menjalankan script main.py di dalam container
    run_pyspark_etl=DockerOperator (
        task_id='run_pyspark_script',
        image='latihan-pyspark-api-pyspark-app',
        api_version='auto',
        auto_remove=True,
        command='python main.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        mount_tmp_dir=False
    )

    run_pyspark_etl