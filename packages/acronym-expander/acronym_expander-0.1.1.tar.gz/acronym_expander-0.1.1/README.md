# acronym-expander

A lightweight Python utility to expand acronyms into their full forms.

acronym-expander helps developers, data scientists, and technical writers quickly convert commonly used acronyms into human-readable full forms, improving code clarity, documentation, and text processing workflows.

## Features:
1.Expand common acronyms with a single function call.
2.Lightweight and dependency-free.
3.Easy to integrate into scripts, notebooks, or larger projects.
4.Useful for documentation, text preprocessing, and educational purposes.

## Install
```bash
pip install acronym-expander

## Usage
```python
from acronym_expander import DEFAULT_MAP

sentence = "NASA and AI are collaborating with WHO in NYC."

expanded_sentence = " ".join(
    [DEFAULT_MAP.get(word.upper().strip(".,!?;:"), word) for word in sentence.split()]
)

print("Original:", sentence)
print("Expanded:", expanded_sentence)

## Expected Output:
Original: NASA and AI are collaborating with WHO in NYC.
Expanded: National Aeronautics and Space Administration and Artificial Intelligence are collaborating with World Health Organization in New York City.

