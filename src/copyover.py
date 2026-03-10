import os
import shutil


def copy_over(src_dir, dest_dir):
    # wipe destination directory first
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.makedirs(dest_dir)

    copy_recursive(src_dir, dest_dir)


def copy_recursive(src_dir, dest_dir):
    for f in os.listdir(src_dir):
        src_path = os.path.join(src_dir, f)
        dest_path = os.path.join(dest_dir, f)

        if os.path.isdir(src_path):
            os.makedirs(dest_path)
            copy_recursive(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)