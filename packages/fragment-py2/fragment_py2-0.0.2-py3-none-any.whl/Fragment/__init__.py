from .core import account, user, get_headers
from .utils.nick_to_hash import nick_to_hash
from . import utils
from .stars import price, pay_init, pay_info
from .premium import price as premium_price
from .ton import lite_server_list, lite_server_random
from .ton import wallet

# Create a class that will serve as the Fragment namespace
class FragmentNamespace:
    def __init__(self):
        self.account = account
        self.user = UserNamespace()
        self.utils = UtilsNamespace()
        self.stars = StarsNamespace()
        self.premium = PremiumNamespace()
        self.ton = TonNamespace()

class UserNamespace:
    def __init__(self):
        self.nick_to_hash = nick_to_hash

class UtilsNamespace:
    def __init__(self):
        self.decoder = utils.decoder
        self.nick_to_hash = nick_to_hash

class StarsNamespace:
    def __init__(self):
        self.price = price
        self.pay_init = pay_init
        self.pay_info = pay_info

class PremiumNamespace:
    def __init__(self):
        self.price = premium_price

class TonNamespace:
    def __init__(self):
        self.lite_server_list = lite_server_list
        self.lite_server_random = lite_server_random
        self.wallet = WalletNamespace()

class WalletNamespace:
    def __init__(self):
        self.balance = wallet.balance
        self.v4r2 = wallet.v4r2

# Create the Fragment instance to be imported
Fragment = FragmentNamespace()

# Export only Fragment
__all__ = ["Fragment"] 