import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    print(f'Creating {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    new_base = os.path.basename(folder) + '_'
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backup_zip.write(foldername)
        for filename in filenames:
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done')

backup_to_zip(r'C:\delicious')

