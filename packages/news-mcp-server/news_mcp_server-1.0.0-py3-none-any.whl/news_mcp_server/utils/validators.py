"""Validation utilities for News MCP Server."""

import re
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urlparse


def validate_query_params(params: Dict[str, Any]) -> List[str]:
    """
    Validate news query parameters.

    Args:
        params: Query parameters to validate

    Returns:
        List of validation errors (empty if valid)
    """
    errors = []

    # Required parameters
    if not params.get("query_text"):
        errors.append("query_text is required")

    # Validate query text
    query_text = params.get("query_text", "")
    if isinstance(query_text, str):
        if len(query_text.strip()) == 0:
            errors.append("query_text cannot be empty")
        elif len(query_text) > 1000:
            errors.append("query_text cannot exceed 1000 characters")
    else:
        errors.append("query_text must be a string")

    # Validate count
    count = params.get("count", 20)
    if not isinstance(count, int):
        errors.append("count must be an integer")
    elif count < 1 or count > 100:
        errors.append("count must be between 1 and 100")

    # Validate country codes
    country_code = params.get("country_code")
    if country_code:
        if not validate_country_codes(country_code):
            errors.append("Invalid country code format. Use ISO-3166-1 alpha-2 codes (e.g., 'US,CA')")

    # Validate language codes
    lang_code = params.get("lang_code")
    if lang_code:
        if not validate_language_codes(lang_code):
            errors.append("Invalid language code format. Use ISO-639-1 codes (e.g., 'en,es')")

    # Validate sort option
    sort_option = params.get("sort", "latest")
    if sort_option not in ["latest", "relevance"]:
        errors.append("sort must be 'latest' or 'relevance'")

    # Validate search_after (pagination cursor)
    search_after = params.get("search_after")
    if search_after and not isinstance(search_after, str):
        errors.append("search_after must be a string")

    # Validate target_lang_code for translation
    target_lang_code = params.get("target_lang_code")
    if target_lang_code:
        if not validate_language_code(target_lang_code):
            errors.append("Invalid target_lang_code format. Use ISO-639-1 code (e.g., 'en')")

    return errors


def validate_country_codes(country_codes: str) -> bool:
    """
    Validate comma-separated country codes.

    Args:
        country_codes: Comma-separated ISO-3166-1 alpha-2 codes

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(country_codes, str):
        return False

    # Split and validate each code
    codes = [code.strip().upper() for code in country_codes.split(",")]

    for code in codes:
        if not re.match(r"^[A-Z]{2}$", code):
            return False

    return len(codes) > 0


def validate_language_codes(lang_codes: str) -> bool:
    """
    Validate comma-separated language codes.

    Args:
        lang_codes: Comma-separated ISO-639-1 codes

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(lang_codes, str):
        return False

    # Split and validate each code
    codes = [code.strip().lower() for code in lang_codes.split(",")]

    for code in codes:
        if not re.match(r"^[a-z]{2}$", code):
            return False

    return len(codes) > 0


def validate_language_code(lang_code: str) -> bool:
    """
    Validate a single language code.

    Args:
        lang_code: ISO-639-1 language code

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(lang_code, str):
        return False

    return re.match(r"^[a-z]{2}$", lang_code.strip().lower()) is not None


def validate_api_response(response: Dict[str, Any]) -> List[str]:
    """
    Validate API response structure.

    Args:
        response: API response to validate

    Returns:
        List of validation errors (empty if valid)
    """
    errors = []

    # Check if response is a dictionary
    if not isinstance(response, dict):
        errors.append("Response must be a dictionary")
        return errors

    # Validate MCP JSON-RPC structure
    if "jsonrpc" not in response:
        errors.append("Response missing 'jsonrpc' field")
    elif response["jsonrpc"] != "2.0":
        errors.append("Invalid jsonrpc version, expected '2.0'")

    if "id" not in response:
        errors.append("Response missing 'id' field")

    # Must have either result or error
    has_result = "result" in response
    has_error = "error" in response

    if not has_result and not has_error:
        errors.append("Response must contain either 'result' or 'error'")
    elif has_result and has_error:
        errors.append("Response cannot contain both 'result' and 'error'")

    # Validate error structure if present
    if has_error:
        error = response["error"]
        if not isinstance(error, dict):
            errors.append("Error must be a dictionary")
        else:
            if "code" not in error:
                errors.append("Error missing 'code' field")
            elif not isinstance(error["code"], int):
                errors.append("Error code must be an integer")

            if "message" not in error:
                errors.append("Error missing 'message' field")
            elif not isinstance(error["message"], str):
                errors.append("Error message must be a string")

    # Validate result structure if present
    if has_result:
        result = response["result"]
        if isinstance(result, dict) and "items" in result:
            items = result["items"]
            if not isinstance(items, list):
                errors.append("Result items must be a list")
            else:
                # Validate each news item
                for i, item in enumerate(items):
                    item_errors = validate_news_item(item, f"Item {i}")
                    errors.extend(item_errors)

    return errors


def validate_news_item(item: Dict[str, Any], context: str = "News item") -> List[str]:
    """
    Validate a single news item.

    Args:
        item: News item to validate
        context: Context for error messages

    Returns:
        List of validation errors
    """
    errors = []

    if not isinstance(item, dict):
        errors.append(f"{context}: must be a dictionary")
        return errors

    # Required fields
    required_fields = ["id", "title", "url", "source", "lang_code", "country_code", "ts"]

    for field in required_fields:
        if field not in item:
            errors.append(f"{context}: missing required field '{field}'")

    # Validate field types and formats
    if "url" in item:
        if not validate_url(item["url"]):
            errors.append(f"{context}: invalid URL format")

    if "ts" in item:
        if not isinstance(item["ts"], (int, float)):
            errors.append(f"{context}: timestamp 'ts' must be a number")

    if "lang_code" in item:
        if not validate_language_code(item["lang_code"]):
            errors.append(f"{context}: invalid language code")

    if "country_code" in item:
        if not re.match(r"^[A-Z]{2}$", item["country_code"]):
            errors.append(f"{context}: invalid country code")

    return errors


def validate_url(url: str) -> bool:
    """
    Validate URL format.

    Args:
        url: URL to validate

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(url, str):
        return False

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def validate_api_key(api_key: str) -> bool:
    """
    Validate API key format.

    Args:
        api_key: API key to validate

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(api_key, str):
        return False

    # Basic validation - adjust based on your API key format
    return len(api_key.strip()) >= 8


def validate_cache_ttl(ttl: Union[int, float]) -> bool:
    """
    Validate cache TTL value.

    Args:
        ttl: TTL value in seconds

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(ttl, (int, float)):
        return False

    return 0 < ttl <= 86400  # Between 1 second and 24 hours


def validate_json_rpc_request(request: Dict[str, Any]) -> List[str]:
    """
    Validate JSON-RPC request structure.

    Args:
        request: JSON-RPC request to validate

    Returns:
        List of validation errors
    """
    errors = []

    if not isinstance(request, dict):
        errors.append("Request must be a dictionary")
        return errors

    # Required fields
    if "jsonrpc" not in request:
        errors.append("Request missing 'jsonrpc' field")
    elif request["jsonrpc"] != "2.0":
        errors.append("Invalid jsonrpc version, expected '2.0'")

    if "method" not in request:
        errors.append("Request missing 'method' field")
    elif not isinstance(request["method"], str):
        errors.append("Method must be a string")

    if "id" not in request:
        errors.append("Request missing 'id' field")

    # Params is optional but must be dict if present
    if "params" in request and not isinstance(request["params"], dict):
        errors.append("Params must be a dictionary")

    return errors


def sanitize_text(text: str, max_length: Optional[int] = None) -> str:
    """
    Sanitize text input by removing control characters and normalizing whitespace.

    Args:
        text: Text to sanitize
        max_length: Maximum length to trim to

    Returns:
        Sanitized text
    """
    if not isinstance(text, str):
        return ""

    # Remove control characters except newlines and tabs
    sanitized = ''.join(char for char in text if ord(char) >= 32 or char in '\n\t')

    # Normalize whitespace
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()

    # Trim length if specified
    if max_length and len(sanitized) > max_length:
        sanitized = sanitized[:max_length].strip()

    return sanitized