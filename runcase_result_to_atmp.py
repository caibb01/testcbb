# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import sys

import requests

from myweb.core.runner import Runner, CONFIG_PATH
import time

from myweb.utils.HttpRequest import HttpRequest
from myweb.utils.config import JsonConfig

if __name__ == '__main__':
    # 开启上传结果到atmp系统时，更新配置中的批次号
    ATMP_FILE = "run_atmp_param.json"
    atmp_config_path = os.path.join(CONFIG_PATH, ATMP_FILE)

    json_file = JsonConfig(atmp_config_path)
    file_content = json_file.get()

    # 获取执行环境

    # 执行环境路径
    env_file = "env_param_setting.json"

    num = len(sys.argv)
    if num == 2:
        env = sys.argv[1]
        env_param_path = os.path.join(CONFIG_PATH, env_file)
        env_param = JsonConfig(env_param_path).get()
        env_param["test_env"] = env
        JsonConfig(env_param_path).set(env_param)

    # 清理本地缓存
    delay_sec = 3
    delete_task_log_data = {"node_id": file_content["parameter"]["node_id"], "server_id": file_content["parameter"]["server_id"]}
    api_request = HttpRequest()
    res = api_request.sendPost(file_content["atmp_url"] + "/edi/delete_task_logs",data=delete_task_log_data)
    print(res)
    # requests.post(file_content["atmp_url"] + "/edi/delete_task_logs",data=delete_task_log_data)
    time.sleep(delay_sec)

    # 判断是否开启上传结果到ATMP系统
    if file_content["is_report_result_to_atmp"] is True:
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y%m%d%H%M%S", local_time)
        data_secs = (ct - int(ct)) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        file_content["parameter"]["batch_no"] = time_stamp
        json_file.set(file_content)

    config_path = "demo.json"
    r = Runner(config_name=config_path)
    r.run()

    # 在atmp平台创建任务
    generate_task_schema_data={"schema_id": file_content["schema_id"], "tester": file_content["tester_id"]}
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    result = requests.post(url=file_content["atmp_url"] + "/edi/generate_task_schema",data=generate_task_schema_data,headers=headers)
    task_id = json.loads(result.content)["data"]

    # 将log提交到atmp
    submit_data = {"node_id": file_content["parameter"]["node_id"] , "task_id": task_id}
    print(submit_data)
    result = requests.post(url=file_content["atmp_url"] + "/edi/submit_task_log",data=submit_data,headers=headers)
    print(result.content.decode('utf8'))

    update_statics_data = {"task_id": task_id}
    result = requests.post(url=file_content["atmp_url"] + "/edi/update_statics",data=update_statics_data,headers=headers)
    print(result.content.decode('utf8'))

    # 发送企业微信消息
    # data={"task_id": task_id, "send_type": "weixin"}
    # result = requests.post(url=file_content["atmp_url"] + "/edi/send_report",data=data,headers=headers)
    # print(result.content.decode('utf8'))


    # 执行完用例后将批次号置为空
    if file_content["is_report_result_to_atmp"] is True:
        file_content["parameter"]["batch_no"] = ""
        json_file.set(file_content)