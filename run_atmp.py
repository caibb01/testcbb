# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import sys
import re
import time
from myweb.core.runner import Runner, ThreadRunner, CONFIG_PATH
from myweb.utils.config import JsonConfig
from myweb.tools.support_atmp_run import atmp_post

if __name__ == '__main__':
    # 获取初始配置运行参数配置
    main_file = "demo.main_atmp.json"
    env_file = "env_param_setting.json"
    env_param_path = os.path.join(CONFIG_PATH, env_file)
    env_param = JsonConfig(env_param_path).get()

    # 开启上传结果到atmp系统时，更新配置中的批次号
    main_path = os.path.join(CONFIG_PATH, main_file)
    main_content = JsonConfig(main_path).get()
    atmp_file = main_content["atmp_file"]
    atmp_config_path = os.path.join(CONFIG_PATH, atmp_file)
    json_file = JsonConfig(atmp_config_path)
    file_content = json_file.get()

    # 获取多线程开关
    main_path = os.path.join(CONFIG_PATH, main_file)
    thread_open = JsonConfig(main_path).get()["thread"]
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
        file_content["parameter"]["server_id"] = file_content["server_id"][env_param["test_env"]]
        json_file.set(file_content)
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
    if "schema_id" in parameters_dict.keys():
        file_content["schema_id"] = parameters_dict["schema_id"]
        json_file.set(file_content)
    if "tester_id" in parameters_dict.keys():
        file_content["tester_id"] = parameters_dict["tester_id"]
        json_file.set(file_content)
    JsonConfig(env_param_path).set(env_param)

    # 在atmp平台创建任务
    generate_task_schema_data = {"schema_id": file_content["schema_id"], "tester": file_content["tester_id"]}
    result = atmp_post(file_content, "/edi/generate_task_schema", generate_task_schema_data)
    task_id = result["data"]["task_id"]
    file_content["parameter"]["task_id"] = task_id
    json_file.set(file_content)

    # 在atmp平台清理执行结果
    delay_sec = 3
    delete_task_log_data = {"node_id": file_content["parameter"]["node_id"], "task_id": file_content["parameter"]["task_id"]}
    result = atmp_post(file_content, "/edi/delete_task_logs", delete_task_log_data)
    time.sleep(delay_sec)

    # 初始化执行信息
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y%m%d%H%M%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    file_content["parameter"]["batch_no"] = time_stamp
    file_content["parameter"]["tester"] = file_content["tester_id"]
    json_file.set(file_content)

    # 开始运行自动化用例
    if thread_open:
        tread_run = ThreadRunner(max_workers=max_workers, config_name=main_file)
        tread_run.thread_run(case_path=case_path, pattern=pattern)
    else:
        main_run = Runner(config_name=main_file)
        main_run.run(case_path=case_path, pattern=pattern)

    # 在atmp平台更新测试任务
    update_statics_data = {"task_id": task_id}
    result = atmp_post(file_content, "/edi/update_task_result", update_statics_data)

    # 在atmp平台发送企业微信消息
    data = {"task_id": task_id, "send_type": "weixin"}
    result = atmp_post(file_content, "/edi/send_report", data)

    # 在atmp平台发送电子邮件
    data = {"task_id": task_id, "send_type": "email"}
    result = atmp_post(file_content, "/edi/send_report", data)

    # 执行完用例后将执行信息置为空
    file_content["parameter"]["log_id"] = ""
    file_content["parameter"]["task_id"] = ""
    file_content["parameter"]["batch_no"] = ""
    file_content["parameter"]["test_code"] = ""
    file_content["parameter"]["tester"] = ""
    file_content["parameter"]["fire_time"] = ""
    file_content["parameter"]["log_time"] = 0.000
    file_content["parameter"]["log_result"] = ""
    file_content["parameter"]["memo"] = ""
    json_file.set(file_content)
