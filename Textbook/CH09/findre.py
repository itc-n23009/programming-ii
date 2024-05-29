import os
import re

def search_in_files(directory, pattern):
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        print(f'Searching in {file_path}:')

        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if re.search(pattern, line):
                    print(f'  Line {line_num}: {line.strip()}')

def main():
    directory = input('Enter directory to search in: ')

    pattern = input('Enter regular expression pattern to search for: ')

    search_in_files(directory, pattern)

if __name__ == "__main__":
    main()

