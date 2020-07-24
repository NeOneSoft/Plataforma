# Plataforma API
Python3.8/Django 3.0 


#Modules:

- products

#Requeriments:

- Python 3.8(Last version)

Before running please follow this steps:

- 1- Create new folder
- 2- Clone this repository and move the unzipped folder to new folder created previously
- 3- Open your terminal and move it to the path folder created on step 1
- 4- Create a virtual environment using the next command(MacOS):
```
                            python3 -m venv <yourvenvname>
```    

#Running local Plataforma API  

- 1- Open your cloned repository (located in your new folder created previously) using
     your code editor preference (PyCharm, VisualStudioCode, ...)
- 2- Open your code editor's terminal and use "cd .." command to move one folder back into directory path
- 3- Activate your virtual environment using the next command(MacOS):
```
                            source <yourvenvname>/bin/activate
```
- 4- Once you have activated your virtual environment, return to your cloned repository (this should be one up folder) using "cd <reponame>" command 
- 5- Install all requirements located in requirements.txt file using the next command:
```
                            pip install -r requirements.txt
```
- 6- Done!!! You can run your local server using the nex command (MacOS):
```
                            python3 manage.py runserver
```
- 7- Open your browser at **127.0.0.1:8000**

#AWS Deploy
```
plat-venv) Gonzalos-MacBook-Air:plataforma gonzaloromero$ eb status
Environment details for: plataforma-dev
  Application name: plataforma
  Region: us-west-2
  Deployed Version: app-97ac-200723_231358
  Environment ID: e-tpwdwdhr3s
  Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Python 3.7 running on 64bit Amazon Linux 2/3.0.3
  Tier: WebServer-Standard-1.0
  CNAME: plataforma-test-eb-dns.us-west-2.elasticbeanstalk.com
  Updated: 2020-07-24 04:17:44.991000+00:00
  Status: Ready
  Health: Red
```


#CURL API use(MacOS)

- 1- Open your terminal
- 2- Use the follow command in your terminal and press ENTER
(Note: Be sure that your local server 127.0.0.1:8000 is running)
```
                            http://127.0.0.1:8000/api/products/
```
- 3- DONE! You will get JSON object with you stored products


#Accessing to Admin Module
 If you want to access to admin module create a superuser following the next steps:
- On your code editor's terminal type the nex command(MacOS) and follow the prompt instructions:
```
                            python3 manage.py createsuperuser
```
Once you have created a superuser go to the next url and access with your superuser credentials
- **http://127.0.0.1:8000/admin/**
Now you can access to admin module's dashboard

#Local API Rest urls
- **http://127.0.0.1:8000/api/products/bulk_insert/**
- **http://127.0.0.1:8000/api/products/**


#Admin url
- **http://127.0.0.1:8000/admin/**
