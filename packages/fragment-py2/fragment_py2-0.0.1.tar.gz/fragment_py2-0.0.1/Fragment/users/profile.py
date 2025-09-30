import requests
from bs4 import BeautifulSoup
import json
import re
from ..core import account

URL = "https://fragment.com/my/profile"

def parse_profile():
    session = requests.Session()
    
    # Create direct cookies dict
    cookies = {
        "stel_ssid": account.stel_ssid,
        "stel_dt": account.stel_dt,
        "stel_token": account.stel_token,
        "stel_ton_token": account.stel_ton_token
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://fragment.com/convert"
    }
    
    # Make API request
    response = session.get(URL, headers=headers, cookies=cookies)
    response.raise_for_status()
    data = response.json()
    
    html = data.get("h", "")
    soup = BeautifulSoup(html, "html.parser")
    
    # Аккаунт
    profile_info = {}
    profile_block = soup.select_one(".tm-settings-item.tm-settings-head-item")
    
    if profile_block:
        profile_info["name"] = profile_block.select_one(".tm-settings-item-head").get_text(strip=True)
        profile_info["username"] = profile_block.select_one(".tm-settings-item-desc").get_text(strip=True)
        profile_info["avatar"] = profile_block.select_one("img")["src"] if profile_block.select_one("img") else None
        profile_info["verified"] = bool(profile_block.select_one(".tm-badge-verified"))
    
    # TON Wallet
    wallet_block = soup.select_one(".tm-settings-item.icon-before.icon-menu-wallet")
    if wallet_block:
        profile_info["wallet"] = wallet_block.select_one(".tm-settings-item-desc").get_text(strip=True)
        profile_info["wallet_verified"] = bool(wallet_block.select_one(".tm-badge-verified"))
    
    return profile_info

if __name__ == "__main__":
    data = parse_profile()
    print(json.dumps(data, indent=2, ensure_ascii=False))
