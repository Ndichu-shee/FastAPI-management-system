from fastapi.testclient import TestClient 

from app import app 

client = TestClient(app)

data = {
                "first_name":"Joyce",
                "last_name":"Ndichu",
                "age":23,
                "nationality":"Kenyan",
                "class_name":"LisaLab",
                "nationality_id":"23763722",
                "email":"ndichujoyce@gmail.com",
                "room":"Tanga",
            } 




def test_add_student():

    response = client.post("/Student",json=data)
    assert response.status_code == 201
    assert response.json()==data



    
