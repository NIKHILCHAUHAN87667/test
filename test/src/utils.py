import os
import sys
from datetime import datetime
from typing import List

def format_list(items: List[str]) -> str:
    return ", ".join(items)

def get_timestamp():
    return datetime.now().isoformat()