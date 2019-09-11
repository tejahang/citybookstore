# Welcome to citybookstore!

**citybookstore** is an online platform for buying/selling used books. However, this is only a working prototype.


## Features

Although a prototype, it still packs enough to be called a lightweight e-commerce web-app.

- Book Listing : publish the book you want to sell.
- User Registration and Login.
- Search Tool
- Cart
- Friendly UI

## Dependencies 

- Django==2.1.7
- mysqlclient==1.4.2.post1
- sorl-thumbnail==12.5.0


> **Note:** The **Publish now** button is disabled if your file has not been published yet.


## Installation

- clone or download the project
	```sh
	git clone https://github.com/tejahang/citybookstore.git 
	```
- create a virtual environment
- install  dependencies 
	```sh
	pip install -r requirements.txt 
	```
- start server
	```sh
	python manage.py startserver
	```
