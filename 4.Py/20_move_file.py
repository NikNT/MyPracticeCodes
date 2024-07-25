import os

src = "test.txt"
dst_dir = "test"

try:
    if os.path.isdir(dst_dir):
        dst = os.path.join(dst_dir, os.path.basename(src))  # Construct the full path
        os.replace(src, dst)
    else:
        print(f'Destination directory {dst_dir} does not exist!')
except FileNotFoundError:
    print(f'{src} was not found!')
except Exception as e:
    print(f'An error occurred: {e}')
