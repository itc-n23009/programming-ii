import os

def find_large_files(folder, size_threshold_mb):
    size_threshold = size_threshold_mb * 1024 * 1024

    for foldername, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold:
                    print(f'{file_path} - {file_size / (1024 * 1024):.2f} MB')
            except FileNotFoundError:
                pass
            except PermissionError:
                pass

source_directory = r'C:\path\to\directory'
size_threshold_mb = 100

find_large_files(source_directory, size_threshold_mb)

