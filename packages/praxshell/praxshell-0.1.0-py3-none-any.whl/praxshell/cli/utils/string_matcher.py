import difflib
from typing import List, Optional

def typo_match(user_input: str, candidates: List[str], cutoff: float = 0.6, n: int = 3) -> Optional[List[str]]:
    if not user_input or not candidates:
        return None
    return difflib.get_close_matches(user_input, candidates, n=n, cutoff=cutoff)
