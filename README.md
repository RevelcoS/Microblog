# Microblog
This is the website for blogs followed by the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)


## Features

Register new account

![Register](https://raw.githubusercontent.com/RevelcoS/Microblog/master/overview/register.png)

Login to your account (you can reset your password)

![Login](https://raw.githubusercontent.com/RevelcoS/Microblog/master/overview/login.png)

Post a blog

![Post](https://raw.githubusercontent.com/RevelcoS/Microblog/master/overview/post.png)

Explore other blogs

![Explore](https://raw.githubusercontent.com/RevelcoS/Microblog/master/overview/explore.png)

Follow users

![Followe](https://raw.githubusercontent.com/RevelcoS/Microblog/master/overview/follow.png)

Edit your account

![Edit](https://raw.githubusercontent.com/RevelcoS/Microblog/master/overview/edit.png)


## Install
To install the application open command prompt and clone the repository:
```
git clone https://github.com/RevelcoS/Microblog
```
Cd into the microblog directory and setup the virtual environment:
```sh
py -3 -m venv venv
```
Activate the environment:
```sh
venv\Scripts\activate
```
Install the packages:
```sh
pip install -r requirements.txt
```
Setup environment variables:
```sh
set FLASK_APP=microblog.py
```

## Run locally
Type the next command in cmd (with environment activated):
```sh
flask run
```
Go to http://127.0.0.1:5000/ and explore!