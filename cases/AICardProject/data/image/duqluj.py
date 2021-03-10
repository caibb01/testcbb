#coding:utf-8
import os

class classPath():
    def pathlist(self):
        # 读取当前路径
        current_dir = os.path.abspath(os.path.dirname(__file__))
        print(current_dir)  # F:\project\pritice

        current_dir1 = os.path.dirname(__file__)
        print(current_dir1)  # F:/project/pritice

        # 读取上上级目录
        parent_path = os.path.dirname(current_dir1)
        print(parent_path)  # F:/project

        # 读取上一级目录
        parent_path1 = os.path.dirname(parent_path)
        print(parent_path1)  # F:/

        parent_path2 = os.path.dirname(current_dir)
        print(parent_path2 + "\\report\TestRun")  # F:\project
        print (r""+parent_path2+"")

    def case_path(self):
        '''
        :return: 框架中用例的目录
        '''
        case_path = classPath().pathlist().parent_path2 + r"\\TestCasesRepository\AIcardTest"
        return case_path
        print (case_path)
    def cs(self,p1="",p2=""):
        if p1!="":
            print("P1",p1)
        elif p2!="":
            print("P2",p2)
        else:
            print("111111111111")


if __name__ == '__main__':
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # print(current_dir)  # F:\project\pritice
    # # 读取上上级目录
    # print(2222222222)
    # parent_path = os.path.dirname(current_dir)
    # print(parent_path)  # F:/project
    # classPath().pathlist()
    t =classPath()
    print(t.cs(p1="2"))
