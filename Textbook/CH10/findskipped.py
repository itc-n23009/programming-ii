import os, re

def find_and_fix_gaps(prefix, directory, start=None, end=None):
    pattern = re.compile(rf'^{re.escape(prefix)}(\d{{3}})\.txt$')

    files = [filename for filename in os.listdir(directory) if pattern.match(filename)]
    numbers = sorted(int(pattern.match(filename).group(1)) for filename in files)

    expected_numbers = range(numbers[0] if start is None else start, numbers[-1]+1 if end is None else end+1)
    missing_numbers = [num for num in expected_numbers if num not in numbers]

    for num in missing_numbers:
        missing_filename = f'{prefix}{num:03}.txt'
        print(f'Missing file: {missing_filename}')
        open(os.path.join(directory, missing_filename), 'w').close()

    if start is not None and end is not None:
        for num in range(start, end+1):
            new_filename = f'{prefix}{num:03}.txt'
            if new_filename not in files:
                print(f'Inserting new file: {new_filename}')
                open(os.path.join(directory, new_filename), 'w').close()

prefix = 'spam'
directory = '/path/to/directory'
start = 50
end = 70
find_and_fix_gaps(prefix, directory, start, end)


