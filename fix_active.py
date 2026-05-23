import os

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

files = [f for f in os.listdir(docs_dir) if f.endswith('.html')]

print(f"修复 {len(files)} 个文件的active class...")

for filename in files:
    filepath = os.path.join(docs_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('class="active" class="nav-link"', 'class="nav-link active"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("修复完成!")
