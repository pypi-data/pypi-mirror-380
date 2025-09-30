import requests
import json
from ..core import account, get_headers

def nick_to_hash(nickname):
    """
    Convert a nickname to hash by querying the Fragment API
    
    Args:
        nickname (str): The nickname to look up
        
    Returns:
        dict: JSON response from the API
    """
    url = "https://fragment.com/api"
    
    # Use parameters from account
    params = {
        "hash": account.hash
    }
    
    # Get headers from core
    headers = get_headers()
    
    data = {
        "query": nickname,
        "quantity": "",
        "method": "searchStarsRecipient"
    }
    
    response = requests.post(url, headers=headers, params=params, data=data)
    return response.json() 