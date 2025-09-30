import argparse
from . import AcronymExpander

def main():
    parser = argparse.ArgumentParser(prog="acronym-expander", description="Expand acronyms to full forms")
    parser.add_argument("text", nargs="+", help="Text to expand (wrap in quotes if multiple words)")
    parser.add_argument("-l", "--load", help="Optional JSON file with extra acronym mappings")
    args = parser.parse_args()

    ae = AcronymExpander()
    if args.load:
        ae.load_from_file(args.load)
    text = " ".join(args.text)
    print(ae.expand(text))

if __name__ == "__main__":
    main()
