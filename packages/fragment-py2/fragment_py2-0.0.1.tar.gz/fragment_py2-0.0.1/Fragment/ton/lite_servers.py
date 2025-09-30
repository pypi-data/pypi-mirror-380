import requests
import json
import random
import socket
import struct

def lite_server_list():
    """
    Fetches the TON global config containing liteserver list
    
    Returns:
        dict: The JSON response with liteserver configuration
    """
    url = "https://ton-blockchain.github.io/global.config.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch TON config: {response.status_code}")

def lite_server_random():
    """
    Returns a random liteserver from the TON global config
    
    Returns:
        dict: A randomly selected liteserver with IP converted to human-readable format
    """
    config = lite_server_list()
    liteservers = config.get("liteservers", [])
    
    if not liteservers:
        raise Exception("No liteservers found in config")
    
    # Select a random liteserver
    server = random.choice(liteservers)
    
    # Convert the IP from integer to human-readable format
    ip_int = server.get("ip")
    if ip_int is not None:
        # Convert signed int32 to unsigned int32 if negative
        if ip_int < 0:
            ip_int = ip_int + 2**32
            
        # Convert to IP string
        ip_str = socket.inet_ntoa(struct.pack("!I", ip_int))
        
        # Create a copy with the IP in human-readable format
        server_copy = server.copy()
        server_copy["ip_readable"] = ip_str
        return server_copy
    
    return server 