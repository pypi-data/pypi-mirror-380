import os
import subprocess
from .pathutils import is_directory_empty

def is_git_repo(path, init = False, init_branch = ''):
    try:
        # Change to the specified directory temporarily
        original_cwd = os.getcwd()
        os.chdir(path)

        # Run 'git rev-parse --show-toplevel'
        # If it's a Git repo, this command will prints the absolute path to the top-level directory of the Git repository.
        # If it's not a Git repo, it will return a non-zero exit code (e.g., 128)
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'],
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stderr:
            print(result.stderr)
        norm_parh = os.path.normpath(path)
        git_top_dir = os.path.normpath(str(result.stdout).strip())
        if init and (git_top_dir != norm_parh):
            # Run 'git init'
            args = ['git', 'init']
            if init_branch:
                args.append('--initial-branch')
                args.append(init_branch)
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                check=False  # Don't raise an exception for non-zero exit codes
            )
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return True if result.returncode == 0 else False
        return git_top_dir == norm_parh
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)

def is_bare_git_repo(path, init_empty_dir = False):
    try:
        # Change to the specified directory temporarily
        original_cwd = os.getcwd()
        os.chdir(path)

        # Run 'git rev-parse --is-bare-repository'
        # If it's a Git bare repo, this command will return 0 and print 'true' or 'false'
        # (depending on whether it's inside the .git directory or the working tree)
        # If it's not a Git repo, it will return a non-zero exit code (e.g., 128)
        result = subprocess.run(
            ['git', 'rev-parse', '--is-bare-repository'],
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stderr:
            print(result.stderr)
        result_string = str(result.stdout).strip()
        if init_empty_dir and (result_string == 'false'):
            if is_directory_empty(os.getcwd()):                
                # Run 'git init --bare'
                args = ['git', 'init', '--bare']
                result = subprocess.run(
                    args,
                    capture_output=True,
                    text=True,
                    check=False  # Don't raise an exception for non-zero exit codes
                )
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr)
                return True if result.returncode == 0 else False
        return result_string == 'true'
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)

def git_current_branch():
    try:
        # Run 'git branch --show-current'
        # This command directly prints the name of the current branch. It outputs nothing if you are in a detached HEAD state.
        result = subprocess.run(
            ['git', 'branch', '--show-current'],
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stderr:
            print(result.stderr)
        if result.returncode != 0:
            return ''
        current_branch = str(result.stdout).strip()
        return current_branch
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False

def git_config(name, value):
    try:
        # Run 'git config name value'
        # This command set configuration variables that control various aspects of Git's behavior.
        result = subprocess.run(
            ['git', 'config', name, value],
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True if result.returncode == 0 else False
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False

def git_add_all():
    try:
        # Run 'git add .'
        # This command stages all changes in the current directory and its subdirectories.
        result = subprocess.run(
            ['git', 'add', '.'],
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True if result.returncode == 0 else False
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False

def git_commit(message = ''):
    try:
        # Run 'git commit -m message'
        # This command commits all changes in the current directory.
        args = ['git', 'commit']
        if message:
            args.append('-m')
            args.append(message)
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
            return False
        # git commit returns code 1 when nothing to commit
        return True # if result.returncode == 0 else False        
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False

def git_push(remote = '', branch = '', force_push = False):
    try:
        # Run 'git push remote branch'
        # This command commits all changes in the current directory.
        args = ['git', 'push']
        if remote:
            args.append(remote)
        if branch:
            args.append(branch)
        if force_push:
            args.append('--force')
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=False  # Don't raise an exception for non-zero exit codes
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True if result.returncode == 0 else False
    except OSError:
        # Handle cases where 'git' command is not found
        print("Error: Git command not found. Please ensure Git is installed and in your PATH.")
        return False
