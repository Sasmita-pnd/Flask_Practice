from loan_app import app
import pytest

#test client that makes request to the application without
#running the live server

@pytest.fixture
def client():
    return app.test_client()


def test_ping(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_predictions (client):
    test_data= {
                "ApplicantIncome":10,
                "Credit_History":1.0,
                "Gender":"Male",
                "LoanAmount":111111,
                "Married":"Yes"
                }

    resp = client.post("/predict", json= test_data)

    assert resp.status_code == 200
    assert resp.json == {'Loan Approval Status': 'Not Approved'}