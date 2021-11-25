# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import sys
import time
from myweb.core.runner import Runner, CONFIG_PATH
from myweb.utils.config import JsonConfig
from myweb.tools.support_atmp_run import atmp_post

if __name__ == '__main__':
    # 开启上传结果到atmp系统时，更新配置中的批次号
    ATMP_FILE = "run_atmp_param.json"
    atmp_config_path = os.path.join(CONFIG_PATH, ATMP_FILE)

    json_file = JsonConfig(atmp_config_path)
    file_content = json_file.get()

    # 获取执行环境

    # 执行环境路径
    env_file = ["env_param_setting.json"]

    num = len(sys.argv)
    if num >= 2:
        env = sys.argv[1]
        for file in env_file:
            env_param_path = os.path.join(CONFIG_PATH, file)
            env_param = JsonConfig(env_param_path).get()
            env_param["test_env"] = env
            JsonConfig(env_param_path).set(env_param)
        file_content["parameter"]["server_id"] = file_content["server_id"][env]
        json_file.set(file_content)
    if num >= 3:
        schema = sys.argv[2]
        file_content["schema_id"] = schema
        json_file.set(file_content)
    if num >= 4:
        tester = sys.argv[3]
        file_content["tester_id"] = tester
        json_file.set(file_content)

    # 在atmp平台创建任务
    generate_task_schema_data = {"schema_id": file_content["schema_id"], "tester": file_content["tester_id"]}
    result = atmp_post(file_content, "/edi/generate_task_schema", generate_task_schema_data)
    task_id = result["data"]
    file_content["parameter"]["task_id"] = task_id
    json_file.set(file_content)

    # 在atmp平台清理执行结果
    delay_sec = 3
    delete_task_log_data = {"node_id": file_content["parameter"]["node_id"], "task_id": file_content["parameter"]["task_id"]}
    result = atmp_post(file_content, "/edi/delete_task_logs", delete_task_log_data)
    time.sleep(delay_sec)

    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y%m%d%H%M%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    file_content["parameter"]["batch_no"] = time_stamp
    json_file.set(file_content)

    config_path = "demo_atmp.json"
    r = Runner(config_name=config_path)
    r.run()

    # 在atmp平台更新测试任务
    update_statics_data = {"task_id": task_id}
    result = atmp_post(file_content, "/edi/update_task_result", update_statics_data)

    # 在atmp平台发送企业微信消息
    """
    data = {"task_id": task_id, "send_type": "weixin"}
    result = send_atmp(file_content, "/edi/send_report", data)

    data = {"task_id": task_id, "send_type": "email"}
    result = send_atmp(file_content, "/edi/send_report", data)
    """
    # 执行完用例后将批次号置为空
    file_content["parameter"]["task_log_id"] = ""
    file_content["parameter"]["task_id"] = ""
    file_content["parameter"]["batch_no"] = ""
    file_content["parameter"]["test_code"] = ""
    file_content["parameter"]["firetime_start"] = ""
    file_content["parameter"]["firetime_end"] = ""
    file_content["parameter"]["log_time"] = 0.000
    file_content["parameter"]["log_result"] = ""
    file_content["parameter"]["memo"] = ""
    json_file.set(file_content)
