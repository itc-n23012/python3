import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    number = 1

    while os.path.exists(f'{os.path.basename(folder)}_{number}.zip'):
        number += 1

    zip_filename = f'{os.path.basename(folder)}_{number}.zip'
    print(f'Creating {zip_filename}')

    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        for foldername, _, filenames in os.walk(folder):
            backup_zip.write(foldername)
            for filename in filenames:
                if not (filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip')):
                    backup_zip.write(os.path.join(foldername, filename))
    print('Done')

backup_to_zip(input())

