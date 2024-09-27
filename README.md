# fastapi-project

APIs (Application Programming Interfaces) allow different software systems to interact with each other. They can be explained in terms of two components: the client and the server [^1]. When you check your bank account using a mobile app, the mobile app acts as the client, while the relevant bank's database is referred to as the server.

FastAPI is a popular tool used for deploying machine learning models. In this repository, I will explain the steps I followed from Travis Media's video titled '[Why You Need to Learn FastAPI | Hands-on Project](https://www.youtube.com/watch?v=cbASjoZZGIw).' Before explaining the coding steps, let's go over the 7 reasons for choosing FastAPI, as mentioned in the video: (If you want to learn about the cons of FastAPI, click the [link](https://medium.com/sciforce/serving-ml-model-as-an-api-sharing-our-experience-aab8fbfdc27d).)

1.  It’s just plain Python.
2.  Handles requests asynchronously.
3.  Built-in data validation.
4.  Allows type declarations in Python.
5.  Clear error-handling in JSON format.
6.  Built-in authentication support.
7.  Swagger UI built-in for easy API documentation.

#### Step 1
Open the command prompt and enter the following command to navigate to the Desktop

```
cd Desktop
```
#### Step 2 
Create a FastAPI project folder by running the following command in the command prompt


```
mkdir fastapi-project
```

#### Step 3 
Go to fastapi-project folder

```
cd fastapi-project

```
#### Step 4

Create your virtual environment

```
python -m venv venv
```
#### Step 5

Open Visual Studio Code by entering the following command in the command prompt

```
code .
```

#### Step 6

From now on, we will write our code in __Visual Studio Code's terminal__. Activate the virtual environment you created earlier by running the following command in Visual Studio Code's terminal:
```
.venv/Scripts/activate
```

#### Step 7

Install FastAPI

```
pip install fastapi
```

#### Step 8

Install Uvicorn, which is the server that will run our API

```
python -m pip install -upgrade pip
```

```
pip install "uvicorn[standard]"

```

#### Step 9

Navigate to the ```fastapi-project``` folder and create  [```main.py```](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/main.py) files and [```models.py```](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/models.py). 

In ```models.py```, you construct a request body, which is the data sent by the client to the API [^2]. You import ```BaseModel``` from the ```Pydantic``` module to declare your data as a class. 

#### Step 10
Run Uvicorn using the code below. If you encounter a syntax error while updating the code, it will stop running. You will need to restart Uvicorn using the command again. 

```
uvicorn main:app --reload

```
You will see a message in your terminal like: "Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)". Copy the link provided and append /docs to it, resulting in http://127.0.0.1:8000/docs. If you open this link in a web browser, you will see the user interface for your Todo App, as shown below.

<img src="[https://github.com/favicon.ico](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/fastapi_img.png)" width="15">

![screenshot](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/fastapi_img.png)


[^1]: [Reference 1](https://aws.amazon.com/what-is/api/)
[^2]: [Refernce 2](https://fastapi.tiangolo.com/tutorial/body/)
