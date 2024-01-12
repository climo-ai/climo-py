import requests 

def list_models(users=None, areas=None, tags=None):
    """
    List all the models on the climo.ai platform according to specified filters
    """
    pass

def check_username(username):
    endpoint = "http://127.0.0.1:8000/check-username/"
    response = requests.post(endpoint, json={'username': username})
    return response.json()
