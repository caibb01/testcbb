import time
from cases.AICardProject.page.marketingBusinessCenterPO.bookingManagementPO import bookingManagementPO


class bookingManagementLG:

    def __init__(self, driver):
        self.driver = driver
        self.bookingManagementPo = bookingManagementPO(driver)

    # 进入预约管理
    def into_booking_management(self, var):
        time.sleep(3)
        self.bookingManagementPo.into_booking_management()
        time.sleep(2)

    # 预约须知设置-操作
    def booking_instructions_option(self, var):
        self.bookingManagementPo.booking_instructions(description=var["description"], p_ame=var["p_name"])
        time.sleep(3)

    # 页面设置-操作
    def booking_page_setup(self, var):
        self.bookingManagementPo.page_setup(path=var["path"])

    # 填写字段设置-操作
    def add_filed_option(self):
        self.bookingManagementPo.add_filed()

    # 添加自定义字段-操作
    def add_custom_filed(self, var):
        self.bookingManagementPo.add_custom_filed(enter_name=var["enter_name"], p_name2=var["p_name2"])

    # 接待量设置
    def reception_setting_option(self):
        self.bookingManagementPo.reception_setting()

    # 可预约日期设置
    def appointment_date_option(self, var):
        self.bookingManagementPo.appointment_date(days=var["days"])

    # 资格验证设置
    def qualification_setting_option(self, var):
        self.bookingManagementPo.qualification_setting(phone01=var["phone01"], phone02=var["phone02"])



