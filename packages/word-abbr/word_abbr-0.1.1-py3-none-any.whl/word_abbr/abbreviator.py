from typing import Dict, Set

class Abbreviator:
    def __init__(self) -> None:
        # level1: internal abbreviations
        self.internal_abbreviations: Dict[str, str] = {
            "doctor": "Dr.",
            "professor": "Prof."
        }

        # level 2：data file
        from .data import DataManager
        self.data_manager = DataManager()
        self.data_abbreviations: Dict[str, str] = self.data_manager.load_abbreviations()

        # level 3：general abbreviation algorithm

    def get(self, word: str) -> str:
        word_key: str = word.strip().lower()

        # 🔢 Level 1
        if word_key in self.internal_abbreviations:
            return self.internal_abbreviations[word_key]

        # 🔢 Level 2
        if word_key in self.data_abbreviations:
            return self.data_abbreviations[word_key]

        # 🔢 Level 3:
        return self._generate_generic_abbreviation(word_key)


    def _generate_generic_abbreviation(self, word: str, length: int = 4) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g',
                      'h', 'j', 'k', 'l', 'm',
                      'n', 'p', 'q', 'r', 's',
                      't', 'v', 'w', 'x','y',
                      'z']

        if len(word) <= length:
            return word
        else:
            result = []
            for index, char in enumerate(word):
                if len(result) == length:
                    return ''.join(result)
                else:
                    if index == 0:
                        result.append(char)
                    elif char in vowels:
                        continue
                    elif char in consonants:
                        if (char in ['l', 'r', 'm', 'n']
                                and word[index - 1] in vowels
                                and index < len(word) - 1
                                and word[index + 1] in consonants
                                and index > 1):
                            continue
                        else:
                            result.append(char)
            return ''.join(result)

    def get_full_info(self, word: str) -> dict[str, str | bool]:
        word_key = word.strip().lower()
        abbr: str

        if word_key in self.internal_abbreviations:
            abbr = self.internal_abbreviations[word_key]
            source = "internal"
        elif word_key in self.data_abbreviations:
            abbr = self.data_abbreviations[word_key]
            source = "data_file"
        else:
            abbr = self._generate_generic_abbreviation(word_key)
            source = "generic_algorithm"

        return {
            "word": word_key,
            "abbr": abbr,
            "source": source,
            "is_abbreviated": abbr != word_key
        }