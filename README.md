# FastAPI-management-system
A School Management System that allows registration, reading and deleting students from the system

# Installation

### Install pipenv
`pip install  pipenv`

### Create Virtual Environment & install dependencies
`pipenv install -r requirements.txt --python=python3`

### Activate Virtual Environment
`pipenv shell`

# Database
If you are using Linux Install MongoDB using the following commands:

`wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -`

 Create the file `/etc/apt/sources.list.d/mongodb-org-5.0.list file for Ubuntu 20.04 (Focal)`
 
`sudo apt-get update`

`sudo apt-get install -y mongodb-org`

`sudo systemctl start mongod`

`sudo systemctl status mongod`
# Running the app

### Run Server
`uvicorn app:app --reload`

### Launch browser
Launch browser to http://localhost:8000/docs/ 

# Running the Tests
### unit tests
`pytest`
