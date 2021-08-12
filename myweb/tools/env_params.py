from myweb.core.runner import CONFIG_PATH
from myweb.utils.config import *

# 获取环境变量的内容
env_param_path = os.path.join(CONFIG_PATH, 'env_param_setting.json')
env_param = JsonConfig(env_param_path).get()

# 获取设置的环境对应的环境变量
test_env = env_param["test_env"]
test_param = env_param[test_env]
