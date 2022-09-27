#!/usr/bin/python3
"""Load, add, save"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    new_items = sys.argv[1:]
    items.extend(new_items)
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
