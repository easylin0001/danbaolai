import requests
import re
import json

base_url = 'https://doc.crmeb.com/pro_s/prov40'

print("正在获取目标网站完整的导航结构...")
print("=" * 80)

response = requests.get(f"{base_url}/34492", timeout=30)
content = response.text

nav_data_match = re.search(r'wikiMenus\s*[:=]\s*(\[.*?\])', content, re.DOTALL)

if nav_data_match:
    nav_json = nav_data_match.group(1)
    
    try:
        nav_data = json.loads(nav_json)
        
        for item in nav_data:
            if '用户' in item.get('name', ''):
                print(f"\n找到模块: {item['name']}")
                print("-" * 80)
                
                if 'children' in item:
                    for child in item['children']:
                        print(f"  二级导航: {child['name']}")
                        
                        if 'children' in child:
                            for grandchild in child['children']:
                                print(f"    三级导航: {grandchild['name']}")
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
else:
    print("未找到导航数据，尝试从HTML中提取...")
    
    user_section = re.search(r'用户管理.*?(?=<div class="nav-section|$)', content, re.DOTALL)
    
    if user_section:
        print("\n用户管理模块内容：")
        print(user_section.group(0)[:500])
    else:
        print("未找到用户管理模块")

print("\n" + "=" * 80)
