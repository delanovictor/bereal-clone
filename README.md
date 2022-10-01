# bereal-clone
Description

<br>
<br>
<br>



# Endpoints

## Users
| Name | Method | Description |
| --- | --- | --- |
|/users| GET | Get all users


### Response
```json
[
    {
        "id": 1,
        "name": "TesteName",
        "userName": "TesteUName",
        "phoneNumber": "99999999999",
        "profileImage": "nao tem",
        "latitude": 1.0,
        "longitude": 1.0,
        "followers": 0,
        "following": 0,
        "createdAt": "2022-08-27T00:00:00Z",
        "updatedAt": "2022-08-27T00:00:00Z"
    },
    ...
]
```
<br>

| Name | Method | Description |
| --- | --- | --- |
|/users/:id  | GET | Get user by id
### Response
```json
{
    "id": 1,
    "name": "TesteName",
    "userName": "TesteUName",
    "phoneNumber": "99999999999",
    "profileImage": "nao tem",
    "latitude": 1.0,
    "longitude": 1.0,
    "followers": 0,
    "following": 0,
    "createdAt": "2022-08-27T00:00:00Z",
    "updatedAt": "2022-08-27T00:00:00Z"
}
```
<br>

| Name | Method | Description |
| --- | --- | --- |
|/users | POST | Returns array of users
### Body
```json
{
    "name": "",
    "userName": "",
    "phoneNumber": "",
    "profileImage": "",
    "latitude": null,
    "longitude": null,
    "followers": null,
    "following": null
}
```
### Response
The created user
<br>
<br>

---

## Posts

<br>

| Name | Method | Description |
| --- | --- | --- |
|/posts | GET | Get all Posts

### Parameters
| Name | Type | Required / Optional | Description |
| --- | --- | --- | --- |
| user | number | optional | Filter posts by user |

### Response
```json
[
    {
        "id": 1,
        "user": 1,
        "image": "link da imagem",
        "likes": 0,
        "latitude": null,
        "longitude": null,
        "createdAt": "2022-08-27T00:00:00Z",
        "updatedAt": "2022-08-27T00:00:00Z"
    },
    ...
```
<br>

| Name | Method | Description |
| --- | --- | --- |
|/posts/:id | POST | Get post by id

### Body
```json
{
    "id": 1,
    "user": 1,
    "image": "link da imagem",
    "likes": 0,
    "latitude": null,
    "longitude": null,
    "createdAt": "2022-08-27T00:00:00Z",
    "updatedAt": "2022-08-27T00:00:00Z"
}
```
<br>

| Name | Method | Description |
| --- | --- | --- |
|/posts | POST | Create Post
### Body
```json
{
    "user": 1,
    "image": "xxxxxxx.jpg",
    "likes": null,
    "latitude": 123.0,
    "longitude": 321.0
}
```
### Response
```json
{
    "id": 45,
    "user": 1,
    "image": "xxxxxxx.jpg",
    "likes": 0,
    "latitude": 123.0,
    "longitude": 321.0,
    "createdAt": "2022-10-01T16:17:57.256350Z",
    "updatedAt": "2022-10-01T16:17:57.256350Z",
    "url": "https://berealclone-storage.s3.amazonaws.com/1/1664641077.jpg?AWSAccessKeyId=AKIATS3JQI56S64EG7IR&Signature=LfCzGWshtjp06EK1s95iOFhf3BM%3D&content-type=image%2Fjpg&Expires=1664641137"
}
```
<br>
<br>