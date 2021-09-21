
A django application that can help you track the quality of your projects by having other developers rank your posted projects. The projects are rated based on their usability, content and Design


## Admin Dashboard credentials
username : Amin
password :Amin1234


## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## Setup and Installation  
To get the project follow these steps:

##### Cloning the repository:  
 ```bash 
https://github.com/Amin1014/django-ip3.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd django-ip3 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
``` 
 ##### Setup Database
 Create a .env file and fill in the configurations for your database and application.
 python manage.py makemigrations projects
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
## Known Bugs
- My app only rates and comments in the admin dashboard
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  

  
  
## Contact Information   
If you have any question or contributions, please email me at [mohamed.amin@student.moringaschool@gmail.com] 

## License 
* Copyright (c) 2021 **Mohamed Amin**