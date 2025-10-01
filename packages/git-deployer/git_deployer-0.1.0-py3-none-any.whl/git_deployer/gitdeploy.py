from .configutils import load_deploy_config
from .gitutils import is_git_repo, git_current_branch, \
    git_config, git_add_all, git_commit, git_push
import os
from datetime import datetime

class DeployFlags:
    def __init__(self, suppress_git_init = False, suppress_force_push = False):
        self.suppress_git_init = suppress_git_init
        self.suppress_force_push = suppress_force_push

def git_deploy(deploy_site, config_path = 'deploy_config.yml', deploy_flags: DeployFlags = DeployFlags()):

    print(f'\ndeploying "{deploy_site}"...')

    deploy_site_path = os.path.abspath(deploy_site)

    config = load_deploy_config(config_path=config_path, deploy_site=deploy_site)
    config_deploy = config.get('deploy', {})
    deploy_remote = config_deploy.get('remote', {})
    deploy_remote_name = deploy_remote.get('name', '')
    deploy_remote_url = deploy_remote.get('url', '')
    deploy_branch = config_deploy.get('branch', '')
    deploy_name = config_deploy.get('name', '')
    deploy_email = config_deploy.get('email', '')
    deploy_message = config_deploy.get('message', '%Y-%m-%d %H:%M:%S')
    deploy_message = f'Site updated: {datetime.now().strftime(deploy_message)}'
    deploy_git_init = False if deploy_flags.suppress_git_init else config_deploy.get('git_init', False)
    deploy_force_push = False if deploy_flags.suppress_force_push else config_deploy.get('force_push', False)

    if not is_git_repo(deploy_site_path, init=deploy_git_init, init_branch=deploy_branch):
        print(f'Not a git repo: {deploy_site_path}')
        return False
    
    if os.path.exists(deploy_remote_url):
        deploy_remote_url = os.path.abspath(deploy_remote_url)

    try:
        # Change to the specified directory temporarily
        original_cwd = os.getcwd()
        os.chdir(deploy_site_path)

        if deploy_branch:
            current_branch = git_current_branch()
            if current_branch != deploy_branch:
                print(f'You are not currently on the branch "{deploy_branch}".')
                print(f'Please checkout to the branch "{deploy_branch}" before deploy.')
                return False

        if deploy_name:
            if not git_config('user.name', deploy_name):
                return False
        if deploy_email:
            if not git_config('user.email', deploy_email):
                return False
        if not git_add_all():
            return False
        if not git_commit(message=deploy_message):
            return False
        if deploy_remote_name and deploy_remote_url:
            if not git_config(f'remote.{deploy_remote_name}.url', deploy_remote_url):
                return False
        if not git_push(remote=deploy_remote_name, branch=deploy_branch, force_push=deploy_force_push):
            return False
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)

    return True
