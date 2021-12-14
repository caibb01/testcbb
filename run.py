import os
import sys
import re

from myweb.core.runner import Runner, CONFIG_PATH, ThreadRunner
from myweb.utils.config import JsonConfig

if __name__ == '__main__':

    config_path = "demo.json"
    print(CONFIG_PATH)
    # 获取初始配置运行参数配置
    env_param_path = os.path.join(CONFIG_PATH, "env_param_setting.json")
    env_param = JsonConfig(env_param_path).get()
    # 获取多线程开关
    conf_path_ = os.path.join(CONFIG_PATH, "demo.json")
    thread_open = JsonConfig(conf_path_).get()["thread"]
    pattern = ""
    max_workers = 2
    case_path = ""
    parameters_dict = {}
    parameters = sys.argv
    # 解析入参转换成字典
    for i in range(1, len(parameters)):
        # 判断输入参数格式是否正确
        if re.match(r"^\w+[:|：][\w|-]*\*?[\w|-]*.?[\w|-]*$", parameters[i]) is None:
            raise Exception("命令执行所带参数格式应为key:value，且key只支持英文数字和_,value只支持英文数字和-_*.")
        key, value = parameters[i].split(":")
        parameters_dict[key] = value

    # 替换对应的参数
    if "env" in parameters_dict.keys():
        env_param["test_env"] = parameters_dict["env"]
    if "trace_branch" in parameters_dict.keys():
        env_param["test"]["trace_branch"] = parameters_dict["trace_branch"]
    if "pattern" in parameters_dict.keys():
        pattern = parameters_dict["pattern"]
    if "thread" in parameters_dict.keys():
        if parameters_dict["thread"].lower() == "true":
            thread_open = True
        elif parameters_dict["thread"].lower() == "false":
            thread_open = False
        else:
            raise ValueError("thread传参错误，只支持true或false且不区分大小写~")
    if "num" in parameters_dict.keys():
        max_workers = int(parameters_dict["num"])
    if "path" in parameters_dict.keys():
        case_path = parameters_dict["path"]
    JsonConfig(env_param_path).set(env_param)

    # 开始运行自动化用例
    if thread_open:
        tread_run = ThreadRunner(max_workers=max_workers, config_name=config_path)
        tread_run.thread_run(case_path=case_path, pattern=pattern)
    else:
        main_run = Runner(config_name=config_path)
        main_run.run(case_path=case_path, pattern=pattern)



