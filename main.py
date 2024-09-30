from pathlib import Path
import os
from getURLs import process_bookmarks

def check_html_file_exists(file_path):
    path = Path(file_path)
    if path.is_file():
        if path.suffix.lower() == '.html':
            return True
    return False
path = input("请输入包含mc百科mod页面的书签的html文件地址(请不要有双引号)：")
if check_html_file_exists(path):
    print("请稍等")
    process_bookmarks(path)
else:
    print("请输入正确的文件目录！")

os.system("pause")