import time
from cases.AICardProject.page.marketingBusinessCenterPO.popupManagementPO import popupManagementPO


class PopupManagementLg:

    def __init__(self, driver):
        self.driver = driver
        self.popupManagementPO = popupManagementPO(driver)

    def into_popup_management_lg(self):
        # 打开营销业务中心-弹窗管理
        time.sleep(2)
        self.popupManagementPO.into_popup_management()

    def select_item_lg(self, var):
        # 输入关联项目进行搜索
        time.sleep(2)
        self.popupManagementPO.select_item(params=var)

    def search_marketing_popup_lg(self, var):
        # 输入关键字进行搜索
        time.sleep(2)
        self.popupManagementPO.search_marketing_popup(params=var)

    def new_marketing_popup_lg(self, var):
        # 新增营销弹窗
        time.sleep(2)
        self.popupManagementPO.new_marketing_popup(params=var)

    def edit_marketing_popup_lg(self, var):
        # 修改营销弹窗名称
        time.sleep(2)
        self.popupManagementPO.edit_marketing_popup(params=var)

    def delete_marketing_popup_lg(self):
        # 删除营销弹窗
        time.sleep(2)
        self.popupManagementPO.delete_marketing_popup()

    def access_authorization_popup_lg(self):
        # 进入授权弹窗
        time.sleep(2)
        self.popupManagementPO.access_authorization_popup()

    def keyword_search_lg(self, var):
        # 关键字搜索授权弹窗
        time.sleep(2)
        self.popupManagementPO.keyword_search(params=var)

    def add_authorization_popup_lg(self, var):
        # 新增授权弹窗
        time.sleep(2)
        self.popupManagementPO.add_authorization_popup(params=var)

    def edit_authorization_popup_lg(self):
        # 编辑授权弹窗
        time.sleep(2)
        self.popupManagementPO.edit_authorization_popup()

    def delete_authorization_popup_lg(self):
        # 删除授权弹窗
        time.sleep(2)
        self.popupManagementPO.delete_authorization_popup()
