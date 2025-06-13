# UpNyX_Assignment
# AI Chat System – Django REST API Project

This project is a Django-based REST API for an AI Chat System. It supports user registration, login, chatting with an AI (mocked response), and token management.

## 💻 Features

- ✅ User Registration
- ✅ User Login with Token Authentication
- ✅ AI Chat Endpoint (deducts tokens per question)
- ✅ Token Balance Check
- ✅ Fully Testable with Postman

---

## 🏁 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ChaituReddy17/UpNyX_Assignment
```

Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Required Dependencies
```bash
pip install django
pip install djangorestframework
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start the server
```bash
python manage.py runserver
```

### 5. API Endpoints (Test via Postman)
~Register Operation
* Click new in your workspace
* Select HTTP Request
* Set Method to POST
* enter your DEV URL http://127.0.0.1:8000/api/register/
* In body section enter this text

{
  "username": "Your_Username",
  "password": "Your_Password"
}
 
* Now click Send

    $$$You will see something like this
![image alt](https://github.com/ChaituReddy17/UpNyX_Assignment/blob/main/Images/Register.png?raw=true)


~Login Operation
* Change the URL to 
http://127.0.0.1:8000/api/login/
* Since you already Entered body text
* Click Send
* you will get a response like 
{
  "token": "your_token_here"
}
 copy the Token id you will need it
$$$You will see something like this
![image alt](https://github.com/ChaituReddy17/UpNyX_Assignment/blob/main/Images/Login.png?raw=true)


~Tokens
* Change the URL to 
http://127.0.0.1:8000/api/tokens/
* In Headers section add a new key named "Authorization".
* In Value place your token
* Click send and you see an response like
{
  "tokens" : 4000
}
The initial value will be 4000 tokens.
$$$You will see something like this
![image alt](https://github.com/ChaituReddy17/UpNyX_Assignment/blob/main/Images/InitialTokens.png?raw=true)

~Chat
* Change the URL to 
http://127.0.0.1:8000/api/chat/
* Keep the Headers Section Key intact there
* Now in Body Section Enter
{
  "message": "Your_Message_Here"
}
$$$You will see something like this
![image alt](https://github.com/ChaituReddy17/UpNyX_Assignment/blob/main/Images/Chat.png?raw=true)

Now for this operation it will cost 100 tokens now again run with URL
http://127.0.0.1:8000/api/tokens/

and click send you will see some thing like this
$$$You will see something like this
![image alt](https://github.com/ChaituReddy17/UpNyX_Assignment/blob/main/Images/Token.png?raw=true)

as you see the tokens were deducted from the balance Tokens
