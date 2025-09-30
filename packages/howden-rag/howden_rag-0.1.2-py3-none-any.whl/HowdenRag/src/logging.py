import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


def save_chat_history(user_id: str, query: str, response: str, log_dir: str = "logs") -> None:
    """Save a chat interaction to a JSON file."""
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    chat_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "query": query,
        "response": response
    }
    
    file_path = log_path / f"chat_history_{user_id}.json"
    
    # Load existing history or create new list
    if file_path.exists():
        with file_path.open('r', encoding='utf-8') as f:
            history = json.load(f)
    else:
        history = []
    
    history.append(chat_entry)
    
    # Save updated history
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def save_feedback(user_id: str, query: str, response: str, feedback: str, rating: int = None, log_dir: str = "logs") -> None:
    """Save feedback for a chatbot response to a JSON file."""
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    feedback_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "query": query,
        "response": response,
        "feedback": feedback,
        "rating": rating
    }
    
    file_path = log_path / "feedback.json"
    
    if file_path.exists():
        with file_path.open('r', encoding='utf-8') as f:
            feedback_history = json.load(f)
    else:
        feedback_history = []
    
    feedback_history.append(feedback_entry)
    
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(feedback_history, f, ensure_ascii=False, indent=2)
