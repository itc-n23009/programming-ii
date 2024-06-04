import os, shutil

def find_and_copy_files(src_folder, dest_folder, extensions):
    src_folder = os.path.abspath(src_folder)
    dest_folder = os.path.abspath(dest_folder)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for foldername, subfolders, filenames in os.walk(src_folder):
        for filename in filenames:
            if filename.lower().endswith(extensions):
                src_file_path = os.path.join(foldername, filename)
                dest_file_path = os.path.join(dest_folder, filename)
                print(f'Copying {src_file_path} to {dest_file_path}')
                shutil.copy2(src_file_path, dest_file_path)
    
    print('Done')

source_directory = r'C:\source_folder'
destination_directory = r'C:\destination_folder'
file_extensions = ('.pdf', '.jpg')

find_and_copy_files(source_directory, destination_directory, file_extensions)

