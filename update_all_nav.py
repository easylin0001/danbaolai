import os
import re

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

with open('/Users/shensizaowu-designer/Documents/trae_projects/test_1/nav_structure.txt', 'r', encoding='utf-8') as f:
    nav_html = f.read()

sidebar_css = '''
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            width: 260px;
            height: 100vh;
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
            overflow-y: auto;
            z-index: 1000;
        }
        .sidebar::-webkit-scrollbar {
            width: 6px;
        }
        .sidebar::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.2);
            border-radius: 3px;
        }
        .sidebar-header {
            padding: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .sidebar-header h2 {
            color: white;
            font-size: 18px;
        }
        .sidebar-content {
            padding: 10px 0;
        }
        .nav-section {
            margin-bottom: 5px;
        }
        .nav-title {
            color: #4fc3f7;
            font-size: 13px;
            padding: 10px 15px 5px 15px;
            font-weight: bold;
        }
        .nav-subsection {
            margin-left: 15px;
        }
        .nav-subtitle {
            color: rgba(255,255,255,0.5);
            font-size: 12px;
            padding: 5px 15px 3px 15px;
            font-weight: normal;
        }
        .nav-link {
            display: block;
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            padding: 5px 15px 5px 25px;
            font-size: 13px;
            transition: all 0.2s;
        }
        .nav-link.sub {
            padding-left: 35px;
            font-size: 12px;
        }
        .nav-link:hover {
            background: rgba(255,255,255,0.1);
            color: white;
        }
        .nav-link.active {
            background: white;
            color: black;
            text-decoration: underline;
        }
        .main-content {
            margin-left: 260px;
        }
        @media (max-width: 768px) {
            .sidebar {
                width: 200px;
            }
            .main-content {
                margin-left: 200px;
            }
        }
'''

search_box_html = '''
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="搜索全站内容..." onkeyup="handleSearch(event)">
                <button onclick="performSearch()">🔍</button>
                <div id="searchResults" class="search-results"></div>
            </div>'''

search_css = '''
        .search-box {
            position: relative;
            margin-bottom: 15px;
        }
        .search-box input {
            width: 100%;
            padding: 10px 40px 10px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
            outline: none;
        }
        .search-box input:focus {
            border-color: #4fc3f7;
        }
        .search-box button {
            position: absolute;
            right: 5px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        .search-results {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            max-height: 400px;
            overflow-y: auto;
            z-index: 1000;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .search-results.show {
            display: block;
        }
        .search-item {
            padding: 10px 15px;
            border-bottom: 1px solid #eee;
            cursor: pointer;
        }
        .search-item:hover {
            background: #f5f7fa;
        }
        .search-item:last-child {
            border-bottom: none;
        }
        .search-item-title {
            font-weight: bold;
            color: #191919;
            margin-bottom: 5px;
        }
        .search-item-content {
            font-size: 12px;
            color: #666;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .search-item-content mark {
            background: #ffeb3b;
            padding: 0 2px;
        }
        .no-results {
            padding: 15px;
            text-align: center;
            color: #999;
        }
'''

search_js = '''
    <script>
        let searchData = [];
        
        async function loadSearchData() {
            try {
                const response = await fetch('search_index.json');
                searchData = await response.json();
            } catch (e) {
                console.log('搜索数据加载失败');
            }
        }
        
        loadSearchData();
        
        function handleSearch(event) {
            if (event.key === 'Enter') {
                performSearch();
            } else if (event.key === 'Escape') {
                hideResults();
            }
        }
        
        function performSearch() {
            const query = document.getElementById('searchInput').value.trim().toLowerCase();
            const resultsDiv = document.getElementById('searchResults');
            
            if (!query) {
                hideResults();
                return;
            }
            
            const results = [];
            
            for (let item of searchData) {
                const titleMatch = item.title.toLowerCase().includes(query);
                const contentMatch = item.content.toLowerCase().includes(query);
                
                if (titleMatch || contentMatch) {
                    let snippet = '';
                    if (contentMatch) {
                        const idx = item.content.toLowerCase().indexOf(query);
                        const start = Math.max(0, idx - 30);
                        const end = Math.min(item.content.length, idx + query.length + 50);
                        snippet = (start > 0 ? '...' : '') + 
                                  item.content.substring(start, end) + 
                                  (end < item.content.length ? '...' : '');
                    } else {
                        snippet = item.content.substring(0, 80) + '...';
                    }
                    
                    const highlighted = snippet.replace(
                        new RegExp(query, 'gi'),
                        match => '<mark>' + match + '</mark>'
                    );
                    
                    results.push({
                        title: item.title,
                        url: item.url,
                        snippet: highlighted
                    });
                    
                    if (results.length >= 20) break;
                }
            }
            
            if (results.length > 0) {
                resultsDiv.innerHTML = results.map(r => 
                    '<div class="search-item" onclick="goToResult(\\'' + r.url + '\\')">' +
                    '<div class="search-item-title">' + r.title + '</div>' +
                    '<div class="search-item-content">' + r.snippet + '</div>' +
                    '</div>'
                ).join('');
            } else {
                resultsDiv.innerHTML = '<div class="no-results">未找到相关内容</div>';
            }
            
            resultsDiv.classList.add('show');
        }
        
        function goToResult(url) {
            window.location.href = url;
        }
        
        function hideResults() {
            document.getElementById('searchResults').classList.remove('show');
        }
        
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.search-box')) {
                hideResults();
            }
        });
    </script>'''

files = [f for f in os.listdir(docs_dir) if f.endswith('.html')]

print(f"更新 {len(files)} 个文件的导航栏...")

updated_count = 0

for filename in files:
    filepath = os.path.join(docs_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    current_page = filename.replace('.html', '')
    nav_with_active = nav_html.replace(f'href="{current_page}.html"', f'href="{current_page}.html" class="active"')
    nav_with_active = nav_with_active.replace(f'href="{current_page}.html" class="nav-link"', f'href="{current_page}.html" class="nav-link active"')
    
    if '<div class="sidebar">' in content:
        old_nav_match = content.find('<div class="sidebar">')
        old_nav_end = content.find('</div>\n    <div class="main-content">')
        if old_nav_match != -1 and old_nav_end != -1:
            content = content[:old_nav_match] + nav_with_active + content[old_nav_end+6:]
    
    if '.sidebar {' not in content:
        content = content.replace('<style>', '<style>\n' + sidebar_css + search_css)
    
    if 'id="searchInput"' not in content:
        content = content.replace('<div class="header">', '<div class="header">' + search_box_html)
    
    if 'loadSearchData()' not in content:
        content = content.replace('</body>', search_js + '\n</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    updated_count += 1
    if updated_count % 50 == 0:
        print(f"  已更新 {updated_count} 个文件...")

print(f"\n导航栏更新完成! 共更新 {updated_count} 个文件")
