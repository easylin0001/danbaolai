import os
import re
import requests

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

missing_pages = {
    '34503': '商品标签',
    '34504': '商品推荐',
    '34524': '账号注销',
    '34544': '活动背景图',
    '34545': '活动边框',
    '34546': '好友送礼',
    '34547': '自动化运营',
    '34552': '小程序直播',
    '34570': '页面配置',
    '34574': '悬浮按钮',
    '34581': '售后维权',
    '34582': '代客下单',
    '34587': '商品设置',
    '34588': '商城邮费',
    '34591': '定时任务',
    '34592': '政策协议',
    '34593': '单据设置',
    '34602': '采集商品配置',
    '34604': '电子面单',
    '34605': '地图配置',
    '34615': '供应商菜单设置',
    '34617': '采购商说明',
    '34618': '商城硬件',
    '34619': '移动端UI鉴赏',
    '34620': '功能介绍',
    '34630': '出入库记录',
}

base_url = 'https://doc.crmeb.com/pro_s/prov40'

print(f"需要下载 {len(missing_pages)} 个缺失页面...")

success_count = 0
fail_count = 0

for i, (page_id, page_name) in enumerate(missing_pages.items()):
    url = f"{base_url}/{page_id}"
    output_file = os.path.join(docs_dir, f"page_{page_id}.html")
    
    print(f"[{i+1}/{len(missing_pages)}] 下载 {page_name} ({page_id})...", end=' ')
    
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            content = response.text
            
            title_match = re.search(r'<title>([^<]+)</title>', content)
            title = title_match.group(1) if title_match else f"会员电商系统{page_name} - DANBAOLAI文档"
            title = title.replace('CRMEB', 'DANBAOLAI').replace('Crmeb', 'Danbaolai').replace('crmeb', 'danbaolai')
            title = re.sub(r'\s*Pro\s*v?4\.0', '', title, flags=re.IGNORECASE)
            
            content_match = re.search(r'<div class="markdown-body editormd-html-preview">(.*?)</div>\s*<div class="footer-detail', content, re.DOTALL)
            if not content_match:
                content_match = re.search(r'<div class="markdown-body editormd-html-preview">(.*?)</div>', content, re.DOTALL)
            
            if content_match:
                body_content = content_match.group(1)
            else:
                body_content = f"<p>{page_name}内容暂无</p>"
            
            body_content = re.sub(r'src="(/uploads/[^"]+/)([^"]+)"', r'src="images/\2"', body_content)
            body_content = body_content.replace('CRMEB', 'DANBAOLAI').replace('Crmeb', 'Danbaolai').replace('crmeb', 'danbaolai')
            
            html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; background: #f5f7fa; color: #333; line-height: 1.8; }}
        .container {{ max-width: 100%; margin: 0; padding: 30px 40px; }}
        .header {{ background: white; color: #191919; padding: 20px; margin-bottom: 30px; border-radius: 10px; }}
        .header h1 {{ font-size: 24px; margin-bottom: 10px; color: #191919; }}
        .back-link {{ display: inline-block; color: #191919; text-decoration: none; margin-bottom: 15px; }}
        .content {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .content h3 {{ color: #1a1a2e; font-size: 20px; margin: 25px 0 15px 0; padding-bottom: 10px; border-bottom: 2px solid #4fc3f7; }}
        .content h4 {{ color: #333; font-size: 16px; margin: 20px 0 10px 0; }}
        .content p {{ margin: 10px 0; color: #555; }}
        .content img {{ max-width: 100%; height: auto; border-radius: 5px; margin: 15px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        .content ul, .content ol {{ margin: 10px 0 10px 25px; }}
        .content li {{ margin: 5px 0; }}
        .content strong {{ color: #1a1a2e; }}
        .content code {{ background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-family: Consolas, monospace; }}
        .content table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
        .content th, .content td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        .content th {{ background: #f5f7fa; }}
        .footer {{ text-align: center; padding: 20px; color: #999; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="../index.html" class="back-link">← 返回目录</a>
            <h1>{title}</h1>
        </div>
        <div class="content">
            {body_content}
        </div>
        <div class="footer">
            <p>DANBAOLAI 使用手册</p>
        </div>
    </div>
</body>
</html>'''
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_template)
            
            print("✓")
            success_count += 1
        else:
            print(f"✗ HTTP {response.status_code}")
            fail_count += 1
    except Exception as e:
        print(f"✗ {e}")
        fail_count += 1

print(f"\n下载完成! 成功: {success_count}, 失败: {fail_count}")
