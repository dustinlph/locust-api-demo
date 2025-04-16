# locust-api-demo

### 1. Setup environment
```commandline
pipenv install
pipenv shell
```

### 2. launch Flask API
```commandline
cd flask_app
python app.py
```

### 3. execute Locust test
```commandline
cd locust_project
pipenv run locust -f locustfile.py --host=http://localhost:5000
```
UI: http://localhost:8089