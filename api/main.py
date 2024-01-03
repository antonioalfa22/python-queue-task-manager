import requests
import base64

from datetime import datetime
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/start_task', methods=['GET'])
def start_task():
    # Aquí irá la lógica para comunicarse con Airflow
    return "Tarea iniciada", 200


@app.route('/trigger_dag', methods=['GET'])
def trigger_dag():
    airflow_url = "http://airflow_webserver:8080/api/v1/dags/hello_world_dag/dagRuns"
    json_data = {
        "conf": {},
        "dag_run_id": "api__" + datetime.now().strftime("%Y%m%dT%H%M%S"),
        "note": "API triggered",
    }
    credentials = base64.b64encode(b'admin:admin').decode('utf-8')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {credentials}"
    }

    response = requests.post(airflow_url, json=json_data, headers=headers)
    if response.status_code == 200:
        return response.json(), 200
    else:
        return response.json(), response.status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)