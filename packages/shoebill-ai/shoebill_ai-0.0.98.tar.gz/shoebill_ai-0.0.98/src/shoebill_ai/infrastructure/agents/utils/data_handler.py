import json
import re
import logging

# It's good practice to have a logger instance
logger = logging.getLogger(__name__)


def parse_json_data(json_string: str) -> dict:
    """
    Parses a string to extract and load JSON data, with extensive cleaning and repair.

    This function attempts to handle various common malformations:
    - Extracts JSON from Markdown code blocks.
    - Strips leading/trailing non-JSON content and comments.
    - On failure, attempts a series of advanced repairs before a final parsing attempt.
    """
    if not json_string or not json_string.strip():
        logger.warning("Empty JSON string provided.")
        return {}

    # 1. First, strip any comments from the string
    # Remove /* ... */ and // ...
    json_string = re.sub(r'/\*.*?\*/', '', json_string, flags=re.DOTALL)
    json_string = re.sub(r'//.*', '', json_string)

    # 2. Extract content from Markdown blocks
    match = re.search(r'```(?:json)?\s*({.*?})\s*```', json_string, re.DOTALL)
    if match:
        json_string = match.group(1)
    else:
        # 3. If no markdown, greedily find the main JSON object
        start = json_string.find('{')
        end = json_string.rfind('}')
        if start != -1 and end > start:
            json_string = json_string[start:end + 1]
        else:
            logger.warning("Could not find a valid JSON object structure '{...}' in the string.")
            return {}

    # 4. First attempt to parse the cleaned string
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logger.warning(f"Primary JSON parse failed: {e}. Attempting advanced repair...")

        # 5. If it fails, run the advanced repair function and try again
        repaired_string = _repair_json_string(json_string)
        try:
            data = json.loads(repaired_string)
            logger.info("JSON parsed successfully after advanced repair.")
            return data
        except json.JSONDecodeError as e2:
            logger.error(f"Failed to parse JSON even after advanced repair: {e2}")
            # For debugging, log the repaired_string that failed
            # logger.debug(f"Repaired string that failed parsing: {repaired_string}")
            return {}


def _repair_json_string(s: str) -> str:
    """
    Applies a series of advanced fixes to a string to make it valid JSON.
    Handles unquoted keys, single quotes, bad escapes, trailing commas, and more.
    """
    # 1. Add quotes to unquoted keys
    # Looks for a word followed by a colon, but not inside an existing string.
    # Example: { key: "value" } -> { "key": "value" }
    s = re.sub(r'([{,]\s*)(\w+)(\s*:)', r'\1"\2"\3', s)

    # 2. Normalize literals (None, True, False)
    # Using word boundaries (\b) to avoid replacing "None" in "NoneSuch"
    s = re.sub(r'\bNone\b', 'null', s)
    s = re.sub(r'\bTrue\b', 'true', s)
    s = re.sub(r'\bFalse\b', 'false', s)

    # 3. Fix trailing commas in objects and arrays
    s = re.sub(r',\s*([}\]])', r'\1', s)

    # 4. Use a state machine to fix bad escapes and convert single quotes
    result = []
    in_string = False
    quote_char = ''
    i = 0
    while i < len(s):
        char = s[i]

        if not in_string:
            if char in "'\"":
                in_string = True
                quote_char = char
                result.append('"')  # Always output double quotes
            else:
                result.append(char)
            i += 1
            continue

        # --- We are inside a string ---
        if char == quote_char:
            in_string = False
            result.append('"')  # Always output double quotes
            i += 1
        elif char == '\\':
            if i + 1 < len(s):
                next_char = s[i + 1]
                # If the character after \ is the quote char, it's an escaped quote
                if next_char == quote_char:
                    result.append('\\' + quote_char)
                # Handle standard JSON escapes
                elif next_char in '"\\/bfnrtu':
                    result.append('\\' + next_char)
                else:  # Invalid escape, so escape the backslash itself
                    result.append('\\\\')
                    result.append(next_char)
                i += 2
            else:  # Dangling backslash
                result.append('\\\\')
                i += 1
        else:
            result.append(char)
            i += 1

    return "".join(result)