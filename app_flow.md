## Appication workflow
A user can browse the list of available questions like:

```http
GET /friendship/question/ HTTP/1.1
Host: client.com
Accept: application/json
```
This will yield the response:

```http
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": 1,
    "answers": [
      {
          "id": 1,
          "text": "John Doe"
      },
      {
          "id": 2,
          "text": "John Poe"
      }
    ],
    "created_at": "2019-04-04T09:51:50.744638Z",
    "updated_at": "2019-04-04T09:51:50.744699Z",
    "text": "What is your name?"
  }
]
```

Once they have answered some questions they can login with facebook and submit their details to the server
**Note:** Facebook login is not yet implemented in this application.

```http
POST /friendship/quiz_details/ HTTP/1.1
Host: client.com
Accept: application/json
```
With payload:
```json
{
  "user": {"username": "johndoe2"},
  "quiz": {"title": "Where is my mind?"},
  "quiz_result": [
    {
      "question": 1,
      "answer": 1
    }
  ]
}
```

The user can submit their fb details inside `user` object. `quiz` object contains
details about quiz. User can provide name that can catch people's attention. The response
will be like:

```http
HTTP/1.1 201 CREATED
Content-Type: application/json
{
  "id": 5,
  "message": "Thanks for taking this quiz. Share this quiz with your friends and see how they answer",
  "invitation_link": "/friendship/quiz_details/5/",
  "quiz": {
      "id": 5,
      "total_questions": 1,
      "created_at": "2019-04-04T11:21:33.660205Z",
      "updated_at": "2019-04-04T11:21:33.660395Z",
      "title": "Where is my mind?"
  },
  "user": {
      "id": 1,
      "username": "johndoe2"
  },
  "invited_by": null,
  "created_at": "2019-04-04T11:21:33.673670Z",
  "updated_at": "2019-04-04T11:21:33.673711Z"
}
```

The invitation link can be use to share the quiz on facebook. Once any of user's friend click
on the link he will be presented to the same quiz as original user.

```http
GET /friendship/quiz_details/1/ HTTP/1.1
Host: client.com
Accept: application/json
```
The server will provide response of the following format

```http
HTTP/1.1 200 OK
Content-Type: application/json
{
  "id": 5,
  "quiz": {
      "id": 5,
      "total_questions": 1,
      "created_at": "2019-04-04T11:21:33.660205Z",
      "updated_at": "2019-04-04T11:21:33.660395Z",
      "title": "Where is my mind?"
  },
  "user": {
      "id": 1,
      "username": "johndoe2"
  },
  "created_at": "2019-04-04T11:21:33.673670Z",
  "updated_at": "2019-04-04T11:21:33.673711Z"
}
```

Now the user can access the questions like:
```http
GET /friendship/quiz/5/questions HTTP/1.1
Host: client.com
Accept: application/json
```

This will return user with the same quiz which their friend attempted:

```http
HTTP/1.1 200 OK
Content-Type: application/json
[
  {
    "id": 1,
    "answers": [
      {
          "id": 1,
          "text": "John Doe"
      },
      {
          "id": 2,
          "text": "John Poe"
      }
    ],
    "created_at": "2019-04-04T09:51:50.744638Z",
    "updated_at": "2019-04-04T09:51:50.744699Z",
    "text": "What is your name?"
  }
]
```

Once the user has done the quiz he can submit it

```http
POST /friendship/quiz_details/ HTTP/1.1
Host: client.com
Accept: application/json
```
With payload:
```json
{
  "user": {"username": "johndoe"},
  "quiz": {"title": "Where is my mind?"},
  "invited_by": 1
  "quiz_result": [
    {
      "question": 1,
      "answer": 1
    }
  ]
}
```

This will return response:
```http
HTTP/1.1 201 CREATED
Content-Type: application/json
{
  "id": 7,
  "message": "You know your friend johndoe2 very well. You answered 100% questions like him",
  "invitation_link": "/friendship/quiz_details/7/",
  "quiz": {
      "id": 2,
      "total_questions": 1,
      "created_at": "2019-04-04T10:16:44.500479Z",
      "updated_at": "2019-04-04T10:16:44.500534Z",
      "title": "Where is my mind?"
  },
  "user": {
      "id": 1,
      "username": "johndoe"
  },
  "invited_by": 2,
  "created_at": "2019-04-04T11:40:17.193707Z",
  "updated_at": "2019-04-04T11:40:17.193743Z"
}
```
The message now tells the user how many question he was able to answer that matches his friends responses.
