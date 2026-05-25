import os
import re

docs_dir = '/Users/shensizaowu-designer/Documents/trae_projects/test_1/manual_docs'

nav_structure = '''
        <div class="sidebar">
            <div class="sidebar-header">
                <h2>📖 使用手册</h2>
            </div>
            <div class="sidebar-content">
                <div class="nav-section">
                    <div class="nav-title">📦 商品管理</div>
                    <a href="page_34492.html" class="nav-link">商品管理</a>
                    <a href="page_34495.html" class="nav-link">商品添加</a>
                    <a href="page_34496.html" class="nav-link">商品采集</a>
                    <a href="page_34493.html" class="nav-link">商品分类</a>
                    <a href="page_34494.html" class="nav-link">商品规格</a>
                    <a href="page_34497.html" class="nav-link">商品评价</a>
                    <a href="page_34564.html" class="nav-link">商品品牌</a>
                    <a href="page_34599.html" class="nav-link">商品单位</a>
                    <a href="page_34611.html" class="nav-link">商品参数</a>
                    <a href="page_34612.html" class="nav-link">保障服务</a>
                    <a href="page_34613.html" class="nav-link">商品标签</a>
                    <a href="page_34830.html" class="nav-link">商品推荐</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">👥 用户管理</div>
                    <a href="page_34503.html" class="nav-link">用户管理</a>
                    <a href="page_34649.html" class="nav-link">用户列表</a>
                    <a href="page_34504.html" class="nav-link">用户等级</a>
                    <a href="page_34818.html" class="nav-link">用户运营</a>
                    <a href="page_34819.html" class="nav-link">新人礼包</a>
                    <a href="page_34820.html" class="nav-link">激活有礼</a>
                    <a href="page_34671.html" class="nav-link">优惠券</a>
                    <a href="page_34628.html" class="nav-link">账号注销</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">📋 订单管理</div>
                    <a href="page_34498.html" class="nav-link">订单管理</a>
                    <a href="page_34499.html" class="nav-link">订单发货</a>
                    <a href="page_34500.html" class="nav-link">订单退款</a>
                    <a href="page_34501.html" class="nav-link">订单打印</a>
                    <a href="page_34502.html" class="nav-link">订单提醒</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">💬 客服管理</div>
                    <a href="page_34506.html" class="nav-link">客服管理</a>
                    <a href="page_34507.html" class="nav-link">客服功能</a>
                    <a href="page_34508.html" class="nav-link">客服接待</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🎁 营销管理</div>
                    <a href="page_34509.html" class="nav-link">营销管理</a>
                    <a href="page_34677.html" class="nav-link">抽奖</a>
                    <a href="page_34780.html" class="nav-link">礼品卡</a>
                    <a href="page_34781.html" class="nav-link">礼品卡功能说明</a>
                    <a href="page_34510.html" class="nav-link">拼团</a>
                    <a href="page_34511.html" class="nav-link">秒杀</a>
                    <a href="page_34512.html" class="nav-link">砍价</a>
                    <a href="page_34513.html" class="nav-link">积分</a>
                    <a href="page_34681.html" class="nav-link">每日签到</a>
                    <a href="page_34505.html" class="nav-link">付费会员</a>
                    <a href="page_34517.html" class="nav-link">优惠套餐</a>
                    <a href="page_34594.html" class="nav-link">余额充值</a>
                    <a href="page_34606.html" class="nav-link">优惠活动</a>
                    <a href="page_34664.html" class="nav-link">活动背景图</a>
                    <a href="page_34665.html" class="nav-link">活动边框</a>
                    <a href="page_34784.html" class="nav-link">好友送礼</a>
                    <a href="page_34785.html" class="nav-link">好友送礼功能说明</a>
                    <a href="page_34786.html" class="nav-link">收送礼品</a>
                    <a href="page_34810.html" class="nav-link">自动化运营</a>
                    <a href="page_34811.html" class="nav-link">智能推送</a>
                    <a href="page_34813.html" class="nav-link">生日有礼</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">📝 内容管理</div>
                    <a href="page_34728.html" class="nav-link">内容管理</a>
                    <a href="page_34729.html" class="nav-link">社区</a>
                    <a href="page_34732.html" class="nav-link">社区评论</a>
                    <a href="page_34651.html" class="nav-link">文章管理</a>
                    <a href="page_34652.html" class="nav-link">文章分类</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">📺 直播管理</div>
                    <a href="page_34864.html" class="nav-link">直播管理</a>
                    <a href="page_34865.html" class="nav-link">直播前准备</a>
                    <a href="page_34866.html" class="nav-link">阿里云直播配置</a>
                    <a href="page_35613.html" class="nav-link">阿里云资费说明</a>
                    <a href="page_34867.html" class="nav-link">OBS</a>
                    <a href="page_34868.html" class="nav-link">直播功能</a>
                    <a href="page_35608.html" class="nav-link">直播列表</a>
                    <a href="page_35610.html" class="nav-link">中控台</a>
                    <a href="page_35611.html" class="nav-link">观众列表</a>
                    <a href="page_35612.html" class="nav-link">直播统计</a>
                    <a href="page_35609.html" class="nav-link">直播设置</a>
                    <a href="page_35614.html" class="nav-link">小程序直播</a>
                    <a href="page_34696.html" class="nav-link">直播间管理</a>
                    <a href="page_34697.html" class="nav-link">直播商品管理</a>
                    <a href="page_34698.html" class="nav-link">主播管理</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">💰 分销管理</div>
                    <a href="page_34518.html" class="nav-link">分销管理</a>
                    <a href="page_34741.html" class="nav-link">分销员申请</a>
                    <a href="page_34519.html" class="nav-link">分销介绍</a>
                    <a href="page_34520.html" class="nav-link">分销配置</a>
                    <a href="page_34521.html" class="nav-link">分销等级</a>
                    <a href="page_34522.html" class="nav-link">分销员管理</a>
                    <a href="page_34523.html" class="nav-link">佣金提现</a>
                    <a href="page_34734.html" class="nav-link">团队管理</a>
                    <a href="page_34735.html" class="nav-link">团队列表</a>
                    <a href="page_34736.html" class="nav-link">代理商列表</a>
                    <a href="page_34737.html" class="nav-link">代理商申请</a>
                    <a href="page_34738.html" class="nav-link">团队配置</a>
                    <a href="page_34739.html" class="nav-link">团队统计</a>
                    <a href="page_34740.html" class="nav-link">团队订单</a>
                    <a href="page_34748.html" class="nav-link">返佣说明</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">💵 财务管理</div>
                    <a href="page_34595.html" class="nav-link">财务管理</a>
                    <a href="page_34596.html" class="nav-link">财务操作</a>
                    <a href="page_34597.html" class="nav-link">财务记录</a>
                    <a href="page_34598.html" class="nav-link">佣金记录</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🎨 商城装修</div>
                    <a href="page_34524.html" class="nav-link">商城装修</a>
                    <a href="page_34525.html" class="nav-link">主页装修</a>
                    <a href="page_34711.html" class="nav-link">商品详情</a>
                    <a href="page_34709.html" class="nav-link">个人中心</a>
                    <a href="page_34710.html" class="nav-link">商品分类</a>
                    <a href="page_34605.html" class="nav-link">页面配置</a>
                    <a href="page_34699.html" class="nav-link">系统表单</a>
                    <a href="page_34742.html" class="nav-link">悬浮按钮</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">📱 移动端商家管理</div>
                    <a href="page_34701.html" class="nav-link">移动端商家管理</a>
                    <a href="page_34715.html" class="nav-link">商家管理开关</a>
                    <a href="page_34702.html" class="nav-link">工作台模块</a>
                    <a href="page_34703.html" class="nav-link">商品管理</a>
                    <a href="page_34704.html" class="nav-link">订单管理</a>
                    <a href="page_34705.html" class="nav-link">扫码核销</a>
                    <a href="page_34706.html" class="nav-link">售后维权</a>
                    <a href="page_34707.html" class="nav-link">用户管理</a>
                    <a href="page_34708.html" class="nav-link">代客下单</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">⚙️ 商城设置</div>
                    <a href="page_34576.html" class="nav-link">商城设置</a>
                    <a href="page_34745.html" class="nav-link">系统设置</a>
                    <a href="page_34717.html" class="nav-link">同城配送</a>
                    <a href="page_34690.html" class="nav-link">商品设置</a>
                    <a href="page_34530.html" class="nav-link">邮费结构</a>
                    <a href="page_34531.html" class="nav-link">发货设置</a>
                    <a href="page_34532.html" class="nav-link">运费模板</a>
                    <a href="page_34581.html" class="nav-link">物流公司</a>
                    <a href="page_34582.html" class="nav-link">城市数据</a>
                    <a href="page_34583.html" class="nav-link">配送员管理</a>
                    <a href="page_34578.html" class="nav-link">支付设置</a>
                    <a href="page_34577.html" class="nav-link">交易设置</a>
                    <a href="page_34663.html" class="nav-link">定时任务</a>
                    <a href="page_34691.html" class="nav-link">政策协议</a>
                    <a href="page_34743.html" class="nav-link">单据设置</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🔌 应用设置</div>
                    <a href="page_34579.html" class="nav-link">应用设置</a>
                    <a href="page_34580.html" class="nav-link">服务号</a>
                    <a href="page_34584.html" class="nav-link">小程序</a>
                    <a href="page_34585.html" class="nav-link">PC</a>
                    <a href="page_34586.html" class="nav-link">APP</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🔗 第三方接口</div>
                    <a href="page_34587.html" class="nav-link">第三方接口</a>
                    <a href="page_34727.html" class="nav-link">一号通配置</a>
                    <a href="page_34588.html" class="nav-link">小票打印配置</a>
                    <a href="page_34589.html" class="nav-link">采集商品配置</a>
                    <a href="page_34590.html" class="nav-link">物流查询</a>
                    <a href="page_34591.html" class="nav-link">电子面单</a>
                    <a href="page_34670.html" class="nav-link">地图配置</a>
                    <a href="page_34593.html" class="nav-link">短信</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🏢 企业微信</div>
                    <a href="page_34615.html" class="nav-link">企业微信</a>
                    <a href="page_34616.html" class="nav-link">客户管理</a>
                    <a href="page_34619.html" class="nav-link">企业渠道码</a>
                    <a href="page_34620.html" class="nav-link">欢迎语</a>
                    <a href="page_34695.html" class="nav-link">员工列表</a>
                    <a href="page_34621.html" class="nav-link">客户列表</a>
                    <a href="page_34622.html" class="nav-link">客户群发</a>
                    <a href="page_34623.html" class="nav-link">朋友圈列表</a>
                    <a href="page_34617.html" class="nav-link">客户群运营</a>
                    <a href="page_34624.html" class="nav-link">客户群列表</a>
                    <a href="page_34625.html" class="nav-link">自动拉群</a>
                    <a href="page_34626.html" class="nav-link">客户群群发</a>
                    <a href="page_34618.html" class="nav-link">企业微信设置</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🏭 供应商</div>
                    <a href="page_34642.html" class="nav-link">供应商</a>
                    <a href="page_34692.html" class="nav-link">供应商申请</a>
                    <a href="page_34643.html" class="nav-link">供应商管理</a>
                    <a href="page_34644.html" class="nav-link">供应商财务</a>
                    <a href="page_34723.html" class="nav-link">供应商菜单设置</a>
                    <a href="page_34645.html" class="nav-link">供应商后台</a>
                    <a href="page_34693.html" class="nav-link">供应商商品</a>
                    <a href="page_34646.html" class="nav-link">供应商订单</a>
                    <a href="page_34694.html" class="nav-link">财务信息</a>
                    <a href="page_34647.html" class="nav-link">供应商设置</a>
                    <a href="page_34648.html" class="nav-link">供应商硬件配置</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🛒 采购商</div>
                    <a href="page_34782.html" class="nav-link">采购商</a>
                    <a href="page_34783.html" class="nav-link">采购商说明</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🖥️ 商城硬件</div>
                    <a href="page_34571.html" class="nav-link">商城硬件</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">📱 移动端UI鉴赏</div>
                    <a href="page_34712.html" class="nav-link">移动端UI鉴赏</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">🤖 商城AI</div>
                    <a href="page_34821.html" class="nav-link">商城AI</a>
                    <a href="page_34822.html" class="nav-link">功能介绍</a>
                </div>
                <div class="nav-section">
                    <div class="nav-title">📦 库存管理</div>
                    <a href="page_34831.html" class="nav-link">库存管理</a>
                    <a href="page_34832.html" class="nav-link">入库管理</a>
                    <a href="page_34833.html" class="nav-link">出库管理</a>
                    <a href="page_34834.html" class="nav-link">库存查询</a>
                    <a href="page_34835.html" class="nav-link">库存盘点</a>
                    <a href="page_34836.html" class="nav-link">出入库记录</a>
                </div>
            </div>
        </div>'''

print("导航结构已生成")
print(f"导航HTML长度: {len(nav_structure)} 字符")

with open('/Users/shensizaowu-designer/Documents/trae_projects/test_1/nav_structure.txt', 'w', encoding='utf-8') as f:
    f.write(nav_structure)

print("导航结构已保存到 nav_structure.txt")

existing_pages = set()
for filename in os.listdir(docs_dir):
    if filename.startswith('page_') and filename.endswith('.html'):
        page_id = filename.replace('page_', '').replace('.html', '')
        existing_pages.add(page_id)

nav_pages = set(re.findall(r'page_(\d+)\.html', nav_structure))

print(f"\n导航中的页面数: {len(nav_pages)}")
print(f"实际存在的页面数: {len(existing_pages)}")

missing_in_nav = existing_pages - nav_pages
missing_in_files = nav_pages - existing_pages

if missing_in_nav:
    print(f"\n存在但未在导航中的页面: {len(missing_in_nav)}")
if missing_in_files:
    print(f"\n导航中但文件不存在的页面: {len(missing_in_files)}")
    for p in sorted(missing_in_files):
        print(f"  - page_{p}.html")
