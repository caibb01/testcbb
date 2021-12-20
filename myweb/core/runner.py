import os
import unittest
import inspect
import traceback
import datetime
import re
import json
import time
import jinja2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from myweb.tools.support_atmp_run import report_result_to_atmp, check_case
from myweb.utils.mail import Email
from concurrent.futures import ThreadPoolExecutor, wait
import threading
import shutil
from fnmatch import fnmatch

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
CASE_PATH = os.path.join(BASE_PATH, 'cases')
OUTPUT_PATH = os.path.join(BASE_PATH, 'outputs')
DATA_PATH = os.path.join(BASE_PATH, 'data')
CONFIG_PATH = os.path.join(BASE_PATH, 'conf')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template')
STORAGE_PATH = os.path.join(BASE_PATH, 'myweb', 'core', 'storage.json')
CONFIG = 'single.json'

STORAGE = None
lock_storage = [threading.RLock() for i in range(6)]
lock_mars = [threading.RLock() for j in range(3)]

dir_data = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
thread_flag = False


def _get_global_config(config_name=None):
    """
    获取项目全局的配置文件信息（例如driver_path）
    :return:
    """
    config_path = config_name if config_name else 'config.json'
    f = open(os.path.join(DATA_PATH, config_path), 'r', encoding='utf-8')
    config = json.load(f)
    f.close()
    return config


def _get_config(config_name=None):
    """
    获取运行用例集的配置文件信息
    :return:
    """
    with lock_mars[0]:
        config_path = config_name if config_name else CONFIG
        f = open(os.path.join(CONFIG_PATH, config_path), 'r', encoding='utf-8')
        config = json.load(f)
        f.close()
        return config


def _set_config(config_name=None, content=None):
    """
    设置运行用例集的配置文件信息
    :return:
    """
    with lock_mars[0]:
        config_path = config_name if config_name else CONFIG
        content = content if content else {}
        f = open(os.path.join(CONFIG_PATH, config_path), 'w', encoding='utf-8')
        json.dump(content, f, indent=4, ensure_ascii=False)
        f.close()
        return content


def _get_storage():
    """
    获取运行任务的缓存文件
    :return:
    """
    with lock_storage[0]:
        if not os.path.exists(STORAGE_PATH):
            os.makedirs(STORAGE_PATH)
        f = open(STORAGE_PATH, 'r', encoding='utf-8')
        global STORAGE
        STORAGE = json.load(f)
        f.close()
        return STORAGE


def _set_storage(content=None):
    """
    修改运行任务的缓存文件
    :return:
    """
    with lock_storage[0]:
        f = open(STORAGE_PATH, "w", encoding='utf-8')
        if content and isinstance(content, dict):
            json.dump(content, f, indent=4, ensure_ascii=False)
        f.close()


def _setUp_storage(config_name, output=None):
    # 初始化缓存文件
    current_tread_name = threading.current_thread().name
    config = _get_config(config_name)
    with lock_storage[1]:
        storeges_ = _get_storage()
        output = output if output else config['output'][current_tread_name]
        content = {current_tread_name:{}}
        content[current_tread_name]["info"] = []
        content[current_tread_name]['timestamp'] = output.split("_")[-1]
        content[current_tread_name]['project'] = config['project_name']
        content[current_tread_name]['configPath'] = os.path.join(CONFIG_PATH, config_name)
        content[current_tread_name]['reportPath'] = os.path.join(OUTPUT_PATH, config['project_name'], dir_data, output, 'result.html')
        content[current_tread_name]['imagePath'] = os.path.join(OUTPUT_PATH, config['project_name'], dir_data, output, 'image')
        content[current_tread_name]['resultPath'] = os.path.join(OUTPUT_PATH, config['project_name'], dir_data, output, 'result.json')
        storeges_.update(content)
        _set_storage(storeges_)


def _step_screenshot(driver, ty, type_name, msg):
    if isinstance(driver, webdriver.Remote):
        concurrent_tread_name = threading.current_thread().name
        with lock_storage[2]:
            storage = _get_storage()
            current_stamp = datetime.datetime.now().timestamp()
            current_time = datetime.datetime.fromtimestamp(current_stamp).strftime("%Y-%m-%d %H:%M:%S")
            file_time = datetime.datetime.fromtimestamp(current_stamp).strftime("%Y%m%d%H%M%S")
            filename = ty + '_' + file_time + '.png'
            screen_path = os.path.join(storage[concurrent_tread_name]['imagePath'], filename)

            driver.get_screenshot_as_file(screen_path)
            storage[concurrent_tread_name]["info"].append({
                "type": ty,
                "type_name": type_name,
                "msg": msg,
                "filename": filename,
                "path": screen_path,
                "timestamp": current_stamp,
                "current_time": current_time
            })
            _set_storage(storage)
        return screen_path
    else:
        print("driver 类型不正确 截图失败 driver: %s ; type: %s" % (driver, type(driver)))


def _decide_config(el):
    config = _get_config()
    if (el in config.keys() and config[el]):
        return True, config[el]
    return False, None


def _get_file(path, pattern):
    file_path_list = []
    for root_, _, files in os.walk(path):
        for file in files:
            if fnmatch(file, pattern):
                file_path = os.path.join(root_, file)
                file_path_list.append(file_path)
    return file_path_list


# 多线程并行运行测试用例测试类
class ThreadRunner(object):
    def __init__(self, max_workers=2, thread_name_prefix="Thread_", config_name=CONFIG):
        self._pool = ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix=thread_name_prefix)
        self._config_name = config_name
        self._global_config = _get_global_config()
        self._output_path = os.path.join(OUTPUT_PATH, _get_config(config_name)["project_name"], dir_data)
        self._summary_results = None
        self._end_timestamp = None
        self._start_timestamp = None

    # 多线程运行测试用例方法
    def thread_run(self, case_path="", pattern=""):
        global thread_flag
        thread_flag = True
        self._start_timestamp = time.time()
        path_ = os.path.join(CASE_PATH, _get_config(config_name=self._config_name)["project_name"], "case")
        case_path_ = path_ if case_path == "" else os.path.join(path_, case_path)
        # 获取主线程或多线程的用例文件
        case_file_list, main_run_list = self._get_run_case_file(case_path_, "test*.py" if pattern == "" else pattern)
        # 多线程运行
        all_task = [self._pool.submit(self._run_task,  case_path=case_path_, pattern=file_) for file_ in case_file_list]
        wait(all_task)
        self._pool.shutdown()
        # 主线程运行
        if len(main_run_list):
            self._run_task(case_path=case_path_, pattern=main_run_list)
        self._end_timestamp = time.time()
        self._summary_thread_results(self._output_path)
        self._move_file(self._output_path)
        self._del_tread_dir(self._output_path)

        report_mode, _ = _decide_config('report_mode')
        email_mode, receiver = _decide_config('email_mode')

        # 发送测试报告
        if report_mode:
            self._report()
            if email_mode:
                print("send email...")
                self._mail(receiver=receiver)

    # 运行测试用例方法
    def _run_task(self, case_path, pattern):
        run_task = Runner(config_name=self._config_name)
        run_task.run(case_path=case_path, pattern=pattern)

    # 获取指定测试用例文件名称
    def _get_run_case_file(self, path, pattern="test*.py"):
        """获取指定测试用例文件名称
        待实现-------> group: 多线程执行文件分成几组
        path: 用例根目录
        pattern: 匹配用例名称
        return : name_list、main_run_list
        待实现------->   thread_run_list： 用来合理分配每个线程所执行的用例文件
        name_list： 用来在多线程执行的用例文件, 二维数组
        main_run_list： 用来在主线程执行的用例文件，一维数组
        """
        path_list = _get_file(path, pattern)
        name_list = list(set([path.split("\\")[-1] for path in path_list]))
        main_list = _get_config(self._config_name)["MainThread"]
        main_run_list = []
        for name in name_list:
            if name in main_list:
                name_list.remove(name)
                main_run_list.append(name)
        name_list = [[name] for name in name_list]
        return name_list, main_run_list

    # 汇总各自线程下的错误截图到同一目录下
    @staticmethod
    def _move_file(path, pattern="*.png"):
        png_path_list = _get_file(path, pattern)
        new_path = os.path.join(path, "image")
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        for png_path in png_path_list:
            shutil.move(png_path, new_path)

    # 汇总各自线程生成的result.json文件
    def _summary_thread_results(self, path, pattern="result.json"):
        self._summary_results = {
            "start_time": "",
            "start_timestamp": 0,
            "total_time": 0,
            "end_time": "",
            "end_timestamp": 0,
            "results": [],
            "error": 0,
            "failed": 0,
            "success": 0,
            "case_num": 0,
            "passrate": "",
            "project_name": "",
            "project_name_zh": "",
            "miss_case_info": [],
            "miss_num": 0
        }
        # 汇总用例信息
        get_thread_result = _get_file(path, pattern)
        for result_file in get_thread_result:
            if result_file != os.path.join(self._output_path, "result.json"):
                content_ = open(result_file, 'r', encoding='utf-8')
                result_ = json.load(content_)
                content_.close()
                self._summary_results["results"].extend(result_["results"])
                self._summary_results["miss_case_info"].extend(result_["miss_case_info"])
                self._summary_results["error"] += result_["error"]
                self._summary_results["failed"] += result_["failed"]
                self._summary_results["success"] += result_["success"]
                self._summary_results["case_num"] += result_["case_num"]
                self._summary_results["miss_num"] += result_["miss_num"]
                self._summary_results["project_name"] = result_["project_name"]
                self._summary_results["project_name_zh"] = result_["project_name_zh"]

        # 重新计算时间
        self._summary_results["start_timestamp"] = self._start_timestamp
        self._summary_results["end_timestamp"] = self._end_timestamp
        self._summary_results["total_time"] = round(self._end_timestamp - self._start_timestamp, 1)
        self._summary_results["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._start_timestamp))
        self._summary_results["end_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self._end_timestamp))

        # 重新计算通过率
        self._summary_results['passrate'] = "%.2f%%" % (
            float(self._summary_results["success"] * 100) /
            (self._summary_results['case_num'] + self._summary_results["miss_num"])
        )

        # 写入汇总后的resul.json文件
        with open(os.path.join(self._output_path, "result.json"), 'w', encoding='utf-8') as f:
            json.dump(self._summary_results, f, indent=4, ensure_ascii=False)

    # 删除指定根目录下指定的子目录(各自线程生成的目录)
    @staticmethod
    def _del_tread_dir(path, pattern="*Thread*"):
        thread_dir = os.listdir(path)
        for dir_ in thread_dir:
            if fnmatch(dir_, pattern):
                del_path = os.path.join(path, dir_)
                shutil.rmtree(path=del_path, ignore_errors=True)
                print("已成功删除目录:{}".format(del_path))

    # 生成html测试报告
    def _report(self):
        # 生成email_html聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(TEMPLATE_PATH),
            extensions=(),
            autoescape=True
        )
        template = env.get_template("report_template.html", TEMPLATE_PATH)
        self.email_html = template.render({"results": self._summary_results})
        f = open(os.path.join(self._output_path, "result.html"), "w", encoding='utf-8')
        f.write(self.email_html)
        f.close()

    # 发送email邮件
    def _mail(self, receiver=None):
        if receiver:
            e = Email(title="Mars自动化测试报告邮件",
                      receiver=receiver,
                      server='smtp.exmail.qq.com',
                      sender=self._global_config['email']['username'],
                      password=self._global_config['email']['password'],
                      sender_name="MarsUI自动化测试报告",
                      html=self.email_html)
            e.send()


# 主线程运行测试类
class Runner():
    def __init__(self, config_name=CONFIG):
        self.config_path = os.path.join(CONFIG_PATH, config_name)
        self.config_name = config_name
        self.global_config = _get_global_config()
        # 缓存文件 存储正在执行的任务项目名称、时间戳
        self.storage_path = STORAGE_PATH
        self.storage = None
        self.config = None
        self.result = None
        self.receiver = []
        self.email_html = None
        global CONFIG
        CONFIG = self.config_name

    def run(self, pattern, case_path=""):
        self._setUp_config()
        _setUp_storage(config_name=self.config_name)
        try:
            if case_path == "":
                self.case_path = os.path.join(CASE_PATH, self.config['project_name'], "case")
            else:
                self.case_path = os.path.join(CASE_PATH, self.config['project_name'], "case", case_path)
            print("case_path:%s"%self.case_path)
        except:
            raise Exception("File '{0}' not exist <project_name>".format(self.config_path))
        # 加载测试套件
        if not thread_flag:
            discover = unittest.defaultTestLoader.discover(
                   self.case_path, pattern="test*.py" if pattern == "" else pattern, top_level_dir=None)
        else:
            discover = self._merge_discover(self.case_path, pattern)
        # 获取测试套件所有用例名称和用例描述,返回值为dict类型，key为用例名称，value为用例描述
        all_suit_case_dict = self._get_all_suit(discover)
        # 运行测试套件
        runner = unittest.TextTestRunner()
        runner.run(discover)

        retry_mode, retry_times = _decide_config('retry')
        report_mode, _ = _decide_config('report_mode')
        email_mode, receiver = _decide_config('email_mode')
        # 失败用例重试
        if retry_mode:
            self._run_fail_case(retry=retry_times)
        # 重写测试报告，把丢失用例信息也写进来
        self._rewrite_report(all_suit_case_dict)
        # 发送测试报告
        if report_mode:
            self._get_result()
            self._report()
            if email_mode and not thread_flag:
                print("send email...")
                self._mail(receiver=receiver)
        self._tearDown_config()


    def _merge_discover(self, case_path, case_file_list):
        discover_list = [unittest.defaultTestLoader.discover(case_path, pattern=case_file) for case_file in case_file_list]
        merge_discover = discover_list[0]
        for d in range(1, len(discover_list)):
            for i in discover_list[d]._tests:
                merge_discover.addTest(i)
        return merge_discover


    def _get_all_suit(self, discover):
        """获取加载测试套件的所有用例名称和描述
        discover： 入参为测试套件
        return: 返回字典类型，key为用例名，value为用例描述
        """
        # 获取测试套件用例名称和用例描述,key为用例名称，value为用例描述
        all_suit_case_dict = {}
        for i in discover._tests:
            for j in i._tests:
                for k in j._tests:
                    all_suit_case_dict[k._testMethodName] = k._testMethodDoc.strip() if k._testMethodDoc is not None else "用例未添加描述说明~"
        return all_suit_case_dict


    def _rewrite_report(self, all_suit_case_dict):
        """重写测试报告，增加丢失用例
        all_suit_case_dict：入参为_get_all_suit的返回值
        """
        # 判断方法名是否在文件中，不在则属于丢失用例，把方法名和用例备注加进来
        case_info_ = self._get_result()
        # 获取已经执行的用例名称
        run_case_name = []
        for i in case_info_["results"]:
            for j in i["cases_info"]:
                run_case_name.append(j["case_name"])
        # 丢失的用例信息,只存用例名称和用例描述
        miss_case_info = []
        for i in all_suit_case_dict.keys():
            if i not in run_case_name:
                miss_case_info.append({"case_name": i, "case_doc": all_suit_case_dict[i]})
        case_info_["miss_case_info"] = miss_case_info
        case_info_["miss_num"] = len(miss_case_info)
        # 重写用例通过率，把丢失的也算进用例总数里
        case_info_['passrate'] = "%.2f%%" % (
            float(case_info_['success'] * 100) / (case_info_['case_num'] + case_info_["miss_num"]))
        self._set_result(content=case_info_)

    def _run_fail_case(self, retry=2):
        # 使用TestLoader，通过py文件名 module case等方式装载用例
        for i in range(retry):
            fail_cases = self._get_fail_case()
            if fail_cases:
                suite = unittest.TestSuite()
                runner = unittest.TextTestRunner()
                for fc in fail_cases:
                    test = unittest.TestLoader().loadTestsFromName(fc)
                    suite.addTest(test)
                print(suite)
                runner.run(suite)
                self._rewrite_fail_info()

    def _get_fail_case(self):
        case_result = self._get_result()
        fail_info = []
        for r in case_result["results"]:
            module = r["module_name"]
            class_name = r["class_name"]
            for c in r["cases_info"]:
                if c["success"] is False:
                    case_name = c["case_name"]
                    fail_info.append("%s.%s.%s" % (module, class_name, case_name))
        return fail_info

    def _rewrite_fail_info(self):
        flag = False
        while not flag:
            results = self._get_result()
            for r in range(len(results["results"]) - 1):
                if results["results"][r]["module_name"] == results["results"][-1]["module_name"]:
                    # 找到相同module，替换相应的用例，并且删掉最后一个result
                    for c in range(len(results["results"][r]["cases_info"])):
                        if results["results"][r]["cases_info"][c]["case_name"] == \
                                results["results"][-1]["cases_info"][0]["case_name"]:
                            results["results"][-1]["cases_info"][0]["retry"] = results["results"][r]["cases_info"][c]["retry"] + 1
                            del results["results"][r]["cases_info"][c]
                            results["results"][r]["cases_info"].append(results["results"][-1]["cases_info"][0])
                            break
                    results["results"].pop(-1)
                    results['error'] = len(
                        [0 for r in results['results'] for c in r['cases_info'] if c['is_error']])
                    results['failed'] = len(
                        [0 for r in results['results'] for c in r['cases_info'] if c['is_failure']])
                    results['success'] = len(
                        [0 for r in results['results'] for c in r['cases_info'] if c['success']])
                    results['case_num'] = len(
                        [0 for r in results['results'] for _ in r['cases_info']])
                    self._set_result(content=results)
                    break
            else:
                flag = True
                break

    def _report(self):
        current_thread_name = threading.current_thread().name
        # 生成email_html聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(TEMPLATE_PATH),
            extensions=(),
            autoescape=True
        )
        template = env.get_template("report_template.html", TEMPLATE_PATH)
        self.email_html = template.render({"results": self.result})
        f = open(_get_storage()[current_thread_name]['reportPath'], "w", encoding='utf-8')
        f.write(self.email_html)
        f.close()


    def _mail(self, receiver=None):

        if receiver:
            e = Email(title="优化测试报告邮件",
                      receiver=receiver,
                      server='smtp.exmail.qq.com',
                      sender=self.global_config['email']['username'],
                      password=self.global_config['email']['password'],
                      sender_name="优化测试报告邮件",
                      html=self.email_html)
            e.send()

    def _get_result(self):
        current_tread_name = threading.current_thread().name
        self.file_path = os.path.join(OUTPUT_PATH, self.config['project_name'], dir_data, self.config['output'][current_tread_name])
        if not os.path.exists(self.file_path):
            raise Exception("File '{0}' not exist <project_name>".format(self.file_path))
        else:
            f = open(os.path.join(self.file_path, 'result.json'), 'r', encoding='utf-8')
            self.result = json.load(f)
            f.close()
        return self.result

    def _set_result(self, content):
        current_tread_name = threading.current_thread().name
        self.result_path = os.path.join(OUTPUT_PATH, self.config['project_name'], dir_data, self.config['output'][current_tread_name], 'result.json')
        f = open(self.result_path, 'w', encoding='utf-8')
        json.dump(content, f, indent=4, ensure_ascii=False)
        f.close()
        return content

    def _setUp_config(self):
        """
        初始化配置文件，将运行时间作为output文件夹名称保存在配置文件中
        :return:
        """
        current_tread_name = threading.current_thread().name
        with lock_mars[1]:
            self.config = _get_config(config_name=self.config_name)
            self.config['output'][current_tread_name] = current_tread_name + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            _set_config(config_name=self.config_name, content=self.config)

    def _tearDown_config(self):
        """
        删除初始化时保存的output文件夹名称
        :return:
        """
        current_tread_name = threading.current_thread().name
        with lock_mars[2]:
            self.config = _get_config(config_name=self.config_name)
            del self.config['output'][current_tread_name]
            _set_config(config_name=self.config_name, content=self.config)


class TestCase(unittest.TestCase):
    __author__ = '佚名'
    driver = None

    @classmethod
    def setUpClass(cls):
        current_tread_name = threading.current_thread().name
        if _decide_config("auto_open_driver")[0]:
            cls._global_config = _get_global_config()
            option = webdriver.ChromeOptions()
            # 浏览器默认不关闭
            option.add_experimental_option("detach", True)
            # cls.driver = webdriver.Chrome(cls._global_config['driverPath'])

        config_path = os.path.join(CONFIG_PATH, CONFIG)
        cls._config = cls._get_result(cls, config_path)
        cls._output = cls._config[
            'output'][current_tread_name] if current_tread_name in cls._config["output"].keys() \
            else current_tread_name + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        cls._file_path = os.path.join(OUTPUT_PATH, cls._config['project_name'], dir_data, cls._output)
        cls._image_file_path = os.path.join(cls._file_path, "image")
        if not os.path.exists(cls._file_path):
            os.makedirs(cls._file_path)
            if not os.path.exists(cls._image_file_path):
                os.makedirs(cls._image_file_path)
        _setUp_storage(config_name=CONFIG, output=cls._output)

        cls._results = {
            "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "start_timestamp": time.time(),
            "cases_info": [],
            "author": cls.__author__,
            "module_name": cls.__module__,
            "class_name": cls.__name__,
            "project_name": cls._config['project_name'] if 'project_name' in cls._config.keys() else None,
            "project_name_zh": cls._config['project_name_zh'] if 'project_name' in cls._config.keys() else None,
        }
        with lock_storage[5]:
            cls._storage = _get_storage()
            cls._storage[current_tread_name]["module_name"] = cls.__module__
            _set_storage(cls._storage)


    @classmethod
    def tearDownClass(cls):
        # if not _decide_config("driver_always_open")[0]:
        #     # 浏览器常关配置，设置为True则不会自动关闭浏览器
        #     if isinstance(cls.driver, webdriver.Remote):
        #         print("driver quit!")
        #         cls.driver.quit()
        #     else:
        #         print("关闭浏览器失败 driver: %s" % cls.driver)

        cls._results['end_timestamp'] = time.time()
        cls._results['end_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cls._results['total_time'] = round(cls._results['end_timestamp'] - cls._results['start_timestamp'], 1)

        result_path = os.path.join(cls._file_path, 'result.json')

        if not os.path.exists(result_path):
            all_results_info = {
                "start_time": cls._results['start_time'],
                "start_timestamp": cls._results['start_timestamp'],
                "total_time": cls._results['total_time'],
            }
        else:
            all_results_info = cls._get_result(cls, result_path)
            all_results_info['total_time'] = round(cls._results['end_timestamp'] - all_results_info['start_timestamp'],
                                                   1)
        all_results_info['end_time'] = cls._results['end_time']
        all_results_info['end_timestamp'] = cls._results['end_timestamp']
        print(all_results_info)
        if 'results' in all_results_info:
            all_results_info['results'].append(cls._results)
        else:
            all_results_info['results'] = [cls._results]

        all_results_info['error'] = len(
            [0 for r in all_results_info['results'] for c in r['cases_info'] if c['is_error']])
        all_results_info['failed'] = len(
            [0 for r in all_results_info['results'] for c in r['cases_info'] if c['is_failure']])
        all_results_info['success'] = len(
            [0 for r in all_results_info['results'] for c in r['cases_info'] if c['success']])
        all_results_info['case_num'] = len([0 for r in all_results_info['results'] for _ in r['cases_info']])
        all_results_info['passrate'] = "%.2f%%" % (
                float(all_results_info['success'] * 100) / all_results_info['case_num'])
        all_results_info['project_name'] = cls._config['project_name'] if 'project_name' in cls._config.keys() else None
        all_results_info['project_name_zh'] = cls._config[
            'project_name_zh'] if 'project_name' in cls._config.keys() else None

        cls._write_result(cls, result_path, all_results_info)

    def setUp(self):
        # 每次执行用例前先将result初始化total_time
        current_tread_name = threading.current_thread().name
        self._test_filename = inspect.getsourcefile(self.__class__)
        self._has_assert_error = False
        self._result = {"case_name": self._testMethodName,
                        "start_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "start_timestamp": time.time(),
                        "case_doc": self._testMethodDoc.replace('\n', '').strip() if self._testMethodDoc else '',
                        "success": False,
                        "trace": "",
                        "is_failure": False,
                        "is_error": False,
                        "failed_line_num": -1,
                        "screen": [],
                        "image": "",
                        "retry": 0}
        with lock_storage[3]:
            self._storage = _get_storage()
            self._storage[current_tread_name]["case_name"] = self._testMethodName
            _set_storage(self._storage)
        # 定义测试编号
        self.test_code = ""

    def tearDown(self):
        current_thread_name = threading.current_thread().name
        sys_info = self._outcome.errors[-1][-1]
        test_method = getattr(self, self._testMethodName)
        source_line = inspect.getsourcelines(test_method)
        self._result["source"] = {"code": source_line[0], "start": source_line[1]}

        if sys_info:
            e_type, e_value, e_traceback = sys_info
            self._result["failed_line_num"] = -1
            stack_lines = traceback.format_exception(e_type, e_value, e_traceback)
            if len(stack_lines) > 2:
                r = re.compile(r"File [\'\"](.*)[\'\"], line (\d+), in (\w+)")
                for stack_line in stack_lines[1:]:
                    m = r.search(stack_line)
                    if m:
                        if (m.group(1) == self._test_filename and m.group(3) == self._testMethodName):
                            self._result["failed_line_num"] = int(m.group(2))
            if self._has_assert_error:
                self._result["trace"] = stack_lines[-1]
                self._result["is_failure"] = True
            else:
                self._result["trace"] = stack_lines[-1]
                self._result["is_error"] = True
            _step_screenshot(driver=self.driver, ty="fail_"+self._result["case_name"], type_name="用例执行失败", msg="")
        else:
            self._result["success"] = True

        if self._result["is_failure"] is True or self._result["is_error"] is True:
            # 忽略不是UI自动化没有截图，找不到图片而报错
            try:
                image_object = open(_get_storage()[current_thread_name]["info"][0]['path'], "rb")
                image = image_object.read()
                image_object.close()
                self._result["image"] = "data:image/png;base64," + base64.b64encode(image).decode()
            except IndexError:
                pass

        # 每次用例执行完毕之后，将单个用例结果写入result
        # 记录操作信息
        with lock_storage[4]:
            self._storage = _get_storage()
            if self._storage[current_thread_name]["info"]:
                for i in self._storage[current_thread_name]["info"]:
                    self._result["screen"].append(i)
                # 清除操作缓存
                self._storage[current_thread_name]["info"] = []
                _set_storage(self._storage)

        self._result['end_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._result['end_timestamp'] = time.time()
        self._result['total_time'] = round(self._result['end_timestamp'] - self._result['start_timestamp'], 3)
        self._results['cases_info'].append(self._result)

        report_to_atmp = _decide_config("report_to_atmp")[0]
        if report_to_atmp and self._check_case(self.test_codes):
            if self._result["success"] is True:
                report_result_to_atmp(self.test_codes, self.run_result, self._result["start_timestamp"], self._result["end_timestamp"],
                                      "预期与实际结果一致")
            else:
                report_result_to_atmp(self.test_codes, "fail", self._result["start_timestamp"], self._result["end_timestamp"],
                                      self._result["trace"])

    def __getattribute__(self, item):
        # 基本照抄MiniTest写法（Minium提供的TestCase）
        attr = super().__getattribute__(item)
        if item.startswith("assert") and callable(attr):
            def _hook_assert(*args, **kwargs):
                try:
                    attr(*args, **kwargs)
                except AssertionError:
                    self._has_assert_error = True
                    raise

            return _hook_assert
        else:
            return attr

    def _get_result(self, file_name):
        f = open(file_name, 'r', encoding='utf-8')
        result = json.load(f)
        f.close()
        return result

    def _write_result(self, file_name, result):
        f = open(file_name, "w", encoding='utf-8')
        json.dump(result, f, indent=4, ensure_ascii=False)
        f.close()

    def _check_case(self, test_codes):
        report_to_atmp = _decide_config("report_to_atmp")[0]
        if not report_to_atmp:
            return True
        if self.test_codes is None:
            self.test_codes = test_codes
        if self.run_flag is None:
            self.run_flag = check_case(test_codes)
            print("是否执行用例：" + str(self.test_codes) + " -> " + str(self.run_flag))
        return self.run_flag



if __name__ == '__main__':
    r = Runner(config_name='demo.json')
    r.run(pattern="")




