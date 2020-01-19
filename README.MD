## Auth App

Simple REST API app for handling users auth and registration. 

After registration user get access to db with information about other users. Also
user can modify information about himself and delete his account. 

## Installing

To start service just use:

```
docker-compose up
```

## API Documentation


**Note:** Sample requests are send with [Httpie]

- POST `/api/users/<int:id>`  
	Create new user in db  
    Request example:  
    ```
	$ http POST http://localhost:5000/api/users username=john2 password=123 email=john@mail.com```
- GET `/api/users`  
	Get list of all users in db  
	Request example:  
	```
    http --auth john2:123 GET http://localhost:5000/api/users
    ```
- GET `/api/users/<int:id>`  
	Get specified user information  
	Request example:  
    ```
    http --auth john2:123 GET http://localhost:5000/api/users/1
    ```
- PUT `/api/users/<int:id>`  
	Get specified user information  
	Request example: 
    ```
    http --auth john2:123 PUT http://localhost:5000/api/users/1 username=john3
    ```
- DELETE `/api/users/<int:id>`  
	Get specified user information  
	Request example:  
	```
    http --auth john2:123 DELETE http://localhost:5000/api/users/1
    ```