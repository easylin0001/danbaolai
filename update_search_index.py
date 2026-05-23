import os
import re

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

search_index = []

files = [f for f in os.listdir(docs_dir) if f.endswith('.html')]

print(f"生成 {len(files)} 个页面的搜索索引...")

for filename in files:
    filepath = os.path.join(docs_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'<title>([^<]+)</title>', content)
    title = title_match.group(1) if title_match else filename
    
    content_match = re.search(r'<div class="content">(.*?)</div>\s*<div class="footer">', content, re.DOTALL)
    if content_match:
        body = content_match.group(1)
        text = re.sub(r'<[^>]+>', ' ', body)
        text = re.sub(r'\s+', ' ', text).strip()
        snippet = text[:200] if len(text) > 200 else text
    else:
        snippet = ''
    
    search_index.append({
        'title': title,
        'url': filename,
        'content': snippet
    })

import json
output_path = os.path.join(docs_dir, 'search_index.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(search_index, f, ensure_ascii=False, indent=2)

print(f"搜索索引生成完成! 共 {len(search_index)} 条记录")
