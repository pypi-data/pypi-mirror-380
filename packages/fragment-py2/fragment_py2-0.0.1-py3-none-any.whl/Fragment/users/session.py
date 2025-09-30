import requests
from bs4 import BeautifulSoup
import json
import re
from ..core import account, get_headers

URL = "https://fragment.com/my/sessions"


def parse_sessions():
    session = requests.Session()
    
    # Create direct cookies dict like in test.py
    cookies = {
        "stel_ssid": account.stel_ssid,
        "stel_dt": account.stel_dt,
        "stel_token": account.stel_token,
        "stel_ton_token": account.stel_ton_token
    }
    
    headers = {
        "Host": "fragment.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Upgrade-Insecure-Requests": "1",
    }
    
    # Pass cookies as a separate parameter exactly like in test.py
    response = session.get(URL, headers=headers, cookies=cookies)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # --- Инфа об аккаунте ---
    account_info = {}

    # Ник + аватар
    user_btn = soup.select_one(".tm-header-action .btn .tm-button-label")
    if user_btn:
        account_info["username"] = user_btn.get_text(strip=True)

    user_img = soup.select_one(".tm-header-button-photo img")
    if user_img and user_img.get("src"):
        account_info["avatar"] = user_img["src"]

    # Адрес TON-кошелька
    wallet = soup.select_one(".tm-wallet")
    if wallet:
        account_info["ton_wallet"] = wallet.get_text(strip=True)

    # ton_proof и address из JS
    script = soup.find("script", id="aj_script")
    if script:
        match = re.search(r'Wallet\.init\((\{.*?\})\);', script.text, re.S)
        if match:
            try:
                wallet_data = json.loads(match.group(1))
                account_info.update(wallet_data)
            except:
                pass

    # --- Сессии ---
    sessions = []
    rows = soup.select("table.tm-table tbody tr")
    for row in rows:
        session_data = {}

        # Device
        device = row.select_one(".table-cell-value.tm-value")
        if device:
            session_data["device"] = device.get_text(strip=True)

        # Current / Terminate
        status = row.select_one(".table-cell-status-thin")
        if status:
            session_data["status"] = status.get_text(strip=True)

        # Локация
        location = row.select_one(".table-cell-desc-col")
        if location:
            session_data["location"] = location.get_text(strip=True)

        # Дата
        date_tag = row.select_one("time")
        if date_tag:
            session_data["datetime"] = date_tag.get("datetime")
            session_data["date_text"] = date_tag.get_text(strip=True)
        else:
            # "now"
            date_cell = row.select_one("td.wide-only .tm-value")
            if date_cell:
                session_data["date_text"] = date_cell.get_text(strip=True)

        # session_id
        action_div = row.select_one(".tm-table-actions")
        if action_div and action_div.get("data-session-id"):
            session_data["session_id"] = action_div["data-session-id"]

        sessions.append(session_data)

    result = {
        "account": account_info,
        "sessions": sessions
    }

    return result


if __name__ == "__main__":
    data = parse_sessions()
    print(json.dumps(data, indent=2, ensure_ascii=False))
