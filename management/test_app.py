from fastapi.testclient import TestClient 

from app import app 

client = TestClient(app)

data = {
  "first_name": "ann",
  "last_name": "kate",
  "age": 22,
  "nationality": "Kenyan",
  "class_name": "LisaLab",
  "nationality_id": "23763722",
  "email": "ndichujoyce@gmail.com",
  "room": "Tanga"
}


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "School Management System"}
    
    


def test_add_student():
    response = client.post("/student",json=data)
    assert response.status_code == 201
  

def test_get_student():
    response = client.get("/student/624deb79fcf08002af4d017b")
    assert response.status_code==200


def test_delete_student():
    response = client.get("/student/624deb79fcf08002af4d017b")
    assert response.status_code==200

def test_student_id():
    response = client.get("/student/624")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student id not found, try using another Id"}
