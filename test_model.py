from main import app
import pytest

@pytest.fixture
def client():
    return app.test_client()



def test_models(client):
    resp = client.get("/model_test")
    assert resp.status_code == 200
    assert resp.json == {"Model_List" : ["Decision Tree Model" , "Ranfom Forest Model", \
                                         "Extreme Gradient Boosted Machine [xgboost]", \
                                            "Light Gradient Boosting Machine [lightGBM]"]}


    