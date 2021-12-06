#-*- encoding=utf8 -*-
from time import sleep
import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.contentManagementPO.projectManagementPO import projectManagement


class projectManagementLg():
    def __init__(self,driver):
        #super(projectManagementLg,self).__init__(driver)
        self.driver = driver
        self.projectManagementPO = projectManagement(driver)
        self.MenuManager = MenuManager(driver)

    def into_projectManagement_page(self):
        '''打开内容管理-项目管理'''
        self.MenuManager.choiceMenu("内容管理", "内容管理-项目管理")

    def publish_multiple_projects_lg(self,var):
        '''发布项目(包含项目已关联区域，未关联区域，项目被禁用)'''
        self.projectManagementPO.publish_multiple_projects(var['publishStatus'])

    def publish_project_lg(self):
        '''发布项目'''
        self.projectManagementPO.publish_project()

    def close_project_lg(self,var):
        '''关闭项目'''
        #发布状态为已发布
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        #关闭项目
        self.projectManagementPO.publish_project()
        sleep(2)

    def edit_project_lg(self,var):
        '''编辑项目'''
        # 发布状态为已发布
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.edit_project()

    def select_project_lg(self,var):
        '''选择或输入系统项目名称'''
        self.projectManagementPO.select_project(var['parameter'])

    def select_city_lg(self):
        '''根据所属城市，查询项目'''
        self.projectManagementPO.select_city()

    def select_publish_status_lg(self,var):
        '''根据发布状态，查询项目'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])

    def query_lg(self,var):
        '''根据项目系统名称、所属城市、发布状态，查询项目'''
        #选择或输入系统项目名称
        self.projectManagementPO.select_project_01(var['parameter'])
        #根据所属城市，查询项目
        self.projectManagementPO.select_city_01()
        #根据发布状态，查询项目
        self.projectManagementPO.select_publish_status_01(var['publishStatus'])


    def reception_list_lg(self,var):
        '''打开接待列表，勾选checkbox'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.reception_list()

    def reception_list_people_search_lg(self,var):
        '''项目接待列表-人员搜索'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.reception_list_people_search()

    def reception_list_people_hide_lg(self,var):
        '''项目接待列表-人员隐藏'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.reception_list_people_hide()

    def reception_list_people_sort_lg(self,var):
        '''项目接待列表-人员排序'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.reception_list_people_sort()

    def reception_list_remove_personnel_lg(self,var):
        '''项目接待列表-删除人员'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.reception_list_remove_personnel()

    def save_reception_list_lg(self,var):
        '''项目接待列表-保存'''
        self.projectManagementPO.select_publish_status(var['publishStatus'])
        self.projectManagementPO.save_reception_list()

    def copy_page_path_lg(self):
        '''复制页面路径'''
        self.projectManagementPO.copy_page_path()

    def page_switching_lg(self):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        self.projectManagementPO.click_next_page()
        self.projectManagementPO.click_previous_page()





