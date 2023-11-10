# note-app-flask

### [Postman Collection](https://orange-water-893372.postman.co/workspace/django-react~29b6f2f5-8e7b-4fa8-b63c-2ca7ec504ac7/collection/17185093-490b1d64-33d5-49e6-b477-0bfe8978ec5e?action=share&creator=17185093)

## User endpoints
#### Get Users - https://notes-app-ku2v.onrender.com/users

#### Create User - https://notes-app-ku2v.onrender.com/register
Example:
```
{
    "name": "John",
    "username": "john",
    "password": "1234"
}
```

#### Login User - https://notes-app-ku2v.onrender.com/login
##### This endpoint generates access_token
Example:
```
{
    "username": "john",
    "password": "1234"
}
```

## Note endpoints

#### Create Note - https://notes-app-ku2v.onrender.com/register
##### Authorization required - Authorization: Bearer <access_token>
Example:
```
{
    "title": "new note",
    "content": "This is a note"
}
```

#### Get Note - https://notes-app-ku2v.onrender.com/notes/<id>
##### Authorization required - Authorization: Bearer <access_token>
Example:
```
id = 654e5b4e032aeed7547d248d
```

#### Update Note - https://notes-app-ku2v.onrender.com/notes/<id>
##### Authorization required - Authorization: Bearer <access_token>
Example:
```
id = 654e5b4e032aeed7547d248d
```
```
{
    "title": "new note updated",
    "content": "This is a note"
}
```

#### Delete Note - https://notes-app-ku2v.onrender.com/<id>
##### Authorization required - Authorization: Bearer <access_token>
Example:
```
id = 654e5b4e032aeed7547d248d
```

## Installation guide
1. git clone: https://github.com/Ayan-Paul/note-app-flask
2. pip install -r requirements.txt
3. create .env file
4. In .env set DABASE_URL="<Your_MongoDB_URL>"
5. In terminal run: python app.py
