# FastAPI-management-system
A School Management System that allows registration, reading and deleting students from the system

# Installation


### Create Virtual Environment & install dependencies
`python3 -m venv env`

### Activate Virtual Environment
`source env/bin/activate`

### Install the dependencies
`pipenv install -r requirements.txt`



# Database
If you are using Linux Install MongoDB using the following commands:

`wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -`

 Create the file `/etc/apt/sources.list.d/mongodb-org-5.0.list file for Ubuntu 20.04 (Focal)`
 
`sudo apt-get update`

`sudo apt-get install -y mongodb-org`

`sudo systemctl start mongod`

`sudo systemctl status mongod`

https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

# Running the app

### Run Server
`uvicorn app:app --reload`

### Launch browser
Launch browser to http://localhost:8000/docs/ 

# Running the Tests
### unit tests
`pytest`
