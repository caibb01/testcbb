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

from myweb.tools.support_atmp.support_atmp_run import report_result_to_atmp, check_case
from myweb.utils.mail import Email
from selenium.webdriver.chrome.options import Options

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
CASE_PATH = os.path.join(BASE_PATH, 'cases')
OUTPUT_PATH = os.path.join(BASE_PATH, 'outputs')
DATA_PATH = os.path.join(BASE_PATH, 'data')
CONFIG_PATH = os.path.join(BASE_PATH, 'conf')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template')
STORAGE_PATH = os.path.join(BASE_PATH, 'myweb', 'core', 'storage.json')
CONFIG = 'single.json'

STORAGE = None


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
    f = open(STORAGE_PATH, "w", encoding='utf-8')
    if content and isinstance(content, dict):
        json.dump(content, f, indent=4, ensure_ascii=False)
    f.close()


def _setUp_storage(config_name, output=None):
    # 初始化缓存文件
    config = _get_config(config_name)
    output = output if output else config['output']
    content = {}
    content["info"] = []
    content['timestamp'] = output
    content['project'] = config['project_name']
    content['configPath'] = os.path.join(CONFIG_PATH, config_name)
    content['imagePath'] = os.path.join(OUTPUT_PATH, config['project_name'], output, 'image')
    content['resultPath'] = os.path.join(OUTPUT_PATH, config['project_name'], output, 'result.json')
    _set_storage(content)


def _step_screenshot(driver, ty, type_name, msg):
    if isinstance(driver, webdriver.Remote):

        storage = _get_storage()

        current_stamp = datetime.datetime.now().timestamp()
        current_time = datetime.datetime.fromtimestamp(current_stamp).strftime("%Y-%m-%d %H:%M:%S")
        file_time = datetime.datetime.fromtimestamp(current_stamp).strftime("%Y%m%d%H%M%S")
        filename = ty + '_' + file_time + '.png'
        screen_path = os.path.join(OUTPUT_PATH, storage['project'], storage['timestamp'], "image", filename)

        driver.get_screenshot_as_file(screen_path)
        storage["info"].append({
            "type": ty,
            "type_name": type_name,
            "msg": msg,
            "filename": filename,
            "path": screen_path,
            "timestamp": current_stamp,
            "current_time": current_time
        })
        _set_storage(storage)
    else:
        print("driver 类型不正确 截图失败 driver: %s ; type: %s" % (driver, type(driver)))


def _decide_config(el):
    config = _get_config()
    if (el in config.keys() and config[el]):
        return True, config[el]
    return False, None


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

    def run(self):
        self._setUp_config()
        _setUp_storage(config_name=self.config_name)
        try:
            self.case_path = os.path.join(CASE_PATH, self.config['project_name'], "case")
        except:
            raise Exception("File '{0}' not exist <project_name>".format(self.config_path))
        discover = unittest.defaultTestLoader.discover(self.case_path, pattern="test*.py", top_level_dir=None)

        runner = unittest.TextTestRunner()
        runner.run(discover)

        retry_mode, retry_times = _decide_config('retry')
        report_mode, _ = _decide_config('report_mode')
        email_mode, receiver = _decide_config('email_mode')

        if retry_mode:
            self._run_fail_case(retry=retry_times)

        if report_mode:
            self._get_result()
            self._report()
            if email_mode:
                print("send email...")
                self._mail(receiver=receiver)

        self._tearDown_config()

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

        # 生成email_html聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(TEMPLATE_PATH),
            extensions=(),
            autoescape=True
        )
        template = env.get_template("report_template.html", TEMPLATE_PATH)
        self.email_html = template.render({"results": self.result})

        self.mail_report_path = os.path.join(OUTPUT_PATH, STORAGE['project'], 'report.html')
        f = open(self.mail_report_path, "w", encoding='utf-8')
        f.write(self.email_html)
        f.close()

        # output_file = os.path.join(root_dir, "summary.html")
        # with io.open(output_file, 'w', encoding="utf-8") as f:
        #     f.write(html)
        # pass

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
        self.file_path = os.path.join(OUTPUT_PATH, self.config['project_name'], self.config['output'])
        if not os.path.exists(self.file_path):
            raise Exception("File '{0}' not exist <project_name>".format(self.file_path))
        else:
            f = open(os.path.join(self.file_path, 'result.json'), 'r', encoding='utf-8')
            self.result = json.load(f)
            f.close()
        return self.result

    def _set_result(self, content):
        self.result_path = os.path.join(OUTPUT_PATH, self.config['project_name'], self.config['output'], 'result.json')
        f = open(self.result_path, 'w', encoding='utf-8')
        json.dump(content, f, indent=4, ensure_ascii=False)
        f.close()
        return content

    def _setUp_config(self):
        """
        初始化配置文件，将运行时间作为output文件夹名称保存在配置文件中
        :return:
        """
        self.config = _get_config(config_name=self.config_name)
        self.config['output'] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        _set_config(config_name=self.config_name, content=self.config)

    def _tearDown_config(self):
        """
        删除初始化时保存的output文件夹名称
        :return:
        """
        self.config = _get_config(config_name=self.config_name)
        del self.config['output']
        _set_config(config_name=self.config_name, content=self.config)

        # f = open(self.config_path, "w", encoding='utf-8')
        # del self.config['output']
        # json.dump(self.config, f, indent=4, ensure_ascii=False)
        # f.close()


class TestCase(unittest.TestCase):
    __author__ = '佚名'
    driver = None

    @classmethod
    def setUpClass(cls):
        if _decide_config("auto_open_driver")[0]:
            cls._global_config = _get_global_config()
            option = webdriver.ChromeOptions()
            # chrome_options = Options()
            # chrome_options.add_argument('--headless')
            # 浏览器默认不关闭
            option.add_experimental_option("detach", True)
            # cls.driver = webdriver.Chrome(cls._global_config['driverPath'],chrome_options = chrome_options)
            # cls.driver = webdriver.Chrome(cls._global_config['driverPath'])

        config_path = os.path.join(CONFIG_PATH, CONFIG)
        cls._config = cls._get_result(cls, config_path)
        cls._output = cls._config[
            'output'] if 'output' in cls._config.keys() else datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        cls._file_path = os.path.join(OUTPUT_PATH, cls._config['project_name'], cls._output)
        cls._image_file_path = os.path.join(cls._file_path, "image")
        if not os.path.exists(cls._file_path):
            os.makedirs(cls._file_path)
            if not os.path.exists(cls._image_file_path):
                os.makedirs(cls._image_file_path)
        _setUp_storage(config_name=CONFIG, output=cls._output)
        cls.run_flag = None

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

        cls._storage = _get_storage()
        cls._storage["module_name"] = cls.__module__
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

        print(all_results_info['case_num'])
        cls._write_result(cls, result_path, all_results_info)

    def setUp(self):
        # 每次执行用例前先将result初始化total_time
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
                        "retry": 0}

        self._storage = _get_storage()
        self._storage["case_name"] = self._testMethodName
        _set_storage(self._storage)
        # 定义测试编号
        self.test_code = None

    def tearDown(self):
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
            _step_screenshot(driver=self.driver, ty="fail", type_name="用例执行失败", msg="")
        else:
            self._result["success"] = True
        # 每次用例执行完毕之后，将单个用例结果写入result
        # 记录操作信息
        self._storage = _get_storage()
        if self._storage["info"]:
            for i in self._storage["info"]:
                self._result["screen"].append(i)
            # 清除操作缓存
            self._storage["info"] = []
            _set_storage(self._storage)

        self._result['end_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._result['end_timestamp'] = time.time()
        self._result['total_time'] = round(self._result['end_timestamp'] - self._result['start_timestamp'], 3)
        self._results['cases_info'].append(self._result)

        report_to_atmp = _decide_config("report_to_atmp")[0]
        if report_to_atmp and self._check_case(self.test_code):
            if self._result["success"] is True:
                print(self.test_code)
                report_result_to_atmp(self.test_code, "pass", self._result["start_timestamp"], self._result["end_timestamp"],
                                      "预期与实际结果一致")
            else:
                report_result_to_atmp(self.test_code, "fail", self._result["start_timestamp"], self._result["end_timestamp"],
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
        if self.test_code is None:
            self.test_code = test_codes
        report_to_atmp = _decide_config("report_to_atmp")[0]
        if report_to_atmp and self.run_flag is None:
            self.run_flag = check_case(test_codes)
            print("是否执行用例：" + str(self.test_code) + " -> " + str(self.run_flag))
        return self.run_flag


_get_storage()

if __name__ == '__main__':
    r = Runner(config_name='demo.json')
    r.run()
