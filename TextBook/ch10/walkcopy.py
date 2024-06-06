import os, shutil

def copy(src_dir, dest_dir, extensions):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(tuple(extensions)):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied: {src_file_path} to {dest_file_path}")

