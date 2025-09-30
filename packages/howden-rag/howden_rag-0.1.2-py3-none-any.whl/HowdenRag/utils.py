from pathlib import Path
import base64


def make_safe_id(path: Path) -> str:
    """Encode a file path into a URL-safe ID."""
    return base64.urlsafe_b64encode(str(path.resolve()).encode()).decode()

def decode_safe_id(safe_id: str) -> str:
    """Decode a safe ID back to the original file path string."""
    return base64.urlsafe_b64decode(safe_id.encode()).decode()
