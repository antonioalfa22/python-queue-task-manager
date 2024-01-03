# Python Queue Task Manager


## Description
The Python Queue Task Manager is an asynchronous task management system that leverages a queue-based approach to efficiently handle tasks. This system is built using Python and integrates with Apache Airflow, providing a robust and scalable solution for managing complex workflows and task dependencies.

## Features
- **Asynchronous Task Management**: Efficiently manage and process tasks asynchronously.
- **Queue-Based System**: Leverage a queue system to organize and prioritize tasks.
- **Integration with Apache Airflow**: Utilize the powerful features of Apache Airflow for workflow management.
- **Scalable and Flexible**: Designed to scale and adapt to various task management needs.
- **RESTful API with Flask**: Easy to use RESTful API developed with Flask for interacting with the task manager.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation
1. **Clone the Repository**

```
git clone https://github.com/antonioalfa22/python-queue-task-manager
cd python-queue-task-manager
```

2. **Build and Run the Containers**

```
docker-compose up --build
```


### Usage
- The Flask API is accessible at `http://localhost:5000`.
- The Airflow webserver can be accessed at `http://localhost:8080`. Default login credentials are admin/admin.
- Flower (Celery monitoring tool) is available at `http://localhost:5555`.

### API Endpoints
Describe the available API endpoints and how to interact with them.

## Configuration
Explain any configuration steps, including environment variables and external dependencies.

## Contributing
Provide guidelines for how others can contribute to your project. Include instructions for setting up a development environment and submitting pull requests.

## License
State the license under which your project is available. (e.g., MIT, GPL-3.0)
