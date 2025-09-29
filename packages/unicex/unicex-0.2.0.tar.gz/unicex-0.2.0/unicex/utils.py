"""Модуль, который предоставляет дополнительные функции, которые нужны для внутренного использования в библиотеке."""

__all__ = [
    "dict_to_query_string",
    "generate_hmac_sha256_signature",
    "sort_params_by_alphabetical_order",
    "filter_params",
    "batched_list",
    "catch_adapter_errors",
]

import base64
import hashlib
import hmac
import json
from collections.abc import Callable, Iterable
from functools import wraps
from typing import Literal
from urllib.parse import urlencode

from unicex.exceptions import AdapterError


def filter_params(params: dict) -> dict:
    """Фильтрует параметры запроса, удаляя None-значения.

    Параметры:
        params (`dict`): Словарь параметров запроса.

    Возвращает:
        `dict`: Отфильтрованный словарь параметров запроса.
    """
    return {k: v for k, v in params.items() if v is not None}


def sort_params_by_alphabetical_order(params: dict) -> dict:
    """Сортирует параметры запроса по алфавиту.

    Параметры:
        params (`dict`): Словарь параметров запроса.

    Возвращает:
        `dict`: Отсортированный словарь параметров запроса.
    """
    return dict(sorted(params.items()))


def dict_to_query_string(params: dict) -> str:
    """Преобразует словарь параметров в query string для URL.

    - Списки и словари автоматически сериализуются в JSON.
    - Используется стандартная urlencode кодировка.

    Параметры:
        params (`dict`): Словарь параметров запроса.

    Возвращает:
        `str`: Строка параметров, готовая для использования в URL.
    """
    processed = {
        k: json.dumps(v, separators=(",", ":")) if isinstance(v, list | dict) else v
        for k, v in params.items()
    }
    return urlencode(processed, doseq=True)


def generate_hmac_sha256_signature(
    secret_key: str,
    payload: str,
    encoding: Literal["hex", "base64"] = "hex",
) -> str:
    """Генерирует HMAC-SHA256 подпись.

    encoding:
        - "hex" → шестнадцатеричная строка
        - "base64" → base64-строка
    """
    digest = hmac.new(secret_key.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).digest()
    if encoding == "hex":
        return digest.hex()
    elif encoding == "base64":
        return base64.b64encode(digest).decode()
    else:
        raise ValueError("encoding must be 'hex' or 'base64'")


def batched_list[T](iterable: Iterable[T], n: int) -> list[list[T]]:
    """Разбивает последовательность на чанки фиксированного размера.

    Всегда возвращает список списков (list[list[T]]).
    """
    if n <= 0:
        raise ValueError("n must be greater than 0")

    result: list[list[T]] = []
    batch: list[T] = []
    for item in iterable:
        batch.append(item)
        if len(batch) == n:
            result.append(batch)
            batch = []
    if batch:
        result.append(batch)
    return result


def catch_adapter_errors(func: Callable):
    """Декоратор для унификации обработки ошибок в адаптерах.

    Перехватывает все исключения внутри функции и выбрасывает AdapterError
    с подробным сообщением, включающим тип и текст исходного исключения,
    а также имя функции.

    Параметры:
        func (Callable): Декорируемая функция.

    Возвращает:
        Callable: Обёрнутую функцию, выбрасывающую AdapterError при ошибке.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            args_repr = repr(args)
            if len(args_repr) > 200:
                args_preview = args_repr[:200] + "... (truncated)"
            else:
                args_preview = args_repr

            kwargs_repr = repr(kwargs)
            if len(kwargs_repr) > 200:
                kwargs_preview = kwargs_repr[:200] + "... (truncated)"
            else:
                kwargs_preview = kwargs_repr

            raise AdapterError(
                f"({type(e).__name__}): {e}. Can not convert input (args={args_preview}, kwargs={kwargs_preview}) in function `{func.__name__}`."
            ) from e

    return wrapper
