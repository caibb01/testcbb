import os

__file_path = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../"))


def getFilePath(fileName, parentDirectory="cases\\AICardProject\\data\\image"):
    """ 输入image文件夹下的文件名即可返回此文件的绝对路径
        fileName: 文件名
        parentDirectory：在ui-aicard文件夹往下到文件名的路径
    """
    filePath = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), parentDirectory, fileName)
    return filePath
