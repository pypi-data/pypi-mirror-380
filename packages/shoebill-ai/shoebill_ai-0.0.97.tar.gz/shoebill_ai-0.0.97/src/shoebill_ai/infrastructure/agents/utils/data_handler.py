import json
import re
import logging

# It's good practice to have a logger instance
logger = logging.getLogger(__name__)


def parse_json_data(json_string: str) -> dict:
    """
    Parses a string to extract and load JSON data, with robust cleaning and repair.

    This function attempts to handle various common malformations:
    - Extracts JSON from Markdown code blocks.
    - Strips leading/trailing non-JSON content.
    - On failure, attempts a series of repairs (e.g., fixing bad escapes,
      removing trailing commas) before a final parsing attempt.
    """
    if not json_string or not json_string.strip():
        logger.warning("Empty JSON string provided.")
        return {}

    # 1. Extract content from Markdown blocks first
    match = re.search(r'```(?:json)?\s*({.*?})\s*```', json_string, re.DOTALL)
    if match:
        json_string = match.group(1)
    else:
        # 2. If no markdown, greedily find the main JSON object
        start = json_string.find('{')
        end = json_string.rfind('}')
        if start != -1 and end > start:
            json_string = json_string[start:end + 1]
        else:
            logger.warning("Could not find a valid JSON object structure '{...}' in the string.")
            return {}

    # 3. First attempt to parse the cleaned string
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logger.warning(f"Primary JSON parse failed: {e}. Attempting to repair...")

        # 4. If it fails, run the repair function and try again
        repaired_string = _repair_json_string(json_string)
        try:
            data = json.loads(repaired_string)
            logger.info("JSON parsed successfully after repair.")
            return data
        except json.JSONDecodeError as e2:
            logger.error(f"Failed to parse JSON even after repair: {e2}")
            # For debugging, you might want to log the repaired_string
            # logger.debug(f"Repaired string was: {repaired_string}")
            return {}


def _repair_json_string(s: str) -> str:
    """
    Applies a series of fixes to a string to make it valid JSON.
    """
    # 1. Fix trailing commas in objects and arrays
    s = re.sub(r',\s*([}\]])', r'\1', s)

    # 2. Use a state machine to fix bad escapes and control characters
    # This is an enhanced version of your original function
    result = []
    in_string = False
    i = 0
    while i < len(s):
        char = s[i]

        if not in_string:
            if char == '"':
                in_string = True
            result.append(char)
            i += 1
            continue

        # --- We are inside a string ---
        if char == '\\':
            # Check the next character to see if it's a valid escape
            if i + 1 < len(s):
                next_char = s[i + 1]
                if next_char in '"\\/bfnrtu':
                    # It's a valid escape sequence, keep both
                    result.append(char)
                    result.append(next_char)
                    i += 2
                else:
                    # It's an invalid escape, like \'.
                    # We escape the backslash itself.
                    result.append('\\\\')  # Append an escaped backslash
                    result.append(next_char)
                    i += 2
            else:
                # Dangling backslash at the end of the string
                result.append('\\\\')  # Escape it
                i += 1
        elif char == '"':
            in_string = False
            result.append(char)
            i += 1
        elif ord(char) < 0x20:
            # Escape unescaped control characters
            escape_map = {'\n': '\\n', '\r': '\\r', '\t': '\\t', '\b': '\\b', '\f': '\\f'}
            result.append(escape_map.get(char, f'\\u{ord(char):04x}'))
            i += 1
        else:
            result.append(char)
            i += 1

    return "".join(result)