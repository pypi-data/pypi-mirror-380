"""acronym_expander — expand acronyms & abbreviations to full forms."""
__version__ = "0.1.1"

import re
from typing import Dict, Optional

# small default dictionary — extend as you like
DEFAULT_MAP: Dict[str, str] = {
    "WHO": "World Health Organization",
    "UN": "United Nations",
    "NYC": "New York City",
    "AI": "Artificial Intelligence",
    "NASA": "National Aeronautics and Space Administration",
    "HTTP": "HyperText Transfer Protocol",
    "HTTPS": "HyperText Transfer Protocol Secure",
    "HTML": "HyperText Markup Language",
    "CSS": "Cascading Style Sheets",
    "JSON": "JavaScript Object Notation",
    "SQL": "Structured Query Language",
    "USA": "United States of America",
    "EU": "European Union",
    "UK": "United Kingdom",
    "UAE": "United Arab Emirates",
    "GDP": "Gross Domestic Product",
    "ML": "Machine Learning",
    "IOT": "Internet of Things",
    "IoT": "Internet of Things",
    "HTTP2": "HyperText Transfer Protocol version 2",
    "API": "Application Programming Interface",
    "RAM": "Random Access Memory",
    "CPU": "Central Processing Unit",
    "GPU": "Graphics Processing Unit",
}

class AcronymExpander:
    def __init__(self, custom_map: Optional[Dict[str, str]] = None, case_sensitive: bool = False):
        self.case_sensitive = case_sensitive
        self.map = {**DEFAULT_MAP}
        if custom_map:
            self.map.update(custom_map)
        self._build_pattern()

    def _build_pattern(self):
        # order by length so longer keys match first
        keys = sorted(self.map.keys(), key=lambda k: -len(k))
        if not keys:
            self.pattern = re.compile(r'(?!x)x')
            return
        pattern = r'\b(' + '|'.join(re.escape(k) for k in keys) + r')\b'
        flags = 0 if self.case_sensitive else re.IGNORECASE
        self.pattern = re.compile(pattern, flags)

    def expand(self, text: str) -> str:
        def repl(m):
            token = m.group(0)
            if self.case_sensitive:
                full = self.map.get(token)
                return f"{token} ({full})" if full else token
            for k, v in self.map.items():
                if k.lower() == token.lower():
                    return f"{token} ({v})"
            return token
        return self.pattern.sub(repl, text)

    def add(self, acronym: str, full_form: str):
        self.map[acronym] = full_form
        self._build_pattern()

    def load_from_file(self, path: str):
        import json
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError("JSON must be an object mapping acronyms to full forms")
        self.map.update(data)
        self._build_pattern()
