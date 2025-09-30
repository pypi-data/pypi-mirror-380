import requests
import re
import json
from ..core import account, get_headers

def price(quantity):
    """
    Get the current price for a specified quantity of stars
    
    Args:
        quantity (int, str): The quantity of stars to price (can be a number or a string containing a number)
        
    Returns:
        dict: Parsed price information in TON and USDT
    """
    # Try to convert string to integer if it's a string
    if isinstance(quantity, str):
        try:
            quantity = int(quantity)
        except ValueError:
            raise TypeError("Quantity must be a valid number")
    
    # Ensure quantity is a number
    if not isinstance(quantity, (int, float)):
        raise TypeError("Quantity must be a number")
    
    quantity = int(quantity)  # Convert to integer
    
    url = "https://fragment.com/api"
    
    # Use parameters from account
    params = {
        "hash": account.hash
    }
    
    # Get headers from core
    headers = get_headers()
    
    data = {
        "stars": 0,
        "quantity": quantity,
        "method": "updateStarsPrices"
    }
    
    response = requests.post(url, headers=headers, params=params, data=data)
    response_data = response.json()
    
    # Check if request was successful
    if not response_data.get("ok"):
        return {"ok": "false"}
    
    # Extract price information from HTML
    html_price = response_data.get("cur_price", "")
    
    # Extract TON price
    ton_match = re.search(r'icon-ton\">(\d+)<span class=\"mini-frac\">\.(\d+)<\/span>', html_price)
    ton_price = "0"
    if ton_match:
        ton_integer = ton_match.group(1)
        ton_fraction = ton_match.group(2)
        ton_price = f"{ton_integer}.{ton_fraction}"
    
    # Extract USDT price - updated regex to handle both formats with and without decimal points
    usdt_match = re.search(r'~&nbsp;&#036;(\d+(?:\.\d+)?)', html_price)
    usdt_price = "0"
    if usdt_match:
        usdt_price = usdt_match.group(1)
    
    # Format the result
    result = {
        "ok": "true",
        "cur_price": {
            "TON": ton_price,
            "USDT": usdt_price
        }
    }
    
    return result
