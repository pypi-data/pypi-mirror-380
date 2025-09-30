
import requests
import json
from ..core import account, get_headers

def pay_init(recipient, quantity):
    """
    Initialize payment for stars
    
    Args:
        recipient (str): Recipient's hash/identifier
        quantity (int): Amount of stars to send
        
    Returns:
        dict: Contains req_id, myself, to_bot, and amount information
    """
    headers = get_headers()
    
    data = {
        "recipient": recipient,
        "quantity": quantity,
        "method": "initBuyStarsRequest"
    }
    
    response = requests.post(
        "https://fragment.com/api?hash=" + account.hash,
        headers=headers,
        data=data
    )
    
    result = response.json()
    
    # Extract only the required fields
    return {
        "req_id": result.get("req_id"),
        "myself": result.get("myself"),
        "to_bot": result.get("to_bot"),
        "amount": result.get("amount")
    } 