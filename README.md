# fastapi-project

APIs (Application Programming Interfaces) allow different software systems to interact with each other. They can be explained in terms of two components: the client and the server [^1].. When you check your bank account using a mobile app, the mobile app acts as the client, while the relevant bank's database is referred to as the server.

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

Activate the virtual environment you created earlier by running the following command

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

Navigate to the ```fastapi-project``` folder and create a [```main.py```](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/main.py) file. 

#### Step 10

```
uvicorn main:app --reload

```


<img src="[https://github.com/favicon.ico](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/fastapi_img.png)" width="15">

![screenshot](https://github.com/f-kuzey-edes-huyal/fastapi-project/blob/main/fastapi_img.png)


[^1]: [Reference](https://aws.amazon.com/what-is/api/)

