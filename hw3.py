import os
import shutil
import sys

def copy_files(source_dir, dest_dir='dist'):
    try:
        os.makedirs(dest_dir, exist_ok=True)  

        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(root, file)  
                dest_path = os.path.join(dest_dir, os.path.splitext(file)[1].strip('.').lower(), file)  

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)  

                shutil.copy2(source_path, dest_path)  

        print("Копіювання файлів завершено!")
    except Exception as e:
        print(f"Під час копіювання файлів виникла помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    copy_files(source_dir, dest_dir)