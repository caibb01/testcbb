#-*- encoding=utf8 -*-
from time import sleep

from myweb.core.BasePage import BasePage
from cases.AICardProject.page.userManagementPO.clientStandingBookPO import clientStandingBook
from cases.AICardProject.logic.MenuManager import MenuManager


class clientStandingBookLg():
    def __init__(self,driver):
        #super(clientStandingBookLg,self).__init__(driver)
        self.driver=driver
        self.clientStandingBookPO = clientStandingBook(driver)
        self.MenuManager = MenuManager(driver)

    def review_business_relationship_table_lg(self,var):
        '''查看业务关系表，关闭业务关系表（适用于集团客户、区域客户、项目客户）'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        self.clientStandingBookPO.review_business_relationship_table(var['modelName'] + '-')
        #关闭业务关系表（适用于集团客户、区域客户、项目客户）
        self.clientStandingBookPO.close_business_relationship_table(var['modelName'] + '-')


    def review_topological_graph_lg(self,var):
        '''查看来去拓扑图,关闭拓扑图'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        # 查看来去拓扑图
        self.clientStandingBookPO.review_topological_graph(var['modelName']+'-')
        # 关闭来去拓扑图
        self.clientStandingBookPO.close_topological_graph(var['modelName'] + '-')


    def export_list_lg(self,var):
        '''导出列表并下载'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        sleep(3)
        # 点击导出列表按钮
        self.clientStandingBookPO.export_list(var['modelName']+'-')
        # 导出客户列表页面，点击导出按钮
        self.clientStandingBookPO.export_function(var['modelName']+'-')




    def page_switching_lg(self,var):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        # 切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        self.clientStandingBookPO.click_next_page()
        self.clientStandingBookPO.click_previous_page()

    def group_cusromer_inquiry_lg(self,var):
        '''查询集团客户'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        self.clientStandingBookPO.group_customer_inquiry(var['parameter'])
        #对比列表中的数据，当前页没有找到点击下一页继续找，直到最后一页
        #self.clientStandingBookPO.contrast_list_data(var['checkData'])


    def regional_customer_inquiry_lg(self,var):
        '''查询区域客户'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        #区域客户-查询
        self.clientStandingBookPO.regional_customer_inquiry(var['parameter'])
        #对比列表中的数据，当前页没有找到点击下一页继续找，直到最后一页
        #self.clientStandingBookPO.contrast_list_data(var['checkData'])


    def project_customer_inquiry_lg(self,var):
        '''查询项目用户'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        #项目客户-查询
        self.clientStandingBookPO.project_customer_inquiry(var['parameter'])
        #对比列表中的数据，当前页没有找到点击下一页继续找，直到最后一页
        #self.clientStandingBookPO.contrast_list_data(var['checkData'])


    def booking_customer_inquiry_lg(self,var):
        '''查询预约用户'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        #预约客户-查询
        self.clientStandingBookPO.booking_customer_inquiry(var['parameter'])
        #对比列表中的数据，当前页没有找到点击下一页继续找，直到最后一页
        #self.clientStandingBookPO.contrast_list_data(var['checkData'])


    def review_customer_detail_lg(self,var):
        '''预约客户-查看客户列表的详情'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        #查看预约客户列表详情
        self.clientStandingBookPO.review_customer_detail()
        #关闭预约客户明细页面
        self.clientStandingBookPO.close_customer_detail()


    def export_booking_customer_list_lg(self,var):
        '''导出预约客户列表'''
        #切换集团客户/区域客户/项目客户/预约客户的Tab
        self.clientStandingBookPO.switch_to_tab(var['modelName'])
        # 点击导出列表按钮
        self.clientStandingBookPO.export_list(var['modelName']+'-')

    def into_clientStandingBook_page(self):
        '''打开用户管理-客户台账'''
        self.MenuManager.choiceMenu("用户管理","用户管理-客户台账")