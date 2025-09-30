import json

def format_json(data: str) -> str:
    """
    Format a JSON string with indentation.
    Returns pretty-printed JSON or error message.
    """
    try:
        parsed = json.loads(data)
        return json.dumps(parsed, indent=2)
    except Exception as e:
        return f"Invalid JSON: {e}"
