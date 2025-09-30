import base64
import re
from typing import Optional


def pad_base64(s: str) -> str:
    """Добавить '=' до кратности 4 для корректного base64."""
    return s + "=" * ((4 - len(s) % 4) % 4)


def find_printable_text(b: bytes, min_len: int = 5) -> Optional[str]:
    """
    Ищет в байтах самую первую подпоследовательность печатаемых символов
    (включая пробел, таб, переносы строки), длиной >= min_len.
    Возвращает строку (utf-8, с игнорированием ошибок) или None.
    """
    # Переведём байты в безопасное utf-8-представление с заменой ошибок,
    # чтобы regex мог работать. Но сохранём оригинал для точности.
    try:
        s = b.decode('utf-8', errors='ignore')
    except Exception:
        s = ''.join(chr(c) if 32 <= c <= 126 or c in (9, 10, 13) else ' ' for c in b)

    # Паттерн: печатаемые ASCII + таб + \r\n
    pattern = re.compile(r'[\t\r\n\x20-\x7E]{' + str(min_len) + r',}')
    m = pattern.search(s)
    if m:
        return m.group(0)
    return None


def to_json_result(payload: str, decoded_text: str) -> dict:
    """Форматирует результат в словарь"""
    obj = {
        "payload": payload,
        "decoded": decoded_text
    }
    return obj


def decoder(payload: str) -> dict:
    """
    Декодируем payload в читаемый текст и возвращаем в виде словаря.
    
    Args:
        payload (str): Base64 закодированная строка для декодирования
        
    Returns:
        dict: Словарь с исходным payload и декодированным текстом
        
    Example:
        >>> from Fragment import Fragment
        >>> result = Fragment.utils.decoder("te6ccgEBAQEAJwAaSgAAAAA1MCBUZWxlZ3JhbSBTdGFycyAKClJlZiNJbTJ5NWl0ZDY")
        >>> print(result["decoded"])
        50 Telegram Stars 
        
        Ref#Im2y5itd6
        >>> print(result["payload"])
        te6ccgEBAQEAJwAaSgAAAAA1MCBUZWxlZ3JhbSBTdGFycyAKClJlZiNJbTJ5NWl0ZDY
    """
    padded = pad_base64(payload.strip())
    try:
        raw = base64.b64decode(padded, validate=False)
    except Exception as e:
        # если base64 невалидный — попробуем худший сценарий
        raw = payload.encode('utf-8', errors='ignore')

    # Попробуем прямое utf-8 декодирование (с игнором ошибок)
    try:
        decoded_utf = raw.decode('utf-8', errors='ignore')
    except Exception:
        decoded_utf = ''

    # Если получилось осмысленное (есть >=3 печатаемых подряд символов) — возвращаем
    cleaned = find_printable_text(raw, min_len=3)  # минимальная длина 3 — гибче
    if cleaned:
        # устраняем ведущие/хвостовые пробелы, но сохраняем переносы строк внутри
        cleaned = cleaned.strip('\r\n')
        return to_json_result(payload, cleaned)

    # fallback: если ничего не найдено — возвращаем utf-8 с игнорированием ошибок
    if decoded_utf:
        return to_json_result(payload, decoded_utf.strip())

    # последний форс-мажор: показать repr байтов
    return to_json_result(payload, repr(raw))
