import pytest
import requests
import json


def test_api_recommend():
    req = [{"ncm_dmtp": 1, "ncm_sl": 3, "ncm_dmdvt": 1}]
    API_URL = f'http://localhost:5000/api/thuc-pham/goi-y?recommend_request={json.dumps(req)}'
    api_response = requests.get(API_URL)
    assert api_response.status_code == 200
