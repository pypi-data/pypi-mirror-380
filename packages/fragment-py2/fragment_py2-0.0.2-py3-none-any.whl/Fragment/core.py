class Account:
    def __init__(self):
        self.hash = ""
        self.stel_ssid = ""
        self.stel_dt = ""
        self.stel_token = ""
        self.stel_ton_token = ""
        self.toncenter_api_key = ""
        self.tonconsole_api_key = ""
        self.wallet_seed = ""
        
    def session_list(self):
        """
        Get list of active Fragment sessions for the account
        
        Returns:
            dict: Account information and active sessions
        """
        from .users.session import parse_sessions
        return parse_sessions()
        
    def profile(self):
        """
        Get Fragment account profile information
        
        Returns:
            dict: Profile information including name, username, avatar, wallet
        """
        from .users.profile import parse_profile
        return parse_profile()

account = Account()

# Create reusable headers function
def get_headers():
    """
    Generate headers for Fragment API requests
    
    Returns:
        dict: Headers with cookies and other required fields
    """
    headers = {
        "Host": "fragment.com",
        "Cookie": f"stel_ssid={account.stel_ssid}; stel_dt={account.stel_dt}; stel_token={account.stel_token}; stel_ton_token={account.stel_ton_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://fragment.com",
        "Referer": "https://fragment.com/stars/buy?quantity=500",
    }
    return headers

class User:
    def __init__(self):
        pass

user = User()

# Make modules available at Fragment.account and Fragment.user
__all__ = ["account", "user", "get_headers"]
