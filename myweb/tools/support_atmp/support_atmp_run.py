# !/usr/bin/python
# -*- coding: utf-8 -*-
import os,json
import time
import uuid
from myweb.utils.HttpRequest import HttpRequest

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))[0]
ATMP_CONFIG_PATH = os.path.join(BASE_PATH, 'conf')
ATMP_FILE = "run_atmp_param.json"

def report_result_to_atmp(test_code,case_exec_result,start_timestamp):
    """上报结果给ATMP系统"""
    atmp_config_path = os.path.join(ATMP_CONFIG_PATH, ATMP_FILE)

    # 判断配置文件是否存在
    print("==>")
    print(atmp_config_path)
    print(os.path.exists(atmp_config_path))
    if os.path.exists(atmp_config_path):
        json_file = JsonConfigATMP(atmp_config_path)
        file_content = json_file.get()
        # 判断是否开启上传结果到ATMP系统
        print("==>")
        print(file_content)
        if file_content["is_report_result_to_atmp"] is True and file_content["parameter"]["batch_no"] != "":
            file_content["parameter"]["log_result"] = case_exec_result
            file_content["parameter"]["task_log_id"] = str(uuid.uuid1())
            assert "" != test_code
            file_content["parameter"]["test_code"] = test_code
            print(test_code)

            # 转换时间戳为带毫秒的时间格式
            ct = start_timestamp
            local_time = time.localtime(ct)
            data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
            data_secs = (ct - int(ct)) * 1000
            time_stamp = "%s.%03d" % (data_head, data_secs)
            file_content["parameter"]["firetime_start"] = time_stamp
            # print(u"结果上报")
            # print (file_content)
            try:
                # 调用ATMP上传结果
                print("调用ATMP系统接口")
                print(file_content)
                r = HttpRequest()
                post_result = r.sendPost(file_content["atmp_url"] + "/edi/add_task_log",
                                       data=file_content["parameter"])
                assert post_result["code"] == 0
                return post_result
            except Exception as e:
                return e


def update_atmp_config_firetime_start():
    """更新配置文件中firetime_start字段为执行时间为带毫秒的时间格式"""
    atmp_config_path = os.path.join(ATMP_CONFIG_PATH, ATMP_FILE)
    if os.path.exists(atmp_config_path):
        json_file = JsonConfigATMP(atmp_config_path)
        file_content = json_file.get()
        # 判断是否开启上传结果到ATMP系统
        if file_content["is_report_result_to_atmp"] is True:
            ct = time.time()
            local_time = time.localtime(ct)
            data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
            data_secs = (ct - int(ct)) * 1000
            time_stamp = "%s.%03d" % (data_head, data_secs)
            file_content["parameter"]["firetime_start"] = time_stamp
            json_file.set(file_content)

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
    result = report_result_to_atmp("pass",1625644681.028227)
