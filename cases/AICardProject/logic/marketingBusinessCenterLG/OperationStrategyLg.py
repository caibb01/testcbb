from cases.AICardProject.page.marketingBusinessCenterPO.OperationStrategyPO import OperationStrategyPO


class OperationStrategyLg:

    def __init__(self, driver):
        self.driver = driver
        self.OperationStrategyPO = OperationStrategyPO(driver)

    def enter_operation_strategy_lg(self):
        # 进入营销业务中心--运营策略
        self.OperationStrategyPO.enter_operation_strategy()

    def new_visit_transformation_strategy_lg(self, var):
        # 新建到访转化策略
        self.OperationStrategyPO.new_visit_transformation_strategy(params=var)

    def new_transaction_conversion_strategy_lg(self, var):
        # 新建成交转化策略
        self.OperationStrategyPO.new_transaction_conversion_strategy(params=var)

    def new_consultant_transformation_strategy_lg(self, var):
        # 新建顾问转化策略
        self.OperationStrategyPO.new_consultant_transformation_strategy(params=var)

    def pause_visit_conversion_strategy_lg(self):
        # 暂停到访转化策略
        self.OperationStrategyPO.pause_visit_conversion_strategy()

    def pause_transaction_conversion_strategy_lg(self):
        # 暂停成交转化策略
        self.OperationStrategyPO.pause_transaction_conversion_strategy()

    def pause_consultant_conversion_strategy_lg(self):
        # 暂停顾问转化策略
        self.OperationStrategyPO.pause_consultant_transformation_strategy()


    def delete_visit_conversion_policy_lg(self):
        # 删除到访转化策略
        self.OperationStrategyPO.delete_visit_conversion_policy()

    def delete_transaction_conversion_policy_lg(self):
        # 删除成交转化策略
        self.OperationStrategyPO.delete_transaction_conversion_policy()

    def delete_consultant_conversion_policy_lg(self):
        # 删除顾问转化策略
        self.OperationStrategyPO.delete_consultant_conversion_policy()


    def open_visit_conversion_strategy_lg(self):
        # 开启到访转化策略
        self.OperationStrategyPO.open_visit_conversion_strategy()

    def view_visit_forwarding_policy_details_lg(self):
        # 查看到访转化策略详情
        self.OperationStrategyPO.view_visit_forwarding_policy_details()

    def view_visit_forwarding_policy_data_lg(self):
        # 查看到访转化策略数据
        self.OperationStrategyPO.view_visit_forwarding_policy_data()

    def type_search_lg(self):
        # 类型搜索策略
        self.OperationStrategyPO.type_search()

    def status_search_lg(self):
        # 状态筛选策略
        self.OperationStrategyPO.status_search()

    def title_search_lg(self, var):
        # 标题筛选策略
        self.OperationStrategyPO.title_search(params=var)

    def edit_visit_transformation_operation_strategy_lg(self):
        # 编辑到访转化策略后发布
        self.OperationStrategyPO.edit_visit_transformation_operation_strategy()

    def cannot_delete_directly_lg(self):
        # 到访转化策略开启状态下点击删除
        self.OperationStrategyPO.cannot_delete_directly()
