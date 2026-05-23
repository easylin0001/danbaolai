import requests

url = 'https://doc.crmeb.com/pro_s/prov40/34492'

print("正在下载目标网站HTML...")

response = requests.get(url, timeout=30)

with open('/Users/shensizaowu-designer/Documents/trae_projects/test_1/target_site.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("HTML已保存到 target_site.html")
print(f"文件大小: {len(response.text)} 字符")
