# -*- coding: utf-8 -*-
import sys
import os
from myweb.core.runner import Runner,CONFIG_PATH
from myweb.utils.config import JsonConfig

if __name__ == '__main__':
    config_path = "aicard.json"

    # # 执行环境路径
    # env_file = ["env_param_setting.json"]
    # num = len(sys.argv)
    # if num >= 2:
    #     env = sys.argv[1]
    #     for file in env_file:
    #         env_param_path = os.path.join(CONFIG_PATH, file)
    #         env_param = JsonConfig(env_param_path).get()
    #         env_param["test_env"] = env
    #         JsonConfig(env_param_path).set(env_param)

    r = Runner(config_name=config_path)
    r.run()
