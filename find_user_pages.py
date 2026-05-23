import requests
import re

base_url = 'https://doc.crmeb.com/pro_s/prov40'

print("搜索用户管理相关页面...")
print("=" * 60)

for page_id in range(34500, 34600):
    url = f"{base_url}/{page_id}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            if '用户管理' in response.text and '一、功能介绍' in response.text:
                title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', response.text)
                if title_match:
                    title = title_match.group(1)
                    if '用户管理' in title or '用户运营' in title or '用户列表' in title:
                        print(f"\n找到页面 {page_id}: {title}")
                        
                        content_match = re.search(r'<div class="markdown-body[^>]*>(.*?)</div>', response.text, re.DOTALL)
                        if content_match:
                            content = content_match.group(1)
                            if len(content) > 100:
                                print(f"  内容摘要: {content[:150]}...")
    except:
        pass

print("\n" + "=" * 60)
print("搜索完成")
