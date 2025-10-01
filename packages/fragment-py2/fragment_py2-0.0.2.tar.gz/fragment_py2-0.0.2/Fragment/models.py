from dataclasses import dataclass, field
from typing import Optional, List, Any, Dict


class DynamicObject:
    """Базовый класс для динамического создания объектов из словарей с поддержкой точечной нотации"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, DynamicObject(**value))
            elif isinstance(value, list):
                setattr(self, key, [
                    DynamicObject(**item) if isinstance(item, dict) else item 
                    for item in value
                ])
            else:
                setattr(self, key, value)
    
    def __getitem__(self, key):
        """Для обратной совместимости со словарями"""
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        """Для обратной совместимости со словарями"""
        setattr(self, key, value)
    
    def __contains__(self, key):
        """Для обратной совместимости со словарями"""
        return hasattr(self, key)
    
    def get(self, key, default=None):
        """Для обратной совместимости со словарями"""
        return getattr(self, key, default)
    
    def keys(self):
        """Для обратной совместимости со словарями"""
        return self.__dict__.keys()
    
    def values(self):
        """Для обратной совместимости со словарями"""
        return self.__dict__.values()
    
    def items(self):
        """Для обратной совместимости со словарями"""
        return self.__dict__.items()
    
    def to_dict(self):
        """Конвертация обратно в словарь"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, DynamicObject):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [
                    item.to_dict() if isinstance(item, DynamicObject) else item
                    for item in value
                ]
            else:
                result[key] = value
        return result
    
    def __repr__(self):
        attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items() if not k.startswith('_'))
        return f"{self.__class__.__name__}({attrs})"


# ==================== STARS MODELS ====================

class StarsPrice(DynamicObject):
    """Результат запроса цены на Stars с поддержкой точечной нотации"""
    pass


class PaymentInit(DynamicObject):
    """Результат инициализации платежа Stars с поддержкой точечной нотации"""
    pass


class PaymentInfo(DynamicObject):
    """Информация о платеже Stars с поддержкой точечной нотации"""
    pass


# ==================== PREMIUM MODELS ====================

class PremiumPrice(DynamicObject):
    """Информация о ценах на премиум с поддержкой точечной нотации"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Конвертируем options в DynamicObject если это список словарей
        if hasattr(self, 'options') and isinstance(self.options, list):
            self.options = [
                DynamicObject(**opt) if isinstance(opt, dict) else opt 
                for opt in self.options
            ]


# ==================== USER MODELS ====================

class UserProfile(DynamicObject):
    """Профиль пользователя Fragment с поддержкой точечной нотации"""
    pass


class SessionList(DynamicObject):
    """Список сессий пользователя с поддержкой точечной нотации"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Конвертируем account в DynamicObject если это словарь
        if hasattr(self, 'account') and isinstance(self.account, dict):
            self.account = DynamicObject(**self.account)
        # Конвертируем sessions в список DynamicObject если это список словарей
        if hasattr(self, 'sessions') and isinstance(self.sessions, list):
            self.sessions = [
                DynamicObject(**s) if isinstance(s, dict) else s 
                for s in self.sessions
            ]


# ==================== UTILS MODELS ====================

class NickToHashResult(DynamicObject):
    """Результат поиска ника с поддержкой точечной нотации"""
    pass


class DecoderResult(DynamicObject):
    """Результат декодирования payload с поддержкой точечной нотации"""
    pass


# ==================== TON MODELS ====================

class WalletBalanceResult(DynamicObject):
    """Результат проверки баланса кошелька с поддержкой точечной нотации"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Конвертируем balance в DynamicObject если это словарь
        if hasattr(self, 'balance') and isinstance(self.balance, dict):
            self.balance = DynamicObject(**self.balance)


class SendResult(DynamicObject):
    """Результат отправки TON с поддержкой точечной нотации"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Конвертируем transaction в DynamicObject если это словарь
        if hasattr(self, 'transaction') and isinstance(self.transaction, dict):
            self.transaction = DynamicObject(**self.transaction)
        # Конвертируем balance в DynamicObject если это словарь  
        if hasattr(self, 'balance') and isinstance(self.balance, dict):
            self.balance = DynamicObject(**self.balance)


class LiteServer(DynamicObject):
    """Информация о lite сервере TON с поддержкой точечной нотации"""
    pass
