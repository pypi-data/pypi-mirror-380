"""
CLI for em
"""

from __future__ import annotations

import argparse
import os

from em import __version__

CUSTOM_EMOJI_PATH = os.path.join(os.path.expanduser("~/.emojis.json"))

EmojiDict = dict[str, list[str]]


def try_copy_to_clipboard(text: str) -> bool:
    try:
        import pyperclip  # type: ignore[import]
    except ModuleNotFoundError:
        pyperclip = None
        try:
            import xerox  # type: ignore[import]
        except ModuleNotFoundError:
            return False
    copier = pyperclip if pyperclip else xerox
    copier_error = pyperclip.PyperclipException if pyperclip else xerox.ToolNotFound
    try:
        copier.copy(text)
    except copier_error:
        return False
    return True


def parse_emojis(filename: str | None = None) -> EmojiDict:
    import json

    if filename is None:
        from importlib.resources import files

        emoji_traversable = files("em").joinpath("emojis.json")
        return json.loads(emoji_traversable.read_text("utf-8"))

    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def translate(lookup: EmojiDict, code: str) -> str | None:
    if code[0] == ":" and code[-1] == ":":
        code = code[1:-1]

    for emoji, keywords in lookup.items():
        if code == keywords[0]:
            return emoji
    return None


def do_find(lookup: EmojiDict, terms: tuple[str, ...]) -> list[tuple[str, str]]:
    """Match terms against keywords."""
    assert terms, "at least one search term required"
    return [
        (keywords[0], emoji)
        for emoji, keywords in lookup.items()
        if all(any(term in kw for kw in keywords) for term in terms)
    ]


def clean_name(name: str) -> str:
    """Clean emoji name replacing specials chars by underscore"""
    return name.replace("-", "_").replace(" ", "_").lower()


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.color = True  # type: ignore[attr-defined]
    parser.add_argument("name", nargs="*", help="Text to convert to emoji")
    parser.add_argument("-s", "--search", action="store_true", help="Search for emoji")
    parser.add_argument("-r", "--random", action="store_true", help="Get random emoji")
    parser.add_argument(
        "--no-copy", action="store_true", help="Does not copy emoji to clipboard"
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args(arg_list)
    return args


def main(arg_list: list[str] | None = None) -> str | int:
    args = parse_args(arg_list)
    no_copy = args.no_copy

    if not args.name and not args.random:
        return "Error: the 'name' argument is required"

    # Grab the lookup dictionary.
    lookup = parse_emojis()

    if os.path.isfile(CUSTOM_EMOJI_PATH):
        lookup.update(parse_emojis(CUSTOM_EMOJI_PATH))

    if args.random and not args.search:
        import random

        emoji, keywords = random.choice(list(lookup.items()))
        name = keywords[0]
        if not no_copy:
            copied = try_copy_to_clipboard(emoji)
        else:
            copied = False
        print(f"Copied! {emoji}  {name}" if copied else f"{emoji}  {name}")
        return 0

    names = tuple(map(clean_name, args.name))

    # Search mode.
    if args.search:
        # Lookup the search term.
        found = do_find(lookup, names)

        if args.random and len(found) >= 2:
            import random

            found = [random.choice(found)]

        # print them to the screen.
        for name, emoji in found:
            # Some registered emoji have no value.
            try:
                # Copy the results (and say so!) to the clipboard.
                if not no_copy and len(found) == 1:
                    copied = try_copy_to_clipboard(emoji)
                else:
                    copied = False
                print(f"Copied! {emoji}  {name}" if copied else f"{emoji}  {name}")

            # Sometimes, an emoji will have no value.
            except TypeError:
                pass

        if len(found):
            return 0
        else:
            return 1

    # Process the results.
    unfiltered_results = tuple(translate(lookup, name) for name in names)
    results = tuple(r for r in unfiltered_results if r is not None)

    if len(results) < len(unfiltered_results):
        no_copy = True
        missing = True  # Marker for if the given emoji isn't found.
    else:
        missing = False

    # Prepare the result strings.
    print_results = " ".join(results)
    copy_results = "".join(results)

    # Copy the results (and say so!) to the clipboard.
    if not no_copy and not missing:
        copied = try_copy_to_clipboard(copy_results)
    else:
        copied = False

    if print_results:
        print(f"Copied! {print_results}" if copied else print_results)

    return int(missing)


if __name__ == "__main__":
    main()
