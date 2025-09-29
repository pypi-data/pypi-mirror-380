import re
from collections import Counter
from praxshell.config.vault_loader import load_options, load_profiles
from praxshell.cli.utils.display import print_info, print_warning, print_error
from praxshell.cli.utils.color_utils import color
from praxshell.cli.utils.string_matcher import typo_match

OPTIONS_INFO = load_options()
PROFILES = load_profiles()

STOPWORDS = {
    "what", "is", "the", "a", "an", "for", "to", "in", "of", "and", "good",
    "best", "on", "with", "that", "which", "i", "you", "me"
}

def normalize_token(token: str) -> str:
    if token.endswith("ness"):
        return token[:-4]   
    if token.endswith("ing"):
        return token[:-3]   
    if token.endswith("ed"):
        return token[:-2]   
    return token

def tokenize(text: str) -> list[str]:
    words = re.findall(r"\b\w+\b", text.lower())
    return [normalize_token(w) for w in words if w not in STOPWORDS]

def handle_search(query: str):
    query = query.strip()
    if not query:
        print_warning("Usage: search <term or sentence>")
        return

    tokens = tokenize(query)
    if not tokens:
        print_warning("Query too vague. Try using keywords.")
        return

    results = []

    for key, data in OPTIONS_INFO.items():
        score = 0
        key_lower = key.lower()
        desc_lower = data.get("description", "").lower()
        category = data.get("category", "").lower()

        if query.lower() == key_lower:
            score += 5

        for tok in tokens:
            if tok in key_lower:
                score += 3
            if tok in desc_lower:
                score += 2
            if tok in category:
                score += 2

        if score > 0:
            results.append((score, key, data["description"]))

    results.sort(key=lambda x: (-x[0], x[1]))

    if not results:
        candidates = list(OPTIONS_INFO.keys()) + list(PROFILES.keys())
        match = typo_match(query, candidates, cutoff=0.6, n=3)
        print_error(f"No exact results for '{query}'.")
        if match:
            print_info("Did you mean?: " + ", ".join(color(m, "green") for m in match))
        return

    print_info(f"Search results for '{query}':")
    for _, key, desc in results[:5]:
        print(f"- {color(key, 'green')} → {desc}")
