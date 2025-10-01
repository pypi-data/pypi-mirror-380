import unittest
import os
import stat
from datetime import datetime
import shutil

from git_deployer.configutils import load_deploy_config
from git_deployer.gitdeploy import git_deploy, DeployFlags
from git_deployer.gitutils import is_git_repo, is_bare_git_repo
from git_deployer.pathutils import remove_readonly

class TestGitDeploy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        cls.test_dir = test_dir
        deploy_config_path = os.path.join(test_dir, 'deploy_config.yml')
        print('\ndeploy config path:', deploy_config_path)
        cls.deploy_config_path = deploy_config_path
        test_repo_dir = os.path.join(test_dir, '.test_repo')
        print('test deploy repo path:', test_repo_dir)
        os.makedirs(test_repo_dir, exist_ok=True)
        if not is_bare_git_repo(test_repo_dir, init_empty_dir=True):
            raise Exception('run inside ".test_repo directory: git init --bare')
        test_no_git_path = os.path.join(test_dir, '.test_no_git')
        print('test not git path:', test_no_git_path)
        os.makedirs(test_no_git_path, exist_ok=True)
        source_test_index_html_path = os.path.join(test_dir, 'test_index.html')
        target_test_index_html_path = os.path.join(test_no_git_path, 'index.html')
        if not os.path.exists(target_test_index_html_path):
            shutil.copyfile(source_test_index_html_path, target_test_index_html_path)        
        test_site_path = os.path.join(test_dir, '.test_site')
        print('test site path:', test_site_path)
        cls.test_site_path = test_site_path
        os.makedirs(test_site_path, exist_ok=True)
        target_test_index_html_path = os.path.join(test_site_path, 'index.html')
        if not os.path.exists(target_test_index_html_path):
            shutil.copyfile(source_test_index_html_path, target_test_index_html_path)
        temp_file_path = os.path.join(test_site_path, 'temp.txt')
        print('temp file path:', temp_file_path)
        with open(temp_file_path, 'w') as file:
            file.write(str(datetime.now()))
        # if not is_git_repo(test_site_path, init=True, init_branch='master'):
        #     raise Exception('run inside ".test_site" directory: git init')
        test_wrong_branch_path = os.path.join(test_dir, '.test_wrong_branch')
        print('test wrong branch path:', test_wrong_branch_path)
        os.makedirs(test_wrong_branch_path, exist_ok=True)
        target_test_index_html_path = os.path.join(test_wrong_branch_path, 'index.html')
        if not os.path.exists(target_test_index_html_path):
            shutil.copyfile(source_test_index_html_path, target_test_index_html_path)
        if not is_git_repo(test_wrong_branch_path, init=True, init_branch='wrong'):
            raise Exception('run inside ".test_wrong_branch" directory: git init')

    def test_deploy_config(self):
        print('\n--- test_deploy_config ---')
        try:
            # Change to the specified directory temporarily
            original_cwd = os.getcwd()
            os.chdir(self.test_dir)
            config = load_deploy_config(config_path=self.deploy_config_path, deploy_site=self.test_site_path)
            self.assertIn('deploy', config)
            config_deploy = config['deploy']
            self.assertIn('remote', config_deploy)
            deploy_remote = config_deploy['remote']
            self.assertEqual('test2', deploy_remote['name'])
            self.assertEqual('.test_repo', deploy_remote['url'])
            self.assertEqual('master', config_deploy['branch'])
            self.assertTrue(config_deploy['git_init'])
            self.assertTrue(config_deploy['force_push'])
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)

    def test_deploy_test_no_git(self):
        print('\n--- test_deploy_test_no_git ---')
        try:
            # Change to the specified directory temporarily
            original_cwd = os.getcwd()
            os.chdir(self.test_dir)
            self.assertFalse(git_deploy('.test_no_git', deploy_flags=DeployFlags({'suppress_git_init': True})))
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)

    def test_deploy_test_wrong_branch(self):
        print('\n--- test_deploy_test_wrong_branch ---')
        try:
            # Change to the specified directory temporarily
            original_cwd = os.getcwd()
            os.chdir(self.test_dir)
            self.assertFalse(git_deploy('.test_wrong_branch'))
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)

    def test_deploy_test_site(self):
        print('\n--- test_deploy_test_site ---')
        try:
            # Change to the specified directory temporarily
            original_cwd = os.getcwd()
            os.chdir(self.test_dir)
            self.assertTrue(git_deploy('.test_site'))
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)

    def test_deploy_without_force_push(self):
        print('\n--- test_deploy_without_force_push ---')
        try:
            # Change to the specified directory temporarily
            original_cwd = os.getcwd()
            os.chdir(self.test_dir)
            test_site_git_path = os.path.join('.test_site', '.git')
            if os.path.exists(test_site_git_path):
                print(f'removing "{test_site_git_path}"...')
                shutil.rmtree(test_site_git_path, onerror=remove_readonly)
            self.assertFalse(git_deploy('.test_site', deploy_flags=DeployFlags(suppress_force_push=True)))
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)

    def test_deploy_with_force_push(self):
        print('\n--- test_deploy_with_force_push ---')
        try:
            # Change to the specified directory temporarily
            original_cwd = os.getcwd()
            os.chdir(self.test_dir)
            test_site_git_path = os.path.join('.test_site', '.git')
            if os.path.exists(test_site_git_path):
                print(f'removing "{test_site_git_path}"...')
                shutil.rmtree(test_site_git_path, onerror=remove_readonly)
            self.assertTrue(git_deploy('.test_site'))
        finally:
            # Change back to the original working directory
            os.chdir(original_cwd)

if __name__ == '__main__':
    unittest.main()