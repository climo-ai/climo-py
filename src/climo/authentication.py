import os

def set_token(token):
    """
    Set API token in the environment
    """
    os.environ['CLIMO_API_KEY'] = token

def token():
    """
    Return user token
    """
    return os.environ.get('CLIMO_API_KEY')