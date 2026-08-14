def normalize(text: str) -> str:
    """Lowercase and strip whitespace."""
    return " ".join(text.strip().split()).lower()

