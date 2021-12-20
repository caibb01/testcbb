# -*- coding:utf-8 -*-
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from myweb.core.runner import TestCase
from myweb.tools.db_base_operation import DB_Operation
from myweb.tools.support_atmp.base_atmp_step import BaseAtmp
from myweb.tools.support_atmp.support_atmp_base_function import *
from myweb.utils.config import JsonConfig, conf

db_info = {"host": "10.10.4.53", "port": 3306, "user": "test", "password": "test1234", "db": "qfsoft_db_atmp"}


def execute_case_api(server_id, listv):
    db = DB_Operation(db_info)
    # 查询测试用例id
    case = listv.split(",")
    case_group_code = case[0].split(".")
    tc_id = db.select_db_one(
        'SELECT tc_id FROM `t_test_tc` where group_code="%s" and test_code="%s"' % (
        case_group_code[0], case_group_code[1]))
    case_steps = db.select_db_all("SELECT * FROM `t_test_tc_step` where tc_id = '%s'" % tc_id[0])
    new_case_steps_list = []
    for step in case_steps:
        case_step_list = []
        case_step_list.append(step[2])
        case_step_list.append(step[3])
        action_value = eval(step[5])

        if step[2] == "selenium":
            if step[4] == "page":
                object_value = db.select_db_one('select object_value from t_test_object where group_code = "%s" '
                                                'and object_name = "%s" ' % (case_group_code[0], action_value["page"]))
                case_step_list.append(object_value[0])
            else:
                # 获取步骤中的
                object_object_list = action_value["object"].split(".")
                page_name = object_object_list[0]
                page_object = object_object_list[1]
                object_id = db.select_db_one('select object_id from t_test_object where group_code = "%s" '
                                             'and object_name = "%s" ' % (case_group_code[0], page_name))
                detail_value = db.select_db_one('select detail_value from t_test_object_detail where object_id="%s" '
                                                'and detail_name = "%s"' % (object_id[0], page_object))

                detail_value_list = detail_value[0].split("=", 1)
                # print(detail_value_list)
                case_step_list.append(detail_value_list[0])
                case_step_list.append(detail_value_list[1])
                if "value" in action_value.keys():
                    case_step_list.append(action_value["value"])
        else:
            case_step_list.append(action_value[step[4]])
        new_case_steps_list.append(case_step_list)

    print(new_case_steps_list)

    atmp_case = ATMP_Test_Case()
    atmp_case.test_case_01(case_group_code[1],new_case_steps_list)



class ATMP_Test_Case(TestCase):
    def test_case_01(self,test_code,test_step):
        data_config = conf
        self.driver = webdriver.Chrome(executable_path=data_config["driverPath"])
        base_atmp = BaseAtmp(self.driver)
        self.test_code = test_code

        for i in test_step:
            if i[0] == "selenium" and i[1] == 'visit':
                base_atmp.visit(i[2])
            elif i[0] == "selenium":
                if i[2] == "xpath":
                    print('base_atmp.%s(%s)'%(i[1],i[3:]))
                    exec('base_atmp.%s(%s)'%(i[1],i[3:]))
            else:
                exec('%s(%s)' % (i[1], i[2:]))





if __name__ == "__main__":
    execute_case_api("xxx", "X0101.C11002,function,1.0,1,1")
    # atmp_case = ATMP_Test_Case()
    # atmp_case.test_case_01()
