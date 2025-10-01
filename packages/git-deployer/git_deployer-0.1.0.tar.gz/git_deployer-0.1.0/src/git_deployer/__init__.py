from .gitdeploy import git_deploy
import sys

def main():
    """Entry point for the application script"""
    if len(sys.argv) == 2:
        git_deploy(sys.argv[1])
    else:
        print("usage: deploy <path>")

