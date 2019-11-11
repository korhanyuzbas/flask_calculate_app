# Calculation floating-point numbers

A basic Flask application for multiplying giving 2 numbers, process calculation on Celery and returns result on endpoint

### Requirements

```bash
Docker CE
```

### Clone Repository

```bash
git clone https://github.com/korhanyuzbas/flask_calculate_app.git
```

### Build & Launch

```bash
docker-compose up -d --build
```

This will expose app endpoints on port `5001` 

To shut down project:

```bash
docker-compose down
```

### How to use app
Endpoint ``` POST /calculate```

Payload
```
{
    "first_number": <float>,
    "second_number": <float>
} 
```

Response (success)

```
<task_id>
```

After receiving <task_id>, you can check results of calculation with following endpoint:

Endpoint ``` GET /callback/<task_id> ```

Response (success, example)
```
3.14 
```

### Test
Run following command on docker container

``` 
python -m unittest test.py
```
