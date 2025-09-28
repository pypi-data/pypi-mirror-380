import base64
import hashlib
import re
from collections import Counter

_ENCODING = "utf-8"


# === Text Analysis ===


def length(text: str) -> int:
    """
    Return the length of the text.
    """
    return len(text)


def count_substr(
    text: str, substr: str, case_sensitive: bool = False, start: int | None = None, end: int | None = None
) -> int:
    """
    Return the number of non-overlapping occurrences of substr.
    Optional arguments start and end are interpreted as in Python slice notation.
    Set case_sensitive = True to match case-sensitively.
    """
    if not case_sensitive:
        text = text.casefold()
        substr = substr.casefold()
    return text.count(substr, start, end)


WORD_RE = re.compile(r"\b[\w']+\b", flags=re.UNICODE)


def most_common_words(text: str, k: int, case_sensitive: bool = False, min_len: int = 2) -> list[tuple[str, int]]:
    """
    Return the k most common words, and their frequencies in descending order.
    Counting is case-insensitive by default, input text is case-folded before counting unless case_sensitive = True.
    Words with length less than min_len are ignored.
    """
    if k < 0:
        raise ValueError(f"k must be non-negative, got {k}")
    if min_len < 0:
        raise ValueError(f"min_len must be non-negative, got {min_len}")

    if not case_sensitive:
        text = text.casefold()
    words = WORD_RE.findall(text)
    words = [word for word in words if len(word) >= min_len]
    return Counter(words).most_common(k)


def first_index_of_substr(
    text: str, substr: str, case_sensitive: bool = False, start: int | None = None, end: int | None = None
) -> int:
    """
    Return the first index of substr in text. If not found, return -1.
    Optional arguments start and end are interpreted as in Python slice notation.
    Set case_sensitive = True to match case-sensitively.
    """
    if not case_sensitive:
        text = text.casefold()
        substr = substr.casefold()
    return text.find(substr, start, end)


def last_index_of_substr(
    text: str, substr: str, case_sensitive: bool = False, start: int | None = None, end: int | None = None
) -> int:
    """
    Return the last index of substr in text. If not found, return -1.
    Optional arguments start and end are interpreted as in Python slice notation.
    Set case_sensitive = True to match case-sensitively.
    """
    if not case_sensitive:
        text = text.casefold()
        substr = substr.casefold()
    return text.rfind(substr, start, end)


# === Text Manipulation ===


def normalize_text(text: str) -> str:
    """
    Return the case-folded text.
    """
    return text.casefold()


def slice_text(text: str, start: int | None = None, end: int | None = None) -> str:
    """
    Return the slice of text from start to end. Optional arguments start and end are
    interpreted as in Python slice notation.
    """
    return text[start:end]


def replace_substr(text: str, old: str, new: str) -> str:
    """
    Return a copy with all occurrences of substring old replaced by new.
    """
    return text.replace(old, new)


# === Hashing ===


def md5(data: str) -> str:
    """
    Return the MD5 hash of the input data as a string of hexadecimal digits.
    """
    return hashlib.md5(data.encode(_ENCODING)).hexdigest()


def sha1(data: str) -> str:
    """
    Return the SHA-1 hash of the input data as a string of hexadecimal digits.
    """
    return hashlib.sha1(data.encode(_ENCODING)).hexdigest()


def sha256(data: str) -> str:
    """
    Return the SHA-256 hash of the input data as a string of hexadecimal digits.
    """
    return hashlib.sha256(data.encode(_ENCODING)).hexdigest()


def sha512(data: str) -> str:
    """
    Return the SHA-512 hash of the input data as a string of hexadecimal digits.
    """
    return hashlib.sha512(data.encode(_ENCODING)).hexdigest()


# === Base64 ===


def base64_encode(data: str) -> str:
    """
    Return the Base64 encoded string of the input data.
    """
    return base64.b64encode(data.encode(_ENCODING)).decode(_ENCODING)


def base64_decode(data: str) -> str:
    """
    Return the Base64 decoded string of the input data.

    Args:
        data: Base64 encoded string to decode
    """
    try:
        return base64.b64decode(data.encode(_ENCODING)).decode(_ENCODING)
    except Exception as e:
        raise ValueError(f"Invalid Base64 input: {data!r}") from e


def base64_urlsafe_encode(data: str) -> str:
    """
    Return the Base64 URL-safe encoded string of the input data.
    """
    return base64.urlsafe_b64encode(data.encode(_ENCODING)).decode(_ENCODING)


def base64_urlsafe_decode(data: str) -> str:
    """
    Return the Base64 URL-safe decoded string of the input data.
    """
    try:
        return base64.urlsafe_b64decode(data.encode(_ENCODING)).decode(_ENCODING)
    except Exception as e:
        raise ValueError(f"Invalid Base64 URL-safe input: {data!r}") from e


# === Hex ===


def hex_encode(data: str) -> str:
    """
    Return the Hex encoded string of the input data.
    """
    return data.encode(_ENCODING).hex()


def hex_decode(data: str) -> str:
    """
    Return the Hex decoded string of the input data.
    """
    if len(data) % 2 != 0:
        raise ValueError(f"Hex string must have even length, got {len(data)}")

    try:
        return bytes.fromhex(data).decode(_ENCODING)
    except ValueError as e:
        raise ValueError(f"Invalid hex string: {data!r}") from e
