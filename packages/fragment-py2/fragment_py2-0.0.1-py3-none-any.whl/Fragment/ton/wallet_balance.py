import requests
from ..core import account

def balance(wallet_address):
    """
    Check the balance of a TON wallet using either toncenter or tonconsole API
    
    Args:
        wallet_address (str): The TON wallet address
        
    Returns:
        dict: Wallet balance information
    """
    # Validate wallet address (basic check)
    if not wallet_address or not isinstance(wallet_address, str):
        raise ValueError("Invalid wallet address")
    
    # First try toncenter if API key is available
    if account.toncenter_api_key:
        return _check_toncenter_balance(wallet_address)
    # Then try tonconsole if API key is available
    elif account.tonconsole_api_key:
        return _check_tonconsole_balance(wallet_address)
    else:
        raise ValueError("No API keys available. Set either account.toncenter_api_key or account.tonconsole_api_key")

def _check_toncenter_balance(wallet_address):
    """
    Check wallet balance using TON Center API
    
    Args:
        wallet_address (str): The TON wallet address
        
    Returns:
        dict: Wallet balance information
    """
    url = "https://toncenter.com/api/v2/getAddressBalance"
    headers = {
        "X-API-Key": account.toncenter_api_key
    }
    params = {
        "address": wallet_address
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()
        
        # Format for consistent return structure
        if response_data.get("ok") and "result" in response_data:
            balance_nano = int(response_data["result"])
            balance_ton = balance_nano / 1_000_000_000  # Convert from nano TON to TON
            
            return {
                "success": True,
                "balance": {
                    "nano": balance_nano,
                    "ton": balance_ton
                },
                "source": "toncenter"
            }
        else:
            error_msg = response_data.get("error", "Unknown error")
            return {
                "success": False,
                "error": error_msg,
                "source": "toncenter"
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "source": "toncenter"
        }

def _check_tonconsole_balance(wallet_address):
    """
    Check wallet balance using TON Console API (tonapi.io)
    
    Args:
        wallet_address (str): The TON wallet address
        
    Returns:
        dict: Wallet balance information
    """
    # Correct URL format for tonapi.io
    url = f"https://tonapi.io/v2/accounts/{wallet_address}"
    
    # Correct header format for tonapi.io
    headers = {
        "Authorization": f"Bearer {account.tonconsole_api_key}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if response is successful
        if response.status_code != 200:
            return {
                "success": False,
                "error": f"API returned status code: {response.status_code}, Response: {response.text}",
                "source": "tonconsole"
            }
        
        response_data = response.json()
        
        # Extract balance directly from the response
        if "balance" in response_data:
            balance_nano = int(response_data["balance"])
            balance_ton = balance_nano / 1_000_000_000  # Convert from nano TON to TON
            
            return {
                "success": True,
                "balance": {
                    "nano": balance_nano,
                    "ton": balance_ton
                },
                "source": "tonconsole"
            }
        else:
            error_msg = "Balance information not found in response"
            return {
                "success": False,
                "error": error_msg,
                "source": "tonconsole"
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "source": "tonconsole"
        }
