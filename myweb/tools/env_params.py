from myweb.core.runner import CONFIG_PATH
from myweb.utils.config import *





def get_env(file="env_param_setting.json"):
    '''获取环境值'''
    env_param_path = os.path.join(CONFIG_PATH, file)
    env_param = JsonConfig(env_param_path).get()

    # 获取设置的环境对应的环境变量
    env = env_param["env"]
    return env


def get_env_params(file="env_param_setting.json"):
    '''获取不同环境的内容'''
    env_param_path = os.path.join(CONFIG_PATH, file)
    env_param = JsonConfig(env_param_path).get()

    # 获取设置的环境对应的环境变量
    env = env_param["env"]
    return env_param[env]


