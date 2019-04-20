## 1、删除当前路径下.txt文件
import os
def delete_currentPath_txtFile(path):
    for fileName in os.listdir(path):
        if fileName.endswith('.txt'):
            os.remove(fileName)

if __name__ == "__main__":
    path = "."
    delete_currentPath_txtFile(path)


## 2、删除输入路径下的.txt文件
import os
def delete_specifiedPath_txtFile(path):
    for fileName in os.listdir(path):
        if fileName.endswith('.txt'):
            os.remove(fileName)

if __name__ == "__main__":
    path = input("请输入绝对路径：(最后一个字符/,表示该文件夹下)\n")
    delete_specifiedPath_txtFile(path)


## 3、删除当前路径下指定的后缀文件
import os
def delete_currentPath_specifiedFile(path, fileType):
    for fileName in os.listdir(path):
        if fileName.endswith("."+fileType):
            os.remove(fileName)

if __name__ == "__main__":
    path = "."
    fileType = input("请输入文件后缀名")
    delete_currentPath_specifiedFile(path, fileType)


## 4、删除输入路径下输入的后缀文件
import os
def delete_specifiedPath_specifiedFile(path, fileType):
    for fileName in os.listdir(path):
        if fileName.endswith("."+fileType):
            os.remove(fileName)

if __name__=="__main__":
    path = input("请输入绝对路径：")
    fileType = input("请输入文件后缀名（不需要带.）")
    delete_specifiedPath_specifiedFile(path, fileType)


## 删除当前路径下文件名含有数字的文件（包括文件夹）
import re
import os
def delete_currentPath_numberFile(path):
    for fileName in os.listdir(path):
        if re.match(r'\d+', fileName):
            os.remove(fileName)

if __name__=="__main__":
    path = "."
    delete_currentPath_numberFile(path)
    

## 删除输入路径下文件名含有数字的文件（包括文件夹）
import re
import os
def delete_specifiedPath_numberFile(path):
    for fileName in os.listdir(path):
        if re.match(r'\d+', fileName):
            os.remove(fileName)

if __name__=="__main__":
    path = input("请输入绝对路径")
    delete_currentPath_numberFile(path)


## 删除当前文件下输入匹配内容的文件（需要用re正则匹配）
# (1)首字母匹配
# (2)尾字母匹配
# (3)中间匹配
# 等等，如果有其他需求，请各位提出


## 删除输入路径下输入匹配内容的文件（相对复杂）