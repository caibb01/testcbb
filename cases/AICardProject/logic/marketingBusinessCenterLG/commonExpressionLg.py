from time import sleep
from cases.AICardProject.page.marketingBusinessCenterPO.commonExpressionPO import CommonExpressionPO
from cases.AICardProject.logic.MenuManager import MenuManager


class CommonExpressionLg:
    def __init__(self, driver):
        self.driver = driver
        self.commonExpressionPo = CommonExpressionPO(driver)
        self.menuManager = MenuManager(driver)

    def into_common_expression_page(self):
        self.menuManager.choiceMenu("营销业务中心", "营销业务中心-常用语设置")

    def add_buyer_expression(self):
        self.commonExpressionPo.add_buyer_expression()

    def add_seller_expression(self):
        self.commonExpressionPo.add_seller_expression()

    def edit_expression(self):
        self.commonExpressionPo.edit_expression()

    def delete_expression(self):
        self.commonExpressionPo.delete_expression()