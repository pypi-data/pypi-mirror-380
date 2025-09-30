from typing import Dict, List
import os
import shutil
import zipfile39
import rarfile
import py7zr
import tarfile
import re




def save_dict_to_json(data: Dict, file_path: str):
    import json
    with open(file_path, 'w') as json_file:
        # Write the dictionary to the file as JSON
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Dict has been successfully saved to {file_path}")

def write_list_to_txt(uid_list: List, file_path: str, verbose: bool = False):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(uid_list))
    if verbose:
        print(f"List has been successfully saved to {file_path}")
        
def clean_local_cache(paths_list, verbose=False):
    """
    Deletes files or directories specified in paths_list.

    :param paths_list: List of file or directory paths to delete.
    """
    for path in paths_list:
        try:
            if os.path.exists(path):
                if os.path.isfile(path) or os.path.islink(path):
                    os.remove(path)  # Remove file or symlink
                    if verbose:
                        print(f"Deleted file: {path}")
                elif os.path.isdir(path):
                    shutil.rmtree(path)  # Remove directory and its contents
                    if verbose:
                        print(f"Deleted directory: {path}")
            else:
                if verbose:
                    print(f"Path does not exist: {path}")
        except Exception as e:
            if verbose:
                print(f"Error deleting {path}: {e}")


def is_multi_volume_rar(filename):
    # Match: anything + ".part" + digits + ".rar"
    pattern = re.compile(r"\.part\d+\.rar$", re.IGNORECASE)
    return bool(pattern.search(filename))


def is_first_volume_rar(filename):
    """
    Returns True if the filename is a multi-volume RAR and it is the first volume (.part1.rar)
    """
    # Match ".part1.rar" at the end of the filename, case-insensitive
    pattern = re.compile(r"\.part1\.rar$", re.IGNORECASE)
    return bool(pattern.search(filename))       
                
                
def extract_compressed_file(compressed_file_path, extract_dir, delete_compressed_file=True):
    try:
        if compressed_file_path.endswith('.zip'):
            with zipfile39.ZipFile(compressed_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)            
        elif compressed_file_path.endswith('.rar'):
            with rarfile.RarFile(compressed_file_path, 'r') as rar_ref:
                rar_ref.extractall(extract_dir)
        elif compressed_file_path.endswith('.7z'):
            with py7zr.SevenZipFile(compressed_file_path, 'r') as sz_ref:
                sz_ref.extractall(extract_dir)
        elif any(compressed_file_path.endswith(ext) for ext in ['.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2', '.tar.xz']):
            with tarfile.open(compressed_file_path, 'r:*') as tar_ref:
                tar_ref.extractall(extract_dir)
        
        # print(f'成功解压文件: {compressed_file_path} 到 {extract_dir}')
        if delete_compressed_file:
            clean_local_cache([compressed_file_path])
    except Exception as e:
        # should_retry_uncompress = compressed_file_path.endswith('.zip') # retry zip
        # clean_local_cache([compressed_file_path])
        raise Exception(f'error: 解压文件失败, key:{compressed_file_path}, 错误: {str(e)}')


def recursively_extract_compressed_files(root_path, delete_compressed_file=True):
    """
    Recursively extract all compressed files under root_path.
    Handles nested compressed files until no compressed files remain.
    Extract to the same directory as the compressed file.

    Args:
        root_path (str): Directory or file path to start extraction.
        delete_compressed_file (bool): Whether to delete compressed files after extraction.
    """
    # Ensure path is absolute
    root_path = os.path.abspath(root_path)

    def is_compressed_file(file_path):
        exts = ['.zip', '.rar', '.7z', 
                '.tar', '.gz', '.bz2', '.xz', 
                '.tar.gz', '.tar.bz2', '.tar.xz']
        return any(file_path.endswith(ext) for ext in exts)

    # DFS stack for directories
    stack = [root_path]

    while stack:
        current_path = stack.pop()

        if os.path.isfile(current_path) and is_compressed_file(current_path):
            # if the file is a multi-volume rar and it is not the first volume, skip it
            if is_multi_volume_rar(current_path) and not is_first_volume_rar(current_path):
                continue
            # Extract to same directory
            extract_dir = os.path.dirname(current_path)
            try:
                extract_compressed_file(current_path, extract_dir, delete_compressed_file=delete_compressed_file)
            except Exception as e:
                print(f"[WARN] Failed to extract {current_path}: {e}")
                continue
            # After extraction, push directory back to stack to catch newly extracted compressed files
            stack.append(extract_dir)

        elif os.path.isdir(current_path):
            # Add all children to stack
            for child in os.listdir(current_path):
                stack.append(os.path.join(current_path, child))
