#!/usr/bin/python3
"""Load, add, save"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    filename = "add_item.json"
    with open(filename, "r+", encoding="utf-8") as file:
        if len(file.read()):
            items = load_from_json_file(filename)
        else:
            items = []
    new_items = sys.argv[1:]
    items.extend(new_items)
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
