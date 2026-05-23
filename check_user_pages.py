import requests
import re

url = 'https://doc.crmeb.com/pro_s/prov40/34492'

print("正在获取目标网站导航结构...")

response = requests.get(url, timeout=30)
content = response.text

user_section = re.search(r'👥 用户管理</div>(.*?)(?=<div class="nav-section|$)', content, re.DOTALL)

if user_section:
    nav_html = user_section.group(1)
    
    links = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', nav_html)
    
    print("\n用户管理模块下的导航项：")
    print("=" * 60)
    
    for link, text in links:
        page_id = link.split('/')[-1] if '/' in link else link
        print(f"  {text.strip():20s} -> page_{page_id}.html")
else:
    print("未找到用户管理模块")
    print("\n尝试查找所有导航模块...")
    
    all_sections = re.findall(r'<div class="nav-title[^"]*"[^>]*>([^<]+)</div>', content)
    print("\n找到的导航模块：")
    for section in all_sections:
        print(f"  - {section}")
