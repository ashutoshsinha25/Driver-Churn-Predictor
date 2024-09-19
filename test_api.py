from main import app
import pytest

@pytest.fixture
def client():
    return app.test_client()


def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE" : "Hi, I am Pinging V1...!!!!!"}


def test_predict(client):
    test_data = { 
    "total_months":5,
    "age":26,
    "gender":0,
    "city":'C1',
    "education":2,
    "income":40318,
    "DOJ":"07-08-2020",
    "joining_designation":1,
    "grade":1,
    "total_business_val":0,
    "quarterly_rating":1,
    "quarterly_rating_increased":0,
    "income_increased":0
    }
    resp = client.post('/api_test', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"Model_Prediction" : 0} or resp.json == {"Model_Prediction" : 1}