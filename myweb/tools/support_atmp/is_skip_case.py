# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os

import requests

from myweb.core.runner import CONFIG_PATH
from myweb.utils.config import JsonConfig


def is_skip(case_code_list):
    """
    是否跳过执行
    :param case_code_list:
    :return:
    """
    ATMP_FILE = "run_atmp_param.json"
    atmp_config_path = os.path.join(CONFIG_PATH, ATMP_FILE)

    json_file = JsonConfig(atmp_config_path)
    file_content = json_file.get()
    headers = {"Content-Type": "application/json;charset=UTF-8", "User-Id": file_content["tester_id"]}
    data_param = {
        "node_id": file_content["parameter"]["node_id"],
        "task_id": file_content["parameter"]["task_id"],
        "tc_status": "auto"

    }
    skip = True
    try:
        result = requests.post(url=file_content["atmp_url"] + "/edi/get_node_tcs", headers=headers,
                               data=json.dumps(data_param))
        exec_case_code_list = json.loads(result.content)["data"]
        print(exec_case_code_list)
        if len(case_code_list) > 0:
            for case_code in case_code_list:
                for exec_case_code in exec_case_code_list:
                    if case_code in exec_case_code:
                        return skip
                    else:
                        skip = False
    except:
        print("edi/get_node_tcs接口调用失败")
    return skip


if __name__ == "__main__":
    print(is_skip(["C11001"]))
