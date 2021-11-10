# !/usr/bin/python
# -*- coding: utf-8 -*-
import os, json
import time
import uuid
from myweb.utils.HttpRequest import HttpRequest

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))[0]
ATMP_CONFIG_PATH = os.path.join(BASE_PATH, 'conf')
ATMP_FILE = "run_atmp_param.json"


def report_result_to_atmp(test_codes, case_exec_result, start_timestamp, end_timestamp, memo):
    """上报结果给ATMP系统"""
    if len(test_codes) > 0:
        for test_code in test_codes:
            report_one_case_to_atmp(test_code, case_exec_result, start_timestamp, end_timestamp, memo)


def report_one_case_to_atmp(test_code, case_exec_result, start_timestamp, end_timestamp, memo):
    atmp_config_path = os.path.join(ATMP_CONFIG_PATH, ATMP_FILE)
    # 判断配置文件是否存在
    if os.path.exists(atmp_config_path):
        json_file = JsonConfigATMP(atmp_config_path)
        file_content = json_file.get()
        # 判断是否开启上传结果到ATMP系统
        if file_content["parameter"]["batch_no"] != "":
            file_content["parameter"]["log_result"] = case_exec_result
            file_content["parameter"]["task_log_id"] = str(uuid.uuid1())
            assert "" != test_code
            file_content["parameter"]["test_code"] = test_code
            file_content["parameter"]["tester"] = file_content["tester_id"]

            # 转换时间戳为带毫秒的时间格式
            file_content["parameter"]["firetime_start"] = cvt_timestamp(start_timestamp)
            file_content["parameter"]["firetime_end"] = cvt_timestamp(end_timestamp)
            file_content["parameter"]["log_time"] = end_timestamp - start_timestamp
            file_content["parameter"]["memo"] = memo
            json_file.set(file_content)

            # 调用ATMP上传结果
            print("调用ATMP系统接口")
            print(file_content)
            headers = {"Content-Type": "application/json", "User-Id": file_content["tester_id"]}
            r = HttpRequest()
            post_result = r.sendPost(file_content["atmp_url"] + "/edi/add_task_log", headers=headers,
                                     data=file_content["parameter"])
            assert post_result["code"] == 0
            post_result = r.sendPost(file_content["atmp_url"] + "/edi/update_task_log", headers=headers,
                                     data=file_content["parameter"])
            assert post_result["code"] == 0


def check_case(test_codes):
    """
    是否跳过执行
    :param test_codes:
    :return:
    """
    run_flag = False
    atmp_config_path = os.path.join(ATMP_CONFIG_PATH, ATMP_FILE)
    # 判断配置文件是否存在
    if os.path.exists(atmp_config_path):
        json_file = JsonConfigATMP(atmp_config_path)
        file_content = json_file.get()
        headers = {"Content-Type": "application/json;charset=UTF-8", "User-Id": file_content["tester_id"]}
        data_param = {
            "node_id": file_content["parameter"]["node_id"],
            "task_id": file_content["parameter"]["task_id"],
            "tc_status": "auto"
        }
        r = HttpRequest()
        result = r.sendPost(url=file_content["atmp_url"] + "/edi/get_node_tcs", headers=headers,
                            data=data_param)
        exec_case_code_list = result["data"]
        print(exec_case_code_list)
        if test_codes is not None and len(test_codes) > 0:
            for case_code in test_codes:
                for exec_case_code in exec_case_code_list:
                    if case_code in exec_case_code:
                        return True
    return run_flag


def cvt_timestamp(ct):
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp


class JsonConfigATMP():
    def __init__(self, path):
        self.path = path

    def get(self):
        f = open(self.path, 'r', encoding='utf-8')
        self.config = json.load(f)
        f.close()
        return self.config

    def set(self, data):
        f = open(self.path, "w", encoding='utf-8')
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()


if __name__ == "__main__":
    print("OK")
