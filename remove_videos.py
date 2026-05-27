import os
import re

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

files = [f for f in os.listdir(docs_dir) if f.startswith('page_') and f.endswith('.html')]
print(f"找到 {len(files)} 个页面需要处理...")

updated_count = 0
removed_count = 0

for i, filename in enumerate(files):
    filepath = os.path.join(docs_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    patterns = [
        r'<h3[^>]*>.*?视频讲解.*?</h3>\s*<p>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<h3[^>]*>.*?视频教程.*?</h3>\s*<p>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<h3[^>]*>.*?视频.*?</h3>\s*<p>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<h4[^>]*>.*?视频讲解.*?</h4>\s*<p>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<h3[^>]*>.*?视频讲解.*?</h3>\s*<h4[^>]*>.*?</h4>\s*<p>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<h3[^>]*>.*?视频讲解.*?</h3>\s*<p>\s*bilibili\.com/video[^<]*</p>',
        r'<h3[^>]*>.*?视频讲解.*?</h3>\s*<p>\s*<strong[^>]*>.*?</strong>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*<br>\s*<strong[^>]*>.*?</strong>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<pre><code>视频讲解：[^<]*bilibili\.com[^<]*</code></pre>',
        r'<h4[^>]*>.*?</h4>\s*<p>\s*<a[^>]*href="[^"]*bilibili\.com[^"]*"[^>]*>.*?</a>\s*</p>',
        r'<p>\s*<iframe[^>]*src="[^"]*player\.bilibili\.com[^"]*"[^>]*>.*?</iframe>\s*<br>.*?</p>',
        r'<h4[^>]*>.*?</h4>\s*<iframe[^>]*src="[^"]*player\.bilibili\.com[^"]*"[^>]*>.*?</iframe>',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            removed_count += len(matches)
            content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f"[{i+1}/{len(files)}] 更新 {filename} - 删除了 {len(matches)} 个视频内容")

print(f"\n完成! 共更新 {updated_count} 个页面，删除了 {removed_count} 个视频内容")