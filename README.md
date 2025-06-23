## QUOTES API
This is an API project called QUOTES API built with Flask.


## How to run the Project
- Install Python
- Git clone the project with ```https://github.com/Aderinmola/quote_api.git```
- change directory with ``` cd assessment ``` 
- Create your virtualenv with `py -m venv venv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Finally run the API, in another terminal
``` python .\quotes\app.py ```
- Go ahead to test the endpoints listed in the table below with postman, using the base url ``` http://127.0.0.1:5000```


## ROUTES TO IMPLEMENTED
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
_Quote_|
| *GET* | ```/quotes``` | _List all quotes_|_All quotes_|
| *POST* | ```/quotes``` | _Create a quotes_|_Create quotes_|

### 📬 Postman Collection

You can import the included Postman collection to test the API:

- File: [`Flask API postman collection.json`](./quotes_api.postman_collection.json)

Instructions:
1. Open Postman
2. Click "Import" > "Upload Files"
3. Select the file above
4. Start sending requests to `http://localhost:5000/quotes`



