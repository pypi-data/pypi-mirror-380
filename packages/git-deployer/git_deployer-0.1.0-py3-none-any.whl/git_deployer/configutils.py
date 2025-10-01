import yaml
import os
import collections.abc

def update_dict(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d

def load_deploy_config(config_path = 'deploy_config.yml', deploy_site = '') -> dict:
    if config_path and os.path.exists(config_path):
        with open(config_path) as fp:
            config = yaml.safe_load(fp)
    else:
        config = {}
    if deploy_site:
        deploy_site_path = os.path.abspath(deploy_site)
        config_deploy = config.get('deploy', {})
        sites = config_deploy.get('sites', [])    
        for site in sites:
            site_path = site.get('path', '')
            if site_path:
                site_path = os.path.abspath(site_path)
                print(f'site_path: {site_path}')
                if site_path == deploy_site_path:
                    if 'deploy' in site:
                        update_dict(config, { 'deploy': site['deploy'] })
    return config

