#!/usr/bin/python3
"""Log parsing"""
import sys


def main():
    """Main function"""
    try:
        with sys.stdin as stdin:
            statuses = ["200", "301", "400", "401", "403", "404", "405", "500"]
            counter = {status: 0 for status in statuses}
            count = 0
            total_size = 0
            for line in stdin:
                print(line)
                count += 1
                extract = extract_code_and_size(line)
                code = extract["code"]
                size = extract["size"]
                total_size += int(size)
                counter[code] += 1
                if count % 10 == 0:
                    print_summary(counter, total_size, statuses)
    except KeyboardInterrupt:
        print_summary(counter, total_size, statuses)


def print_summary(counter, total, status_list):
    """Print summary so far"""
    print("File size: {}".format(total))
    for status in status_list:
        if counter[status]:
            print("{}: {}".format(status, counter[status]))


def extract_code_and_size(line):
    """Extract status code and file size from line"""
    [_, second_part] = line.split(" - ")
    [_, code_and_size] = second_part.split('" ')
    [code, size] = code_and_size.split(" ")
    return {"code": code, "size": size}


if __name__ == "__main__":
    main()
