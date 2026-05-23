import requests
import re

base_url = 'https://doc.crmeb.com/pro_s/prov40'

search_keywords = [
    '用户列表',
    '用户分组',
    '用户标签',
    '用户设置',
    '用户等级',
    '新人礼包',
    '激活有礼',
    '活动说明',
    '优惠券活动'
]

print("搜索用户管理相关页面...")
print("=" * 80)

found_pages = {}

for keyword in search_keywords:
    print(f"\n搜索: {keyword}")
    
    search_url = f"https://doc.crmeb.com/api/search?cid=0&search={keyword}"
    
    try:
        response = requests.get(search_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 200 and data.get('data'):
                articles = data['data'].get('list', [])
                
                for article in articles[:5]:
                    title = article.get('title', '')
                    article_id = article.get('id', '')
                    url = article.get('url', '')
                    
                    if 'prov40' in url or 'pro_s' in url:
                        print(f"  找到: {title} (ID: {article_id})")
                        found_pages[article_id] = title
    except Exception as e:
        print(f"  搜索失败: {e}")

print("\n" + "=" * 80)
print("\n找到的页面：")
for page_id, title in found_pages.items():
    print(f"  {title}: page_{page_id}.html")
