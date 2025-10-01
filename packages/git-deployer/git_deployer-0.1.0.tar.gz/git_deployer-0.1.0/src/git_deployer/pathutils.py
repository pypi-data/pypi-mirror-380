import os, stat

def is_directory_empty(path):
    """
    Checks if a directory is empty using os.scandir().
    Returns True if the directory is empty, False otherwise.
    """
    if not os.path.isdir(path):
        raise NotADirectoryError(f"'{path}' is not a valid directory.")
    with os.scandir(path) as it:
        return not any(it)
    
def remove_readonly(func, path, exc_info):
    """
    Clear the readonly bit and reattempt the removal
    usage: shutil.rmtree(directory, onerror=remove_readonly)
    """
    # ERROR_ACCESS_DENIED = 5
    if func not in (os.unlink, os.rmdir) or exc_info[1].winerror != 5:
        raise exc_info[1]
    print(f'reset readonly for "{path}"')
    os.chmod(path, stat.S_IWRITE)
    func(path)