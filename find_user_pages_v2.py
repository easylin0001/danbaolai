import requests
import re

base_url = 'https://doc.crmeb.com/pro_s/prov40'

keywords = ['用户列表', '用户分组', '用户标签', '用户设置', '用户等级', '新人礼包', '激活有礼', '活动说明', '优惠券活动']

print("遍历页面ID查找用户管理相关页面...")
print("=" * 80)

found_pages = {}

for page_id in range(34500, 34800):
    url = f"{base_url}/{page_id}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.text
            
            title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
            if title_match:
                title = title_match.group(1)
                
                for keyword in keywords:
                    if keyword in title:
                        print(f"找到页面 {page_id}: {title}")
                        found_pages[page_id] = title
                        break
    except:
        pass

print("\n" + "=" * 80)
print("\n找到的页面：")
for page_id, title in found_pages.items():
    print(f"  {title}: page_{page_id}.html")
