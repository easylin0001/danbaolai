import requests
import re

url = 'https://doc.crmeb.com/pro_s/prov40/34492'

response = requests.get(url)
content = response.text

nav_section = re.search(r'<div class="sidebar-nav"[^>]*>(.*?)</div>\s*</div>\s*<div class="main', content, re.DOTALL)

if nav_section:
    nav_html = nav_section.group(1)
    
    sections = re.findall(r'<div class="nav-section">(.*?)</div>\s*</div>', nav_html, re.DOTALL)
    
    for section in sections:
        title_match = re.search(r'<div class="nav-title[^"]*"[^>]*>([^<]+)</div>', section)
        if title_match:
            title = title_match.group(1).strip()
            
            if '用户' in title:
                print(f"\n找到模块: {title}")
                
                links = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', section)
                for link, text in links:
                    page_id = link.split('/')[-1] if '/' in link else link
                    print(f"  - {text.strip()} (ID: {page_id})")
else:
    print("未找到导航区域")
    print("\n尝试查找所有导航链接...")
    all_links = re.findall(r'<a[^>]*href="/pro_s/prov40/(\d+)"[^>]*>([^<]+)</a>', content)
    
    user_links = [(pid, text) for pid, text in all_links if '用户' in text or '会员' in text]
    
    if user_links:
        print("\n找到用户相关的链接：")
        for pid, text in user_links[:20]:
            print(f"  {text.strip()} - ID: {pid}")
