import requests
import json
from ..core import account, get_headers

def pay_info(transaction_id):
    """
    Get information about a stars payment transaction
    
    Args:
        transaction_id (str): ID of the transaction
        
    Returns:
        dict: Payment link information
    """
    headers = get_headers()
    
    data = {
        "transaction": 1,
        "id": transaction_id,
        "method": "getBuyStarsLink"
    }
    
    response = requests.post(
        "https://fragment.com/api?hash=" + account.hash,
        headers=headers,
        data=data
    )
    
    return response.json()
