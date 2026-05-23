import os

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

files = ['page_34626.html', 'search_index.json']

print("替换 CRM 字样...")

for filename in files:
    filepath = os.path.join(docs_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('CRM', '后台')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("完成!")
