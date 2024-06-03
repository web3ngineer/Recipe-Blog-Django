# Setup Django
### Method-1
step1: ```pip install virtualenv```
step2: ```virtualenv venv```
step3: ```source venv/Scripts/activate```
or
step1: ```python -m venv .venv```
step-2: ```source .venv/Scripts/activate```


### Method-2
step1: ```pip install uv```
step2: ```uv venv```
step-3: ```source .venv\Scripts\activate```

## Installing Django
1. ```pip install django``` or ```uv pip install django```
2. ```django-admin startproject <project-name>```

#### Run Server
1. ```cd <project-name>```
2. ```python manage.py runserver```

#### Create app
1. ```cd <project-name>```
2. ```python manage.py startapp <app-name>```

## Models
1. create models
2. ```python manage.py makemigrations```
3. ```python manage.py migrate```

## Django Shell
```python manage.py shell```

```python
from home.models import *
student = Student(name="shivam Singh", age="21", email="shivamsingh175503@gmail.com", phone="7275098558")
student.save()                        
```
or by Model Manager
```python
student = Student.objects.create(name="Ram", age="22", email="ram12@gmail.com", phone="1234567890", address = "india")
```
See All Students Details
```python
Student.objects.all() # returns array
Student.objects.all()[0] # returns first element in the from of object(dictionary)
Student.objects.all()[0].name  # returns the name field 
Student.objects.all()[0].email 
```

CRUD operations

```python
#get all
cars = Car.objects.all()  # returns all cars in array
# get one
car = Car.objects.get(id=1) # returns one car object by id
carByName = Car.objects.get(car_name = "Tata Nexon") # returns car object having name Tata Nexon
# create
car = Car.objects.create(car_name="BMW x4", speed="320")
# update
cars[0].car_name  # returns the name field of first car
cars[0].car_name = "Tata Nano" # change the name of first car
cars[0].save() # save changes in the db
#or
Car.objects.filter(id=1).update(car_name="Tata Nexon")
# delete
Car.objects.filter(id=1).delete() # delete car with id 1
# delete all
Car.objects.all().delete() # delete all cars Car model
```

