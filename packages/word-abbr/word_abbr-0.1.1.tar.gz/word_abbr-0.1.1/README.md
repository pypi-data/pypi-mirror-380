# word-abbr

A simple Python library for querying common abbreviations of English words.

## Funtions

- Query abbreviations of words (e.g., application → app)
- Support command-line queries
- Support custom word abbreviations
- Built-in common word abbreviation mappings
- Rule-based general abbreviation algorithm

## Install
```bash
pip install word-abbr
```

## Use

### CMD-LINE
```
word-abbr application
```
output: app

### IN CODE
```python
from word_abbr import get_abbr

print(get_abbr("database"))  # db
```

## eneral abbreviation algorithm
### rule 1
Keep the first letter
### rule 2
Starting from the second letter, do not keep vowels
### rule 3
For consonants among l, m, n, and r: if the preceding letter is a vowel and the following letter is a consonant, do not keep them
### rule 4
Repeat the process until the abbreviation length exceeds 4 (can also be customized), then return the result
### rule 5
To be continued