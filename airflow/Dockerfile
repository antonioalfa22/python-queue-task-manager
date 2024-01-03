FROM apache/airflow:latest

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/
COPY airflow.cfg /opt/airflow/airflow.cfg