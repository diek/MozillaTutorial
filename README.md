# Mozilla Tutorial

## Django Learning Project


## ERD of Models
![ERD of Library Project](./static/images/local_library_model_uml.png)


## Get Project from Github  
Navigate to working folder  
`$: git clone git@github.com:diek/MozillaTutorial.git`  
`$: cd MozillaTutorial`   


## Create and Activate a Virtual Environment for the project (Linux and Mac)  
`$: python3 -m venv _env`  
`$: source _env/bin/activate`  
`$: pip install --upgrade pip`  


## Install Django and related packages   
`$: pip install -r requirements.txt`    


## Run Migrations  
`$: python manage.py migrate catalog`  
`$: python manage.py migrate`  


## Update SITE_AUTHOR  
Goto settings.py and update SITE_AUTHOR as needed  
