# flask_mongodb

### Overview
This repository contains a Python application with a Flask-based REST API and a MongoDB NoSQL database. It demonstrates how to create, update, and read key-value pairs in the database using HTTP methods.

### Project structure

* `docker-compose.yml`: Docker Compose configuration for the application and database
* `Makefile`: Contains commands for building, starting, and stopping the API
* `Dockerfile`: Defines the Docker image for the Python application
* `src/app.py`: The main Python application implementing the Flask-based REST API
* `src/requirements`: List of Python dependencies
* `src/static/swagger.yaml`: Swagger API documentation YAML file

### Getting started
##### 1. Clone the Repository

##### 2. Build and Start the Application

```bash
make rebuild
```

##### 3. Access the Swagger Documentation

You can access the Swagger documentation at:
`[http](http://localhost:8080/docs/)http://localhost:8080/docs/`

<img width="1420" alt="image" src="https://github.com/MironovaSveta/flask_mongodb/assets/104065509/ce092ec2-030e-49e5-97e5-78abfd6fd3f3">

##### 4. Use the REST API

You can interact with the REST API endpoints using the tools like 'Postman', or 'curl', or any other REST client. Below are available endpoints.

**Note** Make sure your application is running before making requests.

##### 4.1. Add a Key-Value Pair:

* HTTP method: 'POST'.
* Request URL: `http://localhost:8080/add`
* Request body: (`raw`, content type: `JSON`)

Example of the input JSON data:
```json
{
    "key": "my_key",
    "value": "my_value"
}
```

Example of the output data:
```
[
    {
        "message": "Key-value pair added successfully"
    },
    201
]
```

##### 4.2. Update a Value for a Key:

* HTTP method: 'PUT'
* Request URL: `http://localhost:8080/update`
* Request body: (`raw`, content type: `JSON`)

Example of the input JSON data:
```json
{
    "key": "my_key",
    "new_value": "my_new_value"
}
```

Example of the output data:
```
[
    {
        "message": "Value for key my_key updated successfully"
    },
    200
]
```

##### 4.3. Add a Key-Value Pair:

* HTTP method: 'GET'
* Requested URL: `http://localhost:8080/read/my_key` (replace `my_key` with the key you want to read)

Example of the output data:
```
{
    "_id": {
        "$oid": "653bbbdbf5d5f270b09afdf5"
    },
    "key": "my_key",
    "value": "my_new_value"
}
```

