import re
import os
from datetime import datetime

def extract_urls(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    return urls

def save_urls_to_file(urls):
    current_time = datetime.now().strftime("%Y%m%d-%H%M")
    file_name = f"{current_time}.txt"
    urls_dir = os.path.join(os.path.dirname(__file__), 'URLs')
    os.makedirs(urls_dir, exist_ok=True)
    file_path = os.path.join(urls_dir, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')
    
    return file_path

def process_bookmarks(html_file):
    urls = extract_urls(html_file)
    file_path = save_urls_to_file(urls)
    print(f"URLs 已保存到 {file_path}")