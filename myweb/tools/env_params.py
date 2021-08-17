from myweb.core.runner import CONFIG_PATH
from myweb.utils.config import *


# 获取环境变量的内容
def get_env_params(file="env_param_setting.json"):
    env_param_path = os.path.join(CONFIG_PATH, file)
    env_param = JsonConfig(env_param_path).get()

    # 获取设置的环境对应的环境变量
    test_env = env_param["test_env"]
    return env_param[test_env]
