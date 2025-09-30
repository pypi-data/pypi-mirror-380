import requests
from bs4 import BeautifulSoup
import json
from ..core import account

def price(months=12):
    """
    Get premium subscription pricing options
    
    Args:
        months (int): Number of months for premium subscription (default: 12)
        
    Returns:
        dict: Premium subscription options and TON rate information
    """
    url = f"https://fragment.com/premium/gift?months={months}"
    
    headers = {
        "Host": "fragment.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Upgrade-Insecure-Requests": "1"
    }
    
    cookies = {
        "stel_ssid": account.stel_ssid,
        "stel_dt": account.stel_dt,
        "stel_token": account.stel_token,
        "stel_ton_token": account.stel_ton_token
    }
    
    resp = requests.get(url, headers=headers, cookies=cookies)
    
    soup = BeautifulSoup(resp.text, "html.parser")
    
    data = {"options": [], "tonRate": None}
    
    # Parse subscription options
    options = soup.select(".tm-form-radio-item")
    for opt in options:
        duration = opt.select_one(".tm-radio-label").text.strip() if opt.select_one(".tm-radio-label") else None
        price_ton = opt.select_one(".tm-value").text.strip() if opt.select_one(".tm-value") else None
        price_usd = opt.select_one(".tm-radio-desc").text.strip() if opt.select_one(".tm-radio-desc") else None
        sale = opt.select_one(".tm-radio-label-badge").text.strip() if opt.select_one(".tm-radio-label-badge") else None
        
        data["options"].append({
            "duration": duration,
            "price_ton": price_ton,
            "price_usd": price_usd,
            "sale": sale
        })
    
    # Extract TON rate from ajInit JavaScript data
    if "ajInit(" in resp.text:
        start = resp.text.find("ajInit(") + 7
        end = resp.text.find(");", start)
        aj_data = resp.text[start:end]
        try:
            aj_json = json.loads(aj_data)
            if "state" in aj_json and "tonRate" in aj_json["state"]:
                data["tonRate"] = aj_json["state"]["tonRate"]
        except:
            pass
    
    return data
