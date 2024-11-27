# Agro Tech

A system that consists of manager farm producer informations.

# Tech Stack
* Python 3.11
* Postgres

# First Step
* Creates a .env file and uses the .env_example file as a model.

* If you have docker, run the code below and go to the section  [How to use the API](#-How-to-use-the-API).:
```
docker compose up -d
```

* Creates a virtual environment for the project:
```
python -m venv venv 
```

* Install all packages with poetry:

```
pip install -r requirements.txt

```

* Run script to create the tables
```
python create_tables.py
```

# Run the Application
```
python main.py
```

# How to use the API
## Swagger API
* You can access the Swagger API  
```
http://localhost:8000/docs
```

## Producer Routes
### Producer Model
```
{
    "cpf_cnpj": "12345678910",
    "document_type": "CPF",
    "producer_name": "John",
    "farm_name": "John's Farm",
    "city": "city 1",
    "state": "state 1",
    "farm_area": 1000,
    "arable_area": 500,
    "vegetation_area": 200,
    "cultivation": "Soja",
}
```
### Create a product
* Sends the product you want to create in the body of your request. Use the Product Model for this.
```
http:localhost:8000/producers
```
### Find All Producer
```
http:localhost:8000/producers
```
### Find Total Producers
```
http:localhost:8000/producers/total
```
### Update one producer
```
http:localhost:8000/producers/producer_id
```
### Delete one producer
```
http:localhost:8000/producers/producer_id
````

## Tests
* Run the command to execute unit and integration tests.
```
pytest test
```

