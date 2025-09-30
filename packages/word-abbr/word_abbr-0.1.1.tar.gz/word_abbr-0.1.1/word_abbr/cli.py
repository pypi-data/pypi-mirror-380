import argparse
from .abbreviator import Abbreviator

def main() -> None:
    parser = argparse.ArgumentParser(description="Word Abbreviation Tool")
    parser.add_argument("word", help="Word to abbreviate")
    parser.add_argument("-f", "--full", action="store_true", help="Show full info")

    args = parser.parse_args()
    abbrev = Abbreviator()

    if args.full:
        info = abbrev.get_full_info(args.word)
        print(f"Word: {info['word']}")
        print(f"Abbreviation: {info['abbr']}")
        print(f"Source: {info['source']}")
        print(f"Is Abbreviated: {info['is_abbreviated']}")
    else:
        print(abbrev.get(args.word))

if __name__ == "__main__":
    main()